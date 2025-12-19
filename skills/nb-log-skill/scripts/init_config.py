#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 配置文件生成器

用途：
    一键生成 nb_log_config.py 配置文件模板，包含常用配置项和详细注释

用法：
    python init_config.py [output_path]

示例：
    python init_config.py                    # 在当前目录生成
    python init_config.py /path/to/project   # 在指定目录生成
"""

import sys
from pathlib import Path

# nb_log_config.py 模板内容
CONFIG_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
nb_log 配置文件
自动生成于项目根目录，用于配置全局日志行为
文档：https://nb-log-doc.readthedocs.io/zh-cn/latest/
"""

import logging
from pathlib import Path

# ==================== 日志路径配置 ====================
# 日志文件存放目录
LOG_PATH = Path(__file__).parent / 'logs'

# ==================== 日志级别配置 ====================
# 默认日志级别：DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50
LOG_LEVEL_FILTER = logging.DEBUG

# ==================== 控制台日志配置 ====================
# 是否默认添加控制台 handler
DEFAULUT_IS_ADD_STREAM_HANDLER = True

# 是否使用 loguru 风格的控制台输出
DEFAULUT_IS_USE_LOGURU_STREAM_HANDLER = False

# 控制台日志是否使用彩色（False 则为黑白）
USE_COLORFUL_HANDLER = True

# 是否显示大块背景色（False 只显示文字颜色）
DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = True

# 是否自动为 print 添加点击跳转功能
AUTO_PATCH_PRINT = True

# ==================== 文件日志配置 ====================
# 文件日志 handler 类型
# 1: 多进程安全按大小切割（推荐）
# 2: 多进程安全按时间切割
# 3: 单文件永不切割
# 4: WatchedFileHandler
# 5: 单进程按大小切割
# 6: 单进程按时间切割
# 7: 使用 loguru 文件 handler
LOG_FILE_HANDLER_TYPE = 1

# 单个日志文件大小上限（MB）
LOG_FILE_SIZE = 100

# 日志文件备份数量
LOG_FILE_BACKUP_COUNT = 5

# 是否自动将 error 级别以上日志写入单独文件
AUTO_WRITE_ERROR_LEVEL_TO_SEPARATE_FILE = False

# ==================== 日志格式配置 ====================
# 日志格式模板编号（1-7）
# 1: 简洁格式
# 2: 带进程线程信息
# 3: 详细格式
# 4: JSON 格式
# 5: 推荐格式（默认）
FORMATTER_KIND = 5

# 自定义日志格式模板（可选）
# CUSTOM_FORMATTER = logging.Formatter(
#     '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# ==================== 标准输出重定向配置 ====================
# print 输出自动写入文件（None 表示不写入）
# 设置后会自动每天生成一个文件：2024-01-01.{PRINT_WRTIE_FILE_NAME}
PRINT_WRTIE_FILE_NAME = None  # 例如: 'myapp.print'

# 标准输出自动写入文件（包括 print 和 streamHandler 日志）
SYS_STD_FILE_NAME = None  # 例如: 'myapp.std'

# ==================== 第三方服务配置 ====================
# MongoDB 配置
MONGO_URL = None  # 例如: 'mongodb://localhost:27017'

# Elasticsearch 配置
ELASTIC_HOST = '127.0.0.1'
ELASTIC_PORT = 9200

# Kafka 配置
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'nb_log'

# 邮件配置
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_TO_ADDRS = []

# 钉钉配置
DING_TALK_TOKEN = None
DING_TALK_TIME_INTERVAL = 60  # 钉钉消息发送间隔（秒）

# ==================== 高级配置 ====================
# 是否在导入 nb_log 时显示配置文件路径
SHOW_CONFIG_FILE_PATH_ON_IMPORT = True

# 日志去重间隔（秒），相同日志在此时间内只记录一次
LOG_DEBOUNCE_INTERVAL = 0

# 是否捕获 warnings 模块的警告
CAPTURE_WARNINGS = False
'''


def generate_config(output_dir: str = '.') -> str:
    """
    生成 nb_log_config.py 配置文件

    Args:
        output_dir: 输出目录路径

    Returns:
        生成的配置文件完整路径
    """
    output_path = Path(output_dir)

    # 确保目录存在
    output_path.mkdir(parents=True, exist_ok=True)

    config_file = output_path / 'nb_log_config.py'

    # 检查文件是否已存在
    if config_file.exists():
        response = input(f'[WARN] {config_file} 已存在，是否覆盖？(y/N): ')
        if response.lower() != 'y':
            print('[CANCEL] 已取消')
            return ''

    # 写入配置文件
    config_file.write_text(CONFIG_TEMPLATE, encoding='utf-8')

    # 创建 logs 目录
    logs_dir = output_path / 'logs'
    logs_dir.mkdir(exist_ok=True)

    print(f'[OK] 配置文件已生成: {config_file.absolute()}')
    print(f'[OK] 日志目录已创建: {logs_dir.absolute()}')
    print()
    print('[NEXT] 下一步：')
    print('   1. 根据需要修改 nb_log_config.py 中的配置')
    print('   2. 在代码中使用: from nb_log import get_logger')

    return str(config_file.absolute())


def main():
    """主函数"""
    output_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    generate_config(output_dir)


if __name__ == '__main__':
    main()
