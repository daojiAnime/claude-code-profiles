#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 诊断工具

用途：
    诊断日志配置问题，检测常见错误：
    - 重复 handler 导致日志多次记录
    - 日志级别设置不当
    - 配置文件问题
    - 第三方包日志捕获

用法：
    python diagnose.py [logger_name]

示例：
    python diagnose.py                # 诊断所有 logger
    python diagnose.py myapp          # 诊断指定 logger
"""

import logging
import sys
from typing import Optional


def print_header(title: str):
    """打印分隔标题"""
    print()
    print('=' * 60)
    print(f' {title}')
    print('=' * 60)


def print_ok(msg: str):
    """打印成功信息"""
    print(f'  [OK] {msg}')


def print_warn(msg: str):
    """打印警告信息"""
    print(f'  [WARN] {msg}')


def print_error(msg: str):
    """打印错误信息"""
    print(f'  [ERROR] {msg}')


def print_info(msg: str):
    """打印信息"""
    print(f'  [INFO] {msg}')


def check_nb_log_installed() -> bool:
    """检查 nb_log 是否安装"""
    print_header('检查 nb_log 安装')
    try:
        import nb_log
        version = getattr(nb_log, '__version__', '未知')
        print_ok(f'nb_log 已安装，版本: {version}')
        return True
    except ImportError:
        print_error('nb_log 未安装，请运行: pip install nb_log')
        return False


def check_config_file() -> bool:
    """检查配置文件"""
    print_header('检查配置文件')

    try:
        import nb_log_config
        config_path = nb_log_config.__file__
        print_ok(f'找到配置文件: {config_path}')

        # 检查关键配置
        log_path = getattr(nb_log_config, 'LOG_PATH', None)
        if log_path:
            print_info(f'日志路径: {log_path}')
        else:
            print_warn('未设置 LOG_PATH')

        handler_type = getattr(nb_log_config, 'LOG_FILE_HANDLER_TYPE', 1)
        print_info(f'文件 handler 类型: {handler_type}')

        return True
    except ImportError:
        print_warn('未找到 nb_log_config.py 配置文件')
        print_info('首次使用 nb_log 时会自动生成')
        print_info('或运行: python init_config.py 手动生成')
        return True


def check_logger_handlers(logger_name: Optional[str] = None):
    """检查 logger 的 handler 配置"""
    print_header('检查 Logger Handlers')

    if logger_name:
        loggers_to_check = {logger_name: logging.getLogger(logger_name)}
    else:
        # 获取所有已注册的 logger
        loggers_to_check = dict(logging.Logger.manager.loggerDict)

    if not loggers_to_check:
        print_info('暂无已注册的 logger')
        return

    issues_found = False

    for name, logger_ref in loggers_to_check.items():
        # 跳过 PlaceHolder
        if not isinstance(logger_ref, logging.Logger):
            continue

        logger = logging.getLogger(name)
        handlers = logger.handlers

        print(f'\n  [Logger] "{name}"')
        print(f'     级别: {logging.getLevelName(logger.level)}')
        print(f'     Handlers 数量: {len(handlers)}')

        # 检查重复 handler
        handler_types = {}
        for h in handlers:
            h_type = type(h).__name__
            handler_types[h_type] = handler_types.get(h_type, 0) + 1

        for h_type, count in handler_types.items():
            if count > 1:
                print_warn(f'检测到 {count} 个 {h_type}，可能导致日志重复记录！')
                issues_found = True
            else:
                print_info(f'{h_type}: {count} 个')

    if not issues_found:
        print()
        print_ok('未发现 handler 重复问题')


def check_duplicate_logging():
    """演示和检测日志重复记录问题"""
    print_header('日志重复记录检测')

    print_info('常见的日志重复原因：')
    print('     1. 在循环或函数内反复调用 get_logger() 或 addHandler()')
    print('     2. 多个模块对同一命名空间添加 handler')
    print('     3. 使用 loguru 时反复调用 logger.add()')
    print()
    print_info('解决方案：')
    print('     - 使用 nb_log 时，get_logger() 会自动防止重复添加 handler')
    print('     - 将 logger 实例化放在模块级别，而非函数内部')
    print('     - 参考文档：https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c5.html')


def check_third_party_loggers():
    """检查第三方包的日志配置"""
    print_header('第三方包日志检测')

    common_loggers = [
        ('urllib3', 'requests 底层库，记录 HTTP 请求'),
        ('werkzeug', 'Flask WSGI 服务器，记录请求 URL'),
        ('sqlalchemy', 'SQL ORM，记录 SQL 语句'),
        ('celery', 'Celery 任务队列'),
        ('paramiko', 'SSH 连接库'),
        ('elasticsearch', 'ES 客户端'),
        ('kafka', 'Kafka 客户端'),
    ]

    print_info('常用第三方包日志命名空间：')
    for name, desc in common_loggers:
        logger = logging.getLogger(name)
        handler_count = len(logger.handlers)
        status = '[Y]' if handler_count > 0 else '[N]'
        print(f'     {status} {name}: {desc}')

    print()
    print_info('捕获第三方包日志示例：')
    print('     from nb_log import get_logger')
    print("     get_logger('urllib3')  # 捕获 requests 请求日志")
    print("     get_logger('werkzeug', log_filename='flask.log')  # 捕获 Flask 日志")


def run_diagnostics(logger_name: Optional[str] = None):
    """运行所有诊断"""
    print()
    print('nb_log 诊断工具')
    print('=' * 60)

    # 检查安装
    if not check_nb_log_installed():
        return

    # 检查配置文件
    check_config_file()

    # 检查 handler
    check_logger_handlers(logger_name)

    # 检查重复记录
    check_duplicate_logging()

    # 检查第三方包
    check_third_party_loggers()

    print()
    print('=' * 60)
    print(' 诊断完成')
    print('=' * 60)
    print()


def main():
    """主函数"""
    logger_name = sys.argv[1] if len(sys.argv) > 1 else None
    run_diagnostics(logger_name)


if __name__ == '__main__':
    main()
