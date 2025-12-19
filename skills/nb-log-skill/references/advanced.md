# Nb-Log-Skills - Advanced

**Pages:** 1

---

## 8 禁止对nb_log进行二次封装

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c8.html

**Contents:**
- 8 禁止对nb_log进行二次封装
- 8.1 禁止对nb_log进行以下形式的封装
  - 8.1b 如果非要封装nb_log,为了保证获取的代码文件和行号是正确的，
- 8.2 其他废物封装举例子

不要偷梁换柱，把logger对象换成别的类。nb_log没有发明新的类型，get_logger是返回经典日志类型 logging.Logger， 如果你非要对nb_log封装，那应该返回 logging.Logger 类型，不要用其他类型的对象 .debug() 来记录日志， 要使用 logging.Logger 类型的对象 .debug() 来记录日志。

有的人闲的蛋疼，非要装逼写个废物类，这样封装个废物类有什么必要性了?

nb_log.get_logger() 得到的是内置logging.Logger对象，兼容性无敌了，还能点击精确跳转到发生日志的文件和行号。 用户这样封装那有什么卵用了，增加了什么新功能了吗？ 用户的 LogUtil() 得到的logger对象能 logger.setLevel(logging.WARN) 这样吗，一下子就报错了，因为不是经典日志类型。

用户封装nb_log后，把get_logger的入参全部屏蔽了，无法使用多命名空间，无法自定义不同的日志表现行为和记录到的地方，简直封装了个废物，越封装越差。 写类不是为了装逼，对nb_log和任意三方包能不封装就别封装。

生成logger时候要指定 logger_cls=nb_log.CompatibleLogger , (因为python3.9以下logging不支持设置日志位置的堆栈级别 stacklevel 入参)

并在你的debug方法调用原生logger对象的debug方法时候，加上 extra = {"sys_getframe_n": 3}

包括之前举的例子，封装redis mysql的,有的人这样封装

三方Redis类不好吗，非要封装几千个方法，写几万行代码才开心。 这种封装自定义的 def my_xx() : 方法里面去调用 三方包核心对象.xx()的封装没有什么用，快别封装了。

**Examples:**

Example 1 (unknown):
```unknown
禁止使用此种错误方式来封装 nb_log ，因为点击控制台跳转到的日志地方跳转到你的这个类了，而不是精确跳转到 logger.debug/info()  的地方
并且日志的name 千万不要固定死了，多命名空间才是日志精髓。
所有日志只能写入到mylog.log文件中，不能写入不同的文件,不能给每个日志设置不同的级别，不能自定义日志记录到控制台 文件 mongo中的哪些地方。
```

Example 2 (python):
```python
import nb_log


class LogUtil:
    def __init__(self):
        self.logger = nb_log.get_logger('xx',log_filename='mylog.log')

    def debug(self,msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    print('日志命名固定死了，没有多实例单独控制很差劲。所有日志只能写入到mylog.log文件中，不能写入不同的文件')
    logger = LogUtil()
    logger.debug('点击控制台不能跳转到本行，跳转到工具类去了')
    logger.info('点击控制台不能跳转到本行，跳转到工具类去了')
    logger.warning('点击控制台不能跳转到本行，跳转到工具类去了')
    logger.error('点击控制台不能跳转到本行，跳转到工具类去了')
    logger.critical('点击控制台不能跳转到本行，跳转到工具类去了')
```

Example 3 (python):
```python
import nb_log
logger = nb_log.LogManager('my_logger', logger_cls=nb_log.CompatibleLogger).get_logger_and_add_handlers(log_filename='my_logger.log')

def debug(msg)
    logger.debug(msg, extra = {"sys_getframe_n": 3})
```

Example 4 (python):
```python
from redis import Redis

class MyRedis:
    def __init__(self):
        self.r = Redis()
        
    def my_set(self,k,v):
        self.r.set(k.v)
        
    def my_get(self,k):
        self.r.get(k)
        
    def my_delete(self,k):
        self.r.delete(k)
        
    
    def my_hget(self,name,key):
        self.r.hget(name,key)
    
        
        
    """ 继续废物封装几百个redis方法"""
```

---
