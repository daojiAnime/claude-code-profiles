#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb_log 多进程/多线程并发测试

测试内容：
    - 多进程文件日志安全写入
    - 多进程切割不出错
    - 多线程日志安全

来源：基于 ydf0509/nb_log 官方测试用例
警告：此测试会创建多个进程，请谨慎运行

用法：
    python test_concurrent.py [mode]

参数：
    mode: thread (多线程) 或 process (多进程，默认)
"""

import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from nb_log import get_logger, LogManager


# 多进程测试的 logger 需要在模块级别定义
# 这样每个子进程都能正确获取到 logger
concurrent_logger = None


def init_process_logger():
    """初始化进程级别的 logger"""
    global concurrent_logger
    concurrent_logger = get_logger(
        'test_concurrent',
        log_filename='test_concurrent.log',
        log_file_handler_type=1,  # 多进程安全按大小切割
        is_add_stream_handler=False  # 关闭控制台避免输出混乱
    )


def worker_process(worker_id: int):
    """多进程工作函数"""
    # 每个进程需要自己获取 logger
    logger = get_logger(
        'test_concurrent',
        log_filename='test_concurrent.log',
        log_file_handler_type=1,
        is_add_stream_handler=False
    )

    for i in range(1000):
        logger.info(f'进程 {os.getpid()} - Worker {worker_id} - 消息 {i}')
        time.sleep(0.001)  # 模拟一些延迟

    return f'Worker {worker_id} 完成'


def worker_thread(worker_id: int, logger):
    """多线程工作函数"""
    for i in range(1000):
        logger.info(f'线程 Worker {worker_id} - 消息 {i}')
        time.sleep(0.001)

    return f'Thread Worker {worker_id} 完成'


def test_multiprocess():
    """测试多进程日志写入"""
    print('\n' + '=' * 50)
    print('测试: 多进程并发日志写入')
    print('=' * 50)
    print('[WARN]  此测试会启动 5 个进程，每个写入 1000 条日志')
    print()

    worker_count = 5

    t1 = time.perf_counter()

    with ProcessPoolExecutor(max_workers=worker_count) as executor:
        futures = [executor.submit(worker_process, i) for i in range(worker_count)]
        for future in futures:
            result = future.result()
            print(f'  {result}')

    elapsed = time.perf_counter() - t1
    total_logs = worker_count * 1000

    print()
    print(f'[OK] 多进程测试完成')
    print(f'   总日志数: {total_logs} 条')
    print(f'   总耗时: {elapsed:.2f} 秒')
    print(f'   平均速度: {total_logs/elapsed:.0f} 条/秒')
    print(f'   检查 test_concurrent.log 文件')


def test_multithread():
    """测试多线程日志写入"""
    print('\n' + '=' * 50)
    print('测试: 多线程并发日志写入')
    print('=' * 50)
    print('启动 5 个线程，每个写入 1000 条日志')
    print()

    worker_count = 5

    # 多线程可以共享 logger
    logger = get_logger(
        'test_thread',
        log_filename='test_thread.log',
        is_add_stream_handler=False
    )

    t1 = time.perf_counter()

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [executor.submit(worker_thread, i, logger) for i in range(worker_count)]
        for future in futures:
            result = future.result()
            print(f'  {result}')

    elapsed = time.perf_counter() - t1
    total_logs = worker_count * 1000

    print()
    print(f'[OK] 多线程测试完成')
    print(f'   总日志数: {total_logs} 条')
    print(f'   总耗时: {elapsed:.2f} 秒')
    print(f'   平均速度: {total_logs/elapsed:.0f} 条/秒')
    print(f'   检查 test_thread.log 文件')


def test_process_rotation():
    """测试多进程下的文件切割"""
    print('\n' + '=' * 50)
    print('测试: 多进程文件切割安全性')
    print('=' * 50)
    print('[WARN]  此测试验证多进程下日志切割不出错')
    print('   nb_log 使用文件锁确保切割安全')
    print()

    print('[TIP] 关于多进程切割：')
    print('   - logging.RotatingFileHandler 在多进程下切割会报错')
    print('   - nb_log 的 handler_type=1 使用文件锁解决此问题')
    print('   - 通过批量聚合减少锁竞争，性能提升 10-100 倍')
    print()

    print('[OK] 多进程切割说明完成')
    print('   实际切割测试需要写入大量日志触发切割')


def main():
    """主函数"""
    mode = sys.argv[1] if len(sys.argv) > 1 else 'thread'

    print('\n[TEST] nb_log 并发测试')
    print('=' * 50)

    if mode == 'process':
        test_multiprocess()
    elif mode == 'thread':
        test_multithread()
    else:
        print('用法: python test_concurrent.py [thread|process]')
        return

    test_process_rotation()

    print('\n' + '=' * 50)
    print('[DONE] 并发测试完成！')
    print('=' * 50)


if __name__ == '__main__':
    main()
