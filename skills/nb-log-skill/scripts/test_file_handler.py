#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 文件日志 Handler 测试

测试内容：
    - 5种文件切割方式
    - 多进程安全切割
    - 错误日志单独写入
    - 日志文件大小和备份

来源：基于 ydf0509/nb_log 官方测试用例
"""

import time
from pathlib import Path
from nb_log import get_logger, LogManager


def test_handler_type_1():
    """测试类型1：多进程安全按大小切割（推荐）"""
    print('\n' + '=' * 50)
    print('测试 Handler 类型 1: 多进程安全按大小切割')
    print('=' * 50)

    logger = get_logger(
        'handler_type_1',
        log_filename='handler_type_1.log',
        log_file_handler_type=1,
        is_add_stream_handler=True
    )

    for i in range(10):
        logger.info(f'多进程安全按大小切割测试 - 第 {i+1} 条')

    print('[OK] Handler 类型 1 测试完成')


def test_handler_type_2():
    """测试类型2：多进程安全按时间切割"""
    print('\n' + '=' * 50)
    print('测试 Handler 类型 2: 多进程安全按时间切割')
    print('=' * 50)

    logger = get_logger(
        'handler_type_2',
        log_filename='handler_type_2.log',
        log_file_handler_type=2,
        is_add_stream_handler=True
    )

    for i in range(10):
        logger.info(f'多进程安全按时间切割测试 - 第 {i+1} 条')

    print('[OK] Handler 类型 2 测试完成')


def test_handler_type_3():
    """测试类型3：单文件永不切割"""
    print('\n' + '=' * 50)
    print('测试 Handler 类型 3: 单文件永不切割')
    print('=' * 50)

    logger = get_logger(
        'handler_type_3',
        log_filename='handler_type_3.log',
        log_file_handler_type=3,
        is_add_stream_handler=True
    )

    for i in range(10):
        logger.info(f'单文件永不切割测试 - 第 {i+1} 条')

    print('[OK] Handler 类型 3 测试完成')


def test_handler_type_6():
    """测试类型6：单进程按时间切割"""
    print('\n' + '=' * 50)
    print('测试 Handler 类型 6: 单进程按时间切割')
    print('=' * 50)

    logger = get_logger(
        'handler_type_6',
        log_filename='handler_type_6.log',
        log_file_handler_type=6,
        is_add_stream_handler=True
    )

    for i in range(10):
        logger.info(f'单进程按时间切割测试 - 第 {i+1} 条')

    print('[OK] Handler 类型 6 测试完成')


def test_error_separate_file():
    """测试错误日志单独写入"""
    print('\n' + '=' * 50)
    print('测试: 错误日志单独写入')
    print('=' * 50)

    logger = get_logger(
        'error_separate',
        log_filename='app.log',
        error_log_filename='app_error.log',
        is_add_stream_handler=True
    )

    logger.debug('DEBUG 日志 - 只写入 app.log')
    logger.info('INFO 日志 - 只写入 app.log')
    logger.warning('WARNING 日志 - 只写入 app.log')
    logger.error('ERROR 日志 - 同时写入 app.log 和 app_error.log')
    logger.critical('CRITICAL 日志 - 同时写入 app.log 和 app_error.log')

    print('[OK] 错误日志单独写入测试完成')
    print('   检查 app.log 和 app_error.log')


def test_different_files():
    """测试不同命名空间写入不同文件"""
    print('\n' + '=' * 50)
    print('测试: 不同命名空间写入不同文件')
    print('=' * 50)

    # 不同命名空间的 logger 写入不同文件
    logger_a = get_logger('module_a', log_filename='module_a.log', is_add_stream_handler=True)
    logger_b = get_logger('module_b', log_filename='module_b.log', is_add_stream_handler=True)

    logger_a.info('模块 A 的日志 - 写入 module_a.log')
    logger_b.info('模块 B 的日志 - 写入 module_b.log')

    logger_a.error('模块 A 的错误')
    logger_b.error('模块 B 的错误')

    print('[OK] 不同文件写入测试完成')
    print('   检查 module_a.log 和 module_b.log')


def test_benchmark():
    """简单性能测试"""
    print('\n' + '=' * 50)
    print('测试: 日志写入性能')
    print('=' * 50)

    logger = get_logger(
        'benchmark',
        log_filename='benchmark.log',
        is_add_stream_handler=False  # 关闭控制台输出以测试纯文件写入性能
    )

    count = 10000
    print(f'写入 {count} 条日志...')

    t1 = time.perf_counter()
    for i in range(count):
        logger.info(f'性能测试日志 {i}')
    elapsed = time.perf_counter() - t1

    print(f'[OK] 写入 {count} 条日志耗时: {elapsed:.3f} 秒')
    print(f'   平均每秒写入: {count/elapsed:.0f} 条')


def run_all_tests():
    """运行所有文件 handler 测试"""
    print('\n[TEST] nb_log 文件日志 Handler 测试')
    print('=' * 50)

    test_handler_type_1()
    test_handler_type_2()
    test_handler_type_3()
    test_handler_type_6()
    test_error_separate_file()
    test_different_files()
    test_benchmark()

    print('\n' + '=' * 50)
    print('[DONE] 所有文件 Handler 测试完成！')
    print('=' * 50)


if __name__ == '__main__':
    run_all_tests()
