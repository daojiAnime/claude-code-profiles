#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 基础功能测试

测试内容：
    - 基本日志输出（各级别）
    - 彩色控制台输出
    - 文件日志写入
    - 日志命名空间

来源：基于 ydf0509/nb_log 官方测试用例
"""

from nb_log import get_logger


def test_basic_logging():
    """测试基本日志输出"""
    print('\n' + '=' * 50)
    print('测试 1: 基本日志输出')
    print('=' * 50)

    logger = get_logger('test_basic')

    logger.debug('这是 DEBUG 级别 - 绿色背景')
    logger.info('这是 INFO 级别 - 天蓝色背景')
    logger.warning('这是 WARNING 级别 - 黄色背景')
    logger.error('这是 ERROR 级别 - 粉红色背景')
    logger.critical('这是 CRITICAL 级别 - 血红色背景')

    print('[OK] 基本日志测试完成')


def test_file_logging():
    """测试文件日志写入"""
    print('\n' + '=' * 50)
    print('测试 2: 文件日志写入')
    print('=' * 50)

    logger = get_logger(
        'test_file',
        log_filename='test_file.log',
        is_add_stream_handler=True
    )

    logger.info('这条日志会同时出现在控制台和文件中')
    logger.error('错误日志也会写入文件')

    print('[OK] 文件日志测试完成，检查 test_file.log')


def test_namespace():
    """测试日志命名空间"""
    print('\n' + '=' * 50)
    print('测试 3: 日志命名空间')
    print('=' * 50)

    # 不同命名空间的 logger
    logger_a = get_logger('namespace_a')
    logger_b = get_logger('namespace_b')

    # 验证是不同的 logger 对象
    print(f'logger_a id: {id(logger_a)}')
    print(f'logger_b id: {id(logger_b)}')

    # 相同命名空间返回相同对象
    logger_a2 = get_logger('namespace_a')
    print(f'logger_a2 id: {id(logger_a2)} (应与 logger_a 相同)')

    logger_a.info('来自命名空间 A 的日志')
    logger_b.info('来自命名空间 B 的日志')

    assert id(logger_a) == id(logger_a2), '相同命名空间应返回相同 logger'
    assert id(logger_a) != id(logger_b), '不同命名空间应返回不同 logger'

    print('[OK] 命名空间测试完成')


def test_different_levels():
    """测试不同级别的日志过滤"""
    print('\n' + '=' * 50)
    print('测试 4: 日志级别过滤')
    print('=' * 50)

    import logging

    # DEBUG 级别 logger - 显示所有日志
    logger_debug = get_logger('level_debug', log_level_int=logging.DEBUG)

    # WARNING 级别 logger - 只显示 WARNING 及以上
    logger_warn = get_logger('level_warn', log_level_int=logging.WARNING)

    print('\nDEBUG 级别 logger (应显示 5 条):')
    logger_debug.debug('DEBUG 消息')
    logger_debug.info('INFO 消息')
    logger_debug.warning('WARNING 消息')
    logger_debug.error('ERROR 消息')
    logger_debug.critical('CRITICAL 消息')

    print('\nWARNING 级别 logger (应只显示 3 条):')
    logger_warn.debug('DEBUG 消息 - 不应显示')
    logger_warn.info('INFO 消息 - 不应显示')
    logger_warn.warning('WARNING 消息')
    logger_warn.error('ERROR 消息')
    logger_warn.critical('CRITICAL 消息')

    print('[OK] 日志级别测试完成')


def test_exception_logging():
    """测试异常日志"""
    print('\n' + '=' * 50)
    print('测试 5: 异常堆栈记录')
    print('=' * 50)

    logger = get_logger('test_exception')

    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception('捕获到除零错误，以下是堆栈信息：')

    print('[OK] 异常日志测试完成')


def run_all_tests():
    """运行所有测试"""
    print('\n[TEST] nb_log 基础功能测试')
    print('=' * 50)

    test_basic_logging()
    test_file_logging()
    test_namespace()
    test_different_levels()
    test_exception_logging()

    print('\n' + '=' * 50)
    print('[DONE] 所有基础测试完成！')
    print('=' * 50)


if __name__ == '__main__':
    run_all_tests()
