#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 日志重复记录问题演示

测试内容：
    - 演示错误封装导致的日志重复
    - 演示 nb_log 如何防止重复
    - 对比原生 logging 和 nb_log

来源：基于 ydf0509/nb_log 官方测试用例
警告：部分测试会演示错误用法，仅供学习

用法：
    python test_duplicate.py [demo]

参数：
    demo: wrong (演示错误用法) 或 correct (演示正确用法，默认)
"""

import logging
import sys
import time


def demo_wrong_usage_raw_logging():
    """
    演示：原生 logging 错误封装导致重复记录

    这是一个典型的错误示例，展示为什么需要理解观察者模式
    """
    print('\n' + '=' * 50)
    print('演示: 原生 logging 错误封装（[WARN] 反面教材）')
    print('=' * 50)

    class BadLogUtil:
        """
        错误的日志封装类
        每次实例化都会添加新的 handler，导致重复记录
        """
        def __init__(self):
            self.logger = logging.getLogger('bad_example')
            self.logger.setLevel(logging.DEBUG)
            # [ERROR] 每次实例化都添加 handler，这是错误的！
            self.logger.addHandler(logging.StreamHandler())

        def info(self, msg):
            self.logger.info(msg)

    print('调用 5 次，期望输出 5 条日志：')
    print('-' * 30)

    for i in range(5):
        # [ERROR] 在循环内实例化，导致 handler 累积
        log = BadLogUtil()
        log.info(f'第 {i+1} 次调用')

    print('-' * 30)
    print(f'实际输出: 1+2+3+4+5 = 15 条（高斯求和）')
    print()
    print('[ERROR] 原因: 每次实例化都添加了新的 StreamHandler')
    print('   第1次调用有1个handler，第2次有2个...第5次有5个')
    print('   导致日志重复记录，实际记录次数是高斯求和')


def demo_wrong_usage_loguru():
    """
    演示：loguru 错误使用导致重复记录

    loguru 没有命名空间概念，容易造成重复
    """
    print('\n' + '=' * 50)
    print('演示: loguru 错误使用（[WARN] 反面教材）')
    print('=' * 50)

    try:
        from loguru import logger

        def bad_log_to_file(msg):
            """错误：在函数内 add handler"""
            # [ERROR] 每次调用都 add 一个新的 sink
            logger.add('loguru_test.log')
            logger.info(msg)

        print('如果反复调用 logger.add()：')
        print('  - 每次都会添加新的 sink')
        print('  - 日志会写入所有历史添加的 sink')
        print('  - 随时间推移，重复会越来越严重')
        print()
        print('[WARN]  loguru 正确用法是在模块级别只调用一次 logger.add()')

    except ImportError:
        print('[WARN]  loguru 未安装，跳过演示')


def demo_correct_usage_nb_log():
    """
    演示：nb_log 正确用法 - 自动防止重复

    nb_log 会自动检测是否已添加 handler，避免重复
    """
    print('\n' + '=' * 50)
    print('演示: nb_log 正确用法（[OK] 自动防重复）')
    print('=' * 50)

    from nb_log import get_logger

    print('调用 5 次 get_logger()，期望输出 5 条日志：')
    print('-' * 30)

    for i in range(5):
        # [OK] nb_log 会自动检测，不会重复添加 handler
        logger = get_logger('correct_example')
        logger.info(f'第 {i+1} 次调用')

    print('-' * 30)
    print(f'实际输出: 正好 5 条，没有重复！')
    print()
    print('[OK] nb_log 原理:')
    print('   - 相同命名空间返回同一个 logger 对象')
    print('   - 自动检测是否已有 handler')
    print('   - 基于原生 logging，兼容性好')


def demo_correct_module_level():
    """
    演示：正确的模块级别 logger 定义

    即使使用原生 logging，也应该在模块级别定义 logger
    """
    print('\n' + '=' * 50)
    print('演示: 正确的模块级别定义（[OK] 最佳实践）')
    print('=' * 50)

    # [OK] 在模块级别定义 logger，而非函数内
    # 这里为演示放在函数内，实际应放在模块顶部
    module_logger = logging.getLogger('module_level_example')
    module_logger.setLevel(logging.DEBUG)

    # 只在 handler 为空时添加
    if not module_logger.handlers:
        module_logger.addHandler(logging.StreamHandler())

    print('在模块级别定义 logger 的好处：')
    print('  - logger 只创建一次')
    print('  - handler 只添加一次')
    print('  - 整个模块共享同一个 logger')
    print()

    for i in range(3):
        module_logger.info(f'调用 {i+1}')

    print()
    print('[OK] 正确输出 3 条日志')


def demo_nb_log_namespace():
    """
    演示：nb_log 命名空间的威力

    不同命名空间可以有不同的配置
    """
    print('\n' + '=' * 50)
    print('演示: nb_log 命名空间（[OK] 灵活配置）')
    print('=' * 50)

    from nb_log import get_logger

    # 不同命名空间，不同配置
    logger_debug = get_logger('ns_debug', log_level_int=logging.DEBUG)
    logger_warn = get_logger('ns_warn', log_level_int=logging.WARNING)

    print('DEBUG 级别命名空间：')
    logger_debug.debug('debug 消息 - 显示')
    logger_debug.info('info 消息 - 显示')

    print()
    print('WARNING 级别命名空间：')
    logger_warn.debug('debug 消息 - 不显示')
    logger_warn.info('info 消息 - 不显示')
    logger_warn.warning('warning 消息 - 显示')

    print()
    print('[OK] 不同命名空间可独立控制级别')


def main():
    """主函数"""
    mode = sys.argv[1] if len(sys.argv) > 1 else 'correct'

    print('\n[TEST] nb_log 日志重复记录问题演示')
    print('=' * 50)

    if mode == 'wrong':
        demo_wrong_usage_raw_logging()
        demo_wrong_usage_loguru()
    else:
        demo_correct_usage_nb_log()
        demo_correct_module_level()
        demo_nb_log_namespace()

    print('\n' + '=' * 50)
    print('📚 总结：')
    print('=' * 50)
    print('1. 不要在函数/循环内反复创建 logger 和添加 handler')
    print('2. 使用 nb_log 可自动防止重复添加 handler')
    print('3. 理解日志命名空间是用好日志的关键')
    print('4. 参考: https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c5.html')
    print()


if __name__ == '__main__':
    main()
