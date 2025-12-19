---
name: nb-log-skill
description: Python nb_log 日志库官方文档，配置高性能日志记录，包括多handler支持、彩色控制台、日志文件切割等
---

# nb_log Skill

高性能 Python 日志库 nb_log 完整使用指南。

## When to Use

- 配置 Python 项目日志系统
- 实现彩色控制台日志输出
- 配置多进程安全的文件日志切割
- 将日志发送到钉钉、MongoDB、Elasticsearch、Kafka、邮件等
- 捕获第三方包的日志
- 解决日志重复记录问题

## Quick Reference

### 安装

```bash
pip install nb_log
```

### 基本用法

```python
from nb_log import get_logger

logger = get_logger('my_app')

logger.debug('调试信息 - 绿色')
logger.info('普通信息 - 天蓝色')
logger.warning('警告信息 - 黄色')
logger.error('错误信息 - 粉红色')
logger.critical('严重错误 - 血红色')
```

### 写入文件

```python
from nb_log import get_logger

logger = get_logger('my_app',
                    log_filename='app.log',
                    error_log_filename='error.log')
```

### get_logger 核心参数

| 参数 | 类型 | 说明 |
|-----|------|-----|
| `name` | str | 必填，日志命名空间 |
| `log_level_int` | int | 日志级别 (10=DEBUG, 20=INFO, 30=WARNING, 40=ERROR) |
| `is_add_stream_handler` | bool | 是否输出到控制台 |
| `log_filename` | str | 日志文件名，设置后才写入文件 |
| `log_path` | str | 日志文件夹路径 |
| `error_log_filename` | str | 错误日志单独写入的文件名 |
| `log_file_handler_type` | int | 文件切割类型 (1-7) |
| `formatter_template` | int | 日志格式模板 (1-7) |

### 文件切割类型 (log_file_handler_type)

| 值 | 说明 |
|----|-----|
| 1 | 多进程安全按大小切割（默认，推荐） |
| 2 | 多进程安全按时间切割 |
| 3 | 单文件永不切割 |
| 4 | WatchedFileHandler |
| 5 | 单进程按大小切割 |
| 6 | 单进程按时间切割 |
| 7 | 使用 loguru 的文件 handler |

### 第三方服务集成

```python
from nb_log import get_logger

# 钉钉通知
logger = get_logger('app', ding_talk_token='your_token')

# MongoDB
logger = get_logger('app', mongo_url='mongodb://localhost:27017')

# Elasticsearch
logger = get_logger('app', is_add_elastic_handler=True)

# Kafka
logger = get_logger('app', is_add_kafka_handler=True)

# 邮件通知
logger = get_logger('app', is_add_mail_handler=True, mail_handler_config={...})
```

### 捕获第三方包日志

```python
from nb_log import get_logger
import requests

# 捕获 urllib3 的请求日志
get_logger('urllib3')
requests.get("http://www.baidu.com")

# 捕获 Flask/werkzeug 请求日志
get_logger('werkzeug', log_filename='flask.log')

# 捕获所有日志（调试用）
get_logger(None)
```

### 配置文件

首次运行时自动生成 `nb_log_config.py`：

```python
LOG_PATH = '/var/log/myapp/'
LOG_FILE_HANDLER_TYPE = 1
FORMATTER_KIND = 5
LOG_FILE_SIZE = 100
LOG_FILE_BACKUP_COUNT = 5
```

## Scripts

| 脚本 | 用途 |
|-----|-----|
| init_config.py | 生成 nb_log_config.py 配置模板 |
| diagnose.py | 诊断日志配置问题 |
| test_basic.py | 基础功能测试 |
| test_file_handler.py | 文件 handler 测试 |
| test_third_party.py | 第三方包日志捕获测试 |
| test_concurrent.py | 多进程/多线程并发测试 |
| test_duplicate.py | 日志重复记录问题演示 |

## Reference Files

| 文件 | 内容 |
|-----|-----|
| introduction.md | 安装、基本用法、与 logging/loguru 对比 |
| file_logging.md | 5种文件切割方式、多进程安全、性能对比 |
| integrations.md | 钉钉、MongoDB、ES、Kafka、邮件配置 |
| observer.md | 观察者模式原理、避免日志重复 |
| troubleshooting.md | FAQ、日志级别控制、pyinstaller打包 |
| advanced.md | 封装注意事项、最佳实践 |

## nb_log vs loguru

| 特性 | nb_log | loguru |
|-----|--------|--------|
| 控制台彩色 | 背景色+前景色 | 前景色 |
| 文件日志性能 | 快400% | 较慢 |
| 多进程切割 | 安全 | 会报错 |
| 命名空间 | 完善 | 无 |
| 第三方包兼容 | 原生 logging.Logger | 独立实现 |
| 内置 handler | 10+ 种 | 较少 |

## Notes

- nb_log 基于 Python 原生 logging 封装，返回标准 logging.Logger 对象
- 日志命名空间是核心概念
- 多进程场景建议使用 log_file_handler_type=1
- 不建议对 nb_log 进行二次封装

## Resources

- 官方文档: https://nb-log-doc.readthedocs.io/zh-cn/latest/
- PyPI: https://pypi.org/project/nb-log/
- GitHub: https://github.com/ydf0509/nb_log
