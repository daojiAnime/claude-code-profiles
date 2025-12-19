#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log loguru 模式测试

测试内容：
    - 使用 loguru 风格控制台输出
    - 使用 loguru 文件 handler
    - 混合模式（nb_log + loguru）

来源：基于 ydf0509/nb_log 官方测试用例
"""

from nb_log import get_logger


def test_loguru_stream_handler():
    """测试 loguru 风格控制台输出"""
    print('\n' + '=' * 50)
    print('测试: loguru 风格控制台输出')
    print('=' * 50)

    # 使用 loguru 的 stream handler
    logger = get_logger(
        'loguru_stream',
        is_use_loguru_stream_handler=True
    )

    logger.debug('loguru 风格 DEBUG')
    logger.info('loguru 风格 INFO')
    logger.warning('loguru 风格 WARNING')
    logger.error('loguru 风格 ERROR')
    logger.critical('loguru 风格 CRITICAL')

    print('[OK] loguru 风格控制台测试完成')


def test_loguru_file_handler():
    """测试 loguru 文件 handler"""
    print('\n' + '=' * 50)
    print('测试: loguru 文件 handler (type=7)')
    print('=' * 50)

    # 使用 loguru 的文件 handler (type=7)
    logger = get_logger(
        'loguru_file',
        log_filename='loguru_file.log',
        log_file_handler_type=7,  # loguru 文件 handler
        is_add_stream_handler=True
    )

    logger.debug('写入 loguru 文件 handler')
    logger.info('loguru 文件写入测试')
    logger.error('错误日志也会写入')

    print('[OK] loguru 文件 handler 测试完成')
    print('   检查 loguru_file.log')


def test_mixed_mode():
    """测试混合模式"""
    print('\n' + '=' * 50)
    print('测试: 混合模式 (nb_log + loguru)')
    print('=' * 50)

    # loguru 控制台 + loguru 文件
    logger_loguru = get_logger(
        'mixed_loguru',
        is_use_loguru_stream_handler=True,
        log_filename='mixed_loguru.log',
        log_file_handler_type=7
    )

    # nb_log 控制台 + nb_log 文件
    logger_nb = get_logger(
        'mixed_nb',
        is_use_loguru_stream_handler=False,
        log_filename='mixed_nb.log',
        log_file_handler_type=1
    )

    print('\n[loguru 模式]:')
    logger_loguru.info('loguru 风格输出，写入 mixed_loguru.log')
    logger_loguru.error('loguru 风格错误')

    print('\n[nb_log 模式]:')
    logger_nb.info('nb_log 风格输出，写入 mixed_nb.log')
    logger_nb.error('nb_log 风格错误')

    print()
    print('[OK] 混合模式测试完成')
    print('   检查 mixed_loguru.log 和 mixed_nb.log')


def test_different_namespace_different_style():
    """测试不同命名空间使用不同风格"""
    print('\n' + '=' * 50)
    print('测试: 不同命名空间不同风格')
    print('=' * 50)

    # API 模块使用 loguru 风格
    logger_api = get_logger(
        'api',
        is_use_loguru_stream_handler=True,
        log_filename='api.log',
        log_file_handler_type=7
    )

    # 数据库模块使用 nb_log 风格
    logger_db = get_logger(
        'database',
        is_use_loguru_stream_handler=False,
        log_filename='db.log',
        log_file_handler_type=1
    )

    print('\n[API 模块 - loguru 风格]:')
    logger_api.info('API 请求处理')

    print('\n[Database 模块 - nb_log 风格]:')
    logger_db.info('数据库操作')

    print()
    print('[OK] 不同命名空间不同风格测试完成')


def run_all_tests():
    """运行所有 loguru 模式测试"""
    print('\n[TEST] nb_log loguru 模式测试')
    print('=' * 50)

    try:
        from loguru import logger as _
        print('[INFO] loguru 已安装')
    except ImportError:
        print('[WARN] loguru 未安装，部分功能可能不可用')
        print('   安装: pip install loguru')

    test_loguru_stream_handler()
    test_loguru_file_handler()
    test_mixed_mode()
    test_different_namespace_different_style()

    print('\n' + '=' * 50)
    print('[DONE] 所有 loguru 模式测试完成！')
    print('=' * 50)
    print()
    print('[TIP] nb_log 支持两种模式：')
    print('   - is_use_loguru_stream_handler=True: loguru 风格控制台')
    print('   - log_file_handler_type=7: loguru 文件 handler')


if __name__ == '__main__':
    run_all_tests()
