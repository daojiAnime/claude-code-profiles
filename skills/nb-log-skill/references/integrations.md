# Nb-Log-Skills - Integrations

**Pages:** 1

---

## 3. nb_log记录到 钉钉、Mongo、elastic、邮件等

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c3.html

**Contents:**
- 3. nb_log记录到 钉钉、Mongo、elastic、邮件等
- 3.1 钉钉日志
- 3.2 其他handler包括kafka日志，elastic日志，邮件日志，mongodb日志
- 3.3 各種日志截圖

nb_log 内置支持将日志同时记录到多种目标位置，包括控制台、文件、钉钉群、MongoDB、Elasticsearch、Kafka、邮件等。
通过 `get_logger` 函数的入参设置即可实现"一参傻瓜式"配置。

### 第三方服务相关参数

| 参数名 | 类型 | 用途说明 |
|-------|------|---------|
| `ding_talk_token` | str | 钉钉机器人 webhook token |
| `ding_talk_time_interval` | int | 钉钉消息发送时间间隔（秒），避免消息过于频繁 |
| `mongo_url` | str | MongoDB 连接字符串，如 `mongodb://localhost:27017` |
| `is_add_elastic_handler` | bool | 是否记录到 Elasticsearch |
| `is_add_kafka_handler` | bool | 是否发送到 Kafka |
| `mail_handler_config` | dict | 邮件配置字典 |
| `is_add_mail_handler` | bool | 是否发送邮件通知 |

### 配置文件设置

在 `nb_log_config.py` 中可以配置默认的第三方服务参数：

```python
# MongoDB 配置
MONGO_URL = 'mongodb://localhost:27017'

# Elasticsearch 配置
ELASTIC_HOST = '127.0.0.1'
ELASTIC_PORT = 9200

# Kafka 配置
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'nb_log'

# 邮件配置
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_TO_ADDRS = ['recipient@example.com']
```

**Examples:**

Example 1 - 钉钉日志 (python):
```python
from nb_log import get_logger

# 同时输出到控制台、文件、钉钉群
logger = get_logger("hi",
                    is_add_stream_handler=True,
                    log_filename="hi.log",
                    ding_talk_token='your_dingding_token')
logger.debug('这条日志会同时出现在控制台、文件和钉钉群消息')
logger.error('错误日志会发送到钉钉提醒')
```

Example 2 - MongoDB 日志 (python):
```python
from nb_log import get_logger

# 记录日志到 MongoDB
logger = get_logger("mongo_logger",
                    is_add_stream_handler=True,
                    mongo_url='mongodb://localhost:27017')
logger.info('这条日志会写入 MongoDB')
```

Example 3 - Elasticsearch 日志 (python):
```python
from nb_log import get_logger

# 记录日志到 Elasticsearch
logger = get_logger("es_logger",
                    is_add_stream_handler=True,
                    is_add_elastic_handler=True)
logger.info('这条日志会写入 Elasticsearch')
```

Example 4 - Kafka 日志 (python):
```python
from nb_log import get_logger

# 记录日志到 Kafka
logger = get_logger("kafka_logger",
                    is_add_stream_handler=True,
                    is_add_kafka_handler=True)
logger.info('这条日志会发送到 Kafka')
```

Example 5 - 邮件日志 (python):
```python
from nb_log import get_logger

# 记录错误日志并发送邮件
mail_config = {
    'mailhost': ('smtp.example.com', 465),
    'fromaddr': 'sender@example.com',
    'toaddrs': ['recipient@example.com'],
    'subject': '程序错误报警',
    'credentials': ('sender@example.com', 'password'),
    'secure': ()
}

logger = get_logger("mail_logger",
                    is_add_stream_handler=True,
                    is_add_mail_handler=True,
                    mail_handler_config=mail_config)
logger.error('这条错误日志会发送邮件通知')
```

Example 6 - 组合多种输出 (python):
```python
from nb_log import get_logger

# 同时输出到：控制台 + 文件 + 钉钉 + MongoDB
logger = get_logger("multi_output",
                    is_add_stream_handler=True,
                    log_filename="app.log",
                    ding_talk_token='your_token',
                    mongo_url='mongodb://localhost:27017')

logger.info('这条日志会同时记录到4个地方')
logger.error('错误日志会触发钉钉提醒')
```

---
