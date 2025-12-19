#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 第三方包日志捕获测试

测试内容：
    - 捕获 requests/urllib3 请求日志
    - 捕获 Flask/werkzeug 日志
    - 日志命名空间树形结构
    - get_logger(None) 捕获所有日志

来源：基于 ydf0509/nb_log 官方测试用例
"""

from nb_log import get_logger


def test_capture_urllib3():
    """测试捕获 urllib3/requests 日志"""
    print('\n' + '=' * 50)
    print('测试: 捕获 requests/urllib3 日志')
    print('=' * 50)

    try:
        import requests

        # 给 urllib3 命名空间添加 handler
        # requests 底层使用 urllib3，请求日志在 urllib3 命名空间
        logger = get_logger('urllib3', log_filename='urllib3.log')

        print('发送 HTTP 请求到 baidu.com...')
        response = requests.get('http://www.baidu.com', timeout=5)
        print(f'响应状态码: {response.status_code}')

        print('[OK] urllib3 日志捕获测试完成')
        print('   检查控制台输出和 urllib3.log 文件')

    except ImportError:
        print('[WARN]  requests 未安装，跳过此测试')
        print('   安装: pip install requests')
    except Exception as e:
        print(f'[WARN]  请求失败: {e}')


def test_capture_sqlalchemy():
    """测试捕获 SQLAlchemy SQL 日志"""
    print('\n' + '=' * 50)
    print('测试: 捕获 SQLAlchemy SQL 日志')
    print('=' * 50)

    try:
        from sqlalchemy import create_engine, text

        # 给 sqlalchemy 命名空间添加 handler
        logger = get_logger('sqlalchemy.engine', log_filename='sqlalchemy.log')

        print('执行 SQLite 查询...')
        engine = create_engine('sqlite:///:memory:', echo=False)
        with engine.connect() as conn:
            result = conn.execute(text('SELECT 1 as x'))
            print(f'查询结果: {result.fetchone()}')

        print('[OK] SQLAlchemy 日志捕获测试完成')
        print('   检查控制台输出和 sqlalchemy.log 文件')

    except ImportError:
        print('[WARN]  SQLAlchemy 未安装，跳过此测试')
        print('   安装: pip install sqlalchemy')


def test_namespace_hierarchy():
    """测试日志命名空间层级结构"""
    print('\n' + '=' * 50)
    print('测试: 日志命名空间树形结构')
    print('=' * 50)

    import logging

    # 创建子命名空间的 logger
    logger_abc = logging.getLogger('a.b.c')
    logger_abc.setLevel(logging.DEBUG)

    # 给父命名空间 'a' 添加 handler
    # 这样 a.b.c 的日志也会被捕获
    logger_a = get_logger('a')

    print('日志命名空间层级: a > a.b > a.b.c')
    print('给 "a" 添加 handler 后，子命名空间的日志都会被捕获')
    print()

    # a.b.c 的日志会向上查找 handler
    logger_abc.info('来自 a.b.c 命名空间的日志')
    logger_abc.warning('a.b.c 的警告日志')

    print('[OK] 命名空间层级测试完成')


def test_capture_all_logs():
    """测试 get_logger(None) 捕获所有日志"""
    print('\n' + '=' * 50)
    print('测试: get_logger(None) 捕获所有日志')
    print('=' * 50)

    import logging

    # None 表示根命名空间，会捕获所有日志
    # 注意：生产环境不建议使用，会输出大量日志
    root_logger = get_logger(None)

    print('[WARN]  get_logger(None) 会捕获所有命名空间的日志')
    print('   仅用于调试，找出第三方包的日志命名空间')
    print()

    # 创建一些测试日志
    test_logger = logging.getLogger('some.random.namespace')
    test_logger.setLevel(logging.DEBUG)
    test_logger.info('这条日志来自 some.random.namespace')

    another_logger = logging.getLogger('another.test')
    another_logger.setLevel(logging.DEBUG)
    another_logger.warning('这条日志来自 another.test')

    print()
    print('[OK] 根命名空间捕获测试完成')
    print('   通过输出的命名空间名称，可以找到需要捕获的第三方包日志')


def test_capture_pymysql():
    """测试捕获 PyMySQL 日志"""
    print('\n' + '=' * 50)
    print('测试: 捕获 PyMySQL 日志')
    print('=' * 50)

    try:
        # 给 pymysql 命名空间添加 handler
        logger = get_logger('pymysql', log_filename='pymysql.log')

        print('[WARN]  PyMySQL 日志捕获已配置')
        print('   实际连接数据库时会记录日志')
        print('[OK] PyMySQL 日志捕获配置完成')

    except Exception as e:
        print(f'[WARN]  配置失败: {e}')


def run_all_tests():
    """运行所有第三方包日志捕获测试"""
    print('\n[TEST] nb_log 第三方包日志捕获测试')
    print('=' * 50)

    test_capture_urllib3()
    test_capture_sqlalchemy()
    test_namespace_hierarchy()
    test_capture_pymysql()

    # 最后测试根命名空间，避免影响其他测试
    # test_capture_all_logs()  # 取消注释以测试

    print('\n' + '=' * 50)
    print('[DONE] 所有第三方包日志捕获测试完成！')
    print('=' * 50)
    print()
    print('[TIP] 提示：')
    print('   - 使用 get_logger("包名") 捕获第三方包日志')
    print('   - 日志命名空间是树形结构，父命名空间可捕获子命名空间日志')
    print('   - 调试时可用 get_logger(None) 找出所有可用的命名空间')


if __name__ == '__main__':
    run_all_tests()
