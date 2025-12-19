#!/usr/bin/env python3
"""
提示词质量分析器

分析提示词的质量并提供改进建议
"""

import re
from typing import Dict, List, Tuple
import json


class PromptAnalyzer:
    """提示词分析器"""

    def __init__(self):
        # 质量检查规则
        self.checks = {
            "clarity": self._check_clarity,
            "structure": self._check_structure,
            "specificity": self._check_specificity,
            "examples": self._check_examples,
            "length": self._check_length,
        }

    def analyze(self, prompt: str) -> Dict:
        """
        分析提示词质量

        Args:
            prompt: 待分析的提示词

        Returns:
            分析结果字典，包含评分和建议
        """
        results = {
            "prompt": prompt,
            "length": len(prompt),
            "word_count": len(prompt.split()),
            "scores": {},
            "suggestions": [],
            "overall_score": 0,
        }

        # 运行所有检查
        for name, check_func in self.checks.items():
            score, suggestions = check_func(prompt)
            results["scores"][name] = score
            results["suggestions"].extend(suggestions)

        # 计算总分
        results["overall_score"] = sum(results["scores"].values()) / len(
            self.checks
        )

        return results

    def _check_clarity(self, prompt: str) -> Tuple[int, List[str]]:
        """检查清晰度 (0-100)"""
        score = 100
        suggestions = []

        # 检查模糊词汇
        vague_words = ["一些", "某些", "可能", "大概", "也许", "差不多"]
        found_vague = [w for w in vague_words if w in prompt]
        if found_vague:
            score -= len(found_vague) * 10
            suggestions.append(f"避免模糊词汇: {', '.join(found_vague)}")

        # 检查是否有明确的任务描述
        task_keywords = ["请", "帮我", "创建", "分析", "生成", "编写"]
        if not any(kw in prompt for kw in task_keywords):
            score -= 20
            suggestions.append("添加明确的任务动词（如：请、创建、分析）")

        # 检查句子长度
        sentences = re.split(r'[。！？.!?]', prompt)
        long_sentences = [s for s in sentences if len(s) > 100]
        if long_sentences:
            score -= len(long_sentences) * 5
            suggestions.append(f"有 {len(long_sentences)} 个句子过长，建议拆分")

        return max(0, score), suggestions

    def _check_structure(self, prompt: str) -> Tuple[int, List[str]]:
        """检查结构化程度 (0-100)"""
        score = 50  # 基础分
        suggestions = []

        # 检查 XML 标签
        xml_tags = re.findall(r'<(\w+)>', prompt)
        if xml_tags:
            score += 30
            suggestions.append(f"✓ 使用了 {len(set(xml_tags))} 个 XML 标签")
        else:
            suggestions.append("考虑使用 XML 标签来结构化内容")

        # 检查列表
        has_bullets = bool(re.search(r'[•\-\*]\s', prompt))
        has_numbers = bool(re.search(r'\d+[.、]\s', prompt))
        if has_bullets or has_numbers:
            score += 20
            suggestions.append("✓ 使用了列表结构")
        else:
            suggestions.append("考虑使用列表来组织信息")

        return min(100, score), suggestions

    def _check_specificity(self, prompt: str) -> Tuple[int, List[str]]:
        """检查具体性 (0-100)"""
        score = 50
        suggestions = []

        # 检查具体数字
        numbers = re.findall(r'\d+', prompt)
        if numbers:
            score += 20
            suggestions.append(f"✓ 包含具体数字: {len(numbers)} 处")
        else:
            suggestions.append("添加具体的数字要求（如长度、数量）")

        # 检查格式说明
        format_keywords = ["格式", "JSON", "表格", "列表", "代码"]
        if any(kw in prompt for kw in format_keywords):
            score += 20
            suggestions.append("✓ 指定了输出格式")
        else:
            suggestions.append("明确说明期望的输出格式")

        # 检查约束条件
        constraint_keywords = ["必须", "不要", "仅", "只", "限制"]
        if any(kw in prompt for kw in constraint_keywords):
            score += 10
            suggestions.append("✓ 包含约束条件")

        return min(100, score), suggestions

    def _check_examples(self, prompt: str) -> Tuple[int, List[str]]:
        """检查示例 (0-100)"""
        score = 0
        suggestions = []

        # 检查是否有示例标记
        example_keywords = ["示例", "例如", "比如", "例子", "example"]
        has_examples = any(kw in prompt.lower() for kw in example_keywords)

        if has_examples:
            score = 80
            suggestions.append("✓ 包含示例")

            # 检查示例数量
            example_count = sum(
                prompt.lower().count(kw) for kw in ["示例", "example"]
            )
            if example_count >= 3:
                score = 100
                suggestions.append("✓ 包含多个示例（最佳实践）")
        else:
            suggestions.append("考虑添加示例来说明期望的输出")

        return score, suggestions

    def _check_length(self, prompt: str) -> Tuple[int, List[str]]:
        """检查长度合理性 (0-100)"""
        length = len(prompt)
        suggestions = []

        if length < 20:
            score = 30
            suggestions.append("提示词过短，可能缺少必要信息")
        elif length < 50:
            score = 60
            suggestions.append("提示词较短，考虑添加更多上下文")
        elif length < 200:
            score = 100
            suggestions.append("✓ 长度适中")
        elif length < 500:
            score = 90
            suggestions.append("提示词较长，但仍在合理范围")
        elif length < 1000:
            score = 70
            suggestions.append("提示词较长，考虑结构化或分块")
        else:
            score = 50
            suggestions.append("提示词过长，建议使用链式提示或分块处理")

        return score, suggestions

    def get_grade(self, score: float) -> str:
        """根据分数返回等级"""
        if score >= 90:
            return "优秀 (A)"
        elif score >= 80:
            return "良好 (B)"
        elif score >= 70:
            return "中等 (C)"
        elif score >= 60:
            return "及格 (D)"
        else:
            return "需改进 (F)"

    def format_report(self, results: Dict) -> str:
        """格式化分析报告"""
        report = []
        report.append("=" * 60)
        report.append("提示词质量分析报告")
        report.append("=" * 60)
        report.append(f"\n提示词长度: {results['length']} 字符")
        report.append(f"词数: {results['word_count']}")
        report.append(f"\n总体评分: {results['overall_score']:.1f}/100")
        report.append(f"等级: {self.get_grade(results['overall_score'])}\n")

        report.append("详细评分:")
        report.append("-" * 60)
        score_names = {
            "clarity": "清晰度",
            "structure": "结构化",
            "specificity": "具体性",
            "examples": "示例",
            "length": "长度",
        }
        for key, score in results["scores"].items():
            name = score_names.get(key, key)
            bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
            report.append(f"{name:12s} [{bar}] {score:.0f}/100")

        report.append("\n改进建议:")
        report.append("-" * 60)
        for i, suggestion in enumerate(results["suggestions"], 1):
            if suggestion.startswith("✓"):
                report.append(f"  {suggestion}")
            else:
                report.append(f"{i}. {suggestion}")

        report.append("=" * 60)
        return "\n".join(report)


def main():
    """命令行入口"""
    import sys

    if len(sys.argv) < 2:
        print("用法: python prompt_analyzer.py <提示词文本>")
        print("或者: python prompt_analyzer.py --file <文件路径>")
        sys.exit(1)

    # 读取提示词
    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("请指定文件路径")
            sys.exit(1)
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            prompt = f.read()
    else:
        prompt = " ".join(sys.argv[1:])

    # 分析
    analyzer = PromptAnalyzer()
    results = analyzer.analyze(prompt)

    # 输出报告
    print(analyzer.format_report(results))

    # 如果指定了 --json，输出 JSON 格式
    if "--json" in sys.argv:
        print("\nJSON 输出:")
        print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
