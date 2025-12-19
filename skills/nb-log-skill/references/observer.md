# Nb-Log-Skills - Observer

**Pages:** 2

---

## 4.关于logging包日志观察者模式

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c4.html

**Contents:**
- 4.关于logging包日志观察者模式
- 观察者模式图片

不会扩展日志记录到什么地方，主要是不懂什么叫观察者模式

菜鸟教程的观察者模式demo连接 观察者模式demo

这个uml图上分为Subject 和 基类Observer，以及各种继承或者实现Observer的XxObserver类， 其中每个不同的Observer需要实现doOperation方法。

如果对应到python内置的logging日志包的实现，那么关系就是：

loging.Handler类是uml图的Observer类

StreamHandler FileHandler DingTalkHandler 是uml图的各种XxObservers类。

StreamHandler FileHandler DingTalkHandler类的 emit方法是uml图的doOperation方法

只有先学设计模式，才能知道经典固定套路达到快速看代码，能够达到秒懂源码是怎么规划设计实现的。

如果不先学习经典设计模式，每次看包的源码，需要多浪费很多时间看他怎么设计实现的，不懂设计模式，会觉得太难了看着就放弃了。

在python日志的理解和使用上，国内能和我打成平手的没有几人。

**Examples:**

Example 1 (python):
```python
# 例如 日志想实现记录到 控制台、文件、钉钉群、redis、mongo、es、kafka、发邮件其中的几种的任意组合。
# low的人，会这么写，以下是伪代码，实现记录到控制台、文件、钉钉群这三种的任意几种组合。

def 记录到控制台(msg):
    """实现把msg记录到控制台"""


def 记录到文件(msg):
    """实现把msg记录到文件"""


def 记录到钉钉(msg):
    """实现把msg记录到钉钉"""


def 记录到控制台和文件(msg):
    """实现把msg记录到控制台和文件"""


def 记录到控制台和钉钉(msg):
    """实现把msg记录到控制台和钉钉"""


def 记录到文件和钉钉(msg):
    """实现把msg记录到文件和钉钉"""


def 记录到控制台和文件和钉钉(msg):
    """实现把msg记录到控制台和文件和钉钉"""


# 当需要把msg记录到文件时候，调用函数 记录到文件(msg)
# 当需要把msg记录到控制台时候，调用函数 记录到控制台(msg)
# 当需要把msg记录到钉钉时候，调用函数 记录到钉钉(msg)
# 当需要把msg记录到控制台和文件，调用函数 记录到控制台和文件(msg)
# 当需要把msg记录到控制台和钉钉，调用函数 记录到控制台和钉钉(msg)
# 当需要把msg记录到控制台和文件和钉钉，调用函数 记录到控制台和文件和钉钉(msg)

"""
这样会造成，仅记录到控制台 文件 钉钉这三种的任意几个，需要写6个函数，调用时候需要调用不同的函数名。
但是现在日志可以记录到8种地方，如果还这么low的写法，需要写8的阶乘个函数，调用时候根据场景需要会调用8的阶乘个函数名。
8的阶乘结果是 40320 ，如果很low不学设计模式做到灵活组合，需要多写 4万多个函数，不学设计模式会多么吓人。

"""
```

---

## 5.演示不懂观察者模式，日志重复记录惨烈的例子

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c5.html

**Contents:**
- 5.演示不懂观察者模式，日志重复记录惨烈的例子
- 5.1 演示一个由于不好好理解观察者模式，封装的日志类在调用时候十分惨烈的例子，惨烈程度达到10级。
- 5.2 使用博客园搜索后排名第一个的python 日志封装，也是严重重复记录。
- 5.3 使用火热的loguru 来演示惨烈的文件日志重复记录。

这个例子是为了记录10万次日志到控制台和文件，就算python性能很差，就这个例子而言，预期耗时肯定是需要10秒以内才算合格。

看起来10秒内可以运行完成，实际上1周内能运行结束这个代码，我愿意吃10斤翔。

**Examples:**

Example 1 (python):
```python
"""
演示重复，由于封装错误的类造成的。模拟一个封装严重失误错误的封装例子。

看起来10秒内可以运行完成，实际上1周内能运行结束这个代码，我愿意吃10斤翔。

这个代码惨烈程度达到10级。明明是想记录10000次日志，结果却记录了 10000 * 10001 /2 次。
如果把f函数调用100万次，那么控制台和文件将会各记录5000亿次，日志会把代码拖累死。
不好好理解观察者模式有多惨烈。因为反复添加观察者（handler）,
导致第1次调用记录1次，第二次调用时候记录2次，第10次调用时候记录10次，这成了高斯求和算法了。

这种类似的封装造成的后果可想而知，长期部署运行后，不仅项目代码性能几乎被日志占了99%，还造成磁盘被弄爆炸。
"""
import logging
import time


class LogUtil:
    def __init__(self):
        self.logger = logging.getLogger('a')
        self.logger.setLevel(logging.DEBUG)
        self._add_stream_handler()
        self._add_file_handler()

    def _add_stream_handler(self):
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
        self.logger.addHandler(sh)

    def _add_file_handler(self):
        fh = logging.FileHandler('a.log')
        fh.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
        self.logger.addHandler(fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)


def f(x):
    log = LogUtil()  # 重点是这行，写在了函数内部。既没有做日志命名空间的handlers判断控制，封装的类本身也没写单利或者享元模式。
    log.debug(x)


t1 = time.time()
for i in range(100000):
    f(i)

print(time.time() - t1)
```

Example 2 (python):
```python
import logging


class Log(object):
    def __init__(self, name=__name__, path='mylog.log', level='DEBUG'):
        self.__name = name
        self.__path = path
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger


if __name__ == '__main__':
    def f():
        log = Log(__name__, 'file.log')
        logger = log.Logger
        # logger.debug('I am a debug message')
        # logger.info('I am a info message')
        # logger.warning('I am a warning message')
        # logger.error('I am a error message')
        logger.critical('I am a critical message')


    for i in range(10):
        f()
```

Example 3 (unknown):
```unknown
运行上面这个代码，应为调用了f函数10次，应该是一共打印10次和写入文件10次，结果是打印55次，写入文件55次。
因为这个实例化写在了函数内部，造成每调用一次就新增一次handler，日志记录的总次数不是预期期待的变成了高斯求和。
这种日志封装很惨，如果部署线上，f函数调用了10万次，那么会造成重复记录  100000*100001/2次变成50亿次，
随着程序部署的时间越来越长，服务器cpu会越来越卡，磁盘增长也会越来越快，而且问题难以排查，造成事故会非常惨烈。


千万别说你会注意，只会把Log封装类实例化放在函数的外面，这样做没用的，一个项目几百个模块，
如果在很多个模块级下面都实例化相同命名空间的日志，然后使用run.py调用了几百个模块作为运行起点，一样会造成重复打印。
所以只是小心翼翼的吧日志类的实例化放在模块级下面，仍然会发生重复记录的可能，只不过没有for循环那么惨烈的高斯求和叠加出记录那么多。
但是使用nb_log就可以随便你怎么折腾，放在for循环下面无限实例化都不怕不会重复记录日志。
```

Example 4 (python):
```python
"""
这也是一个很惨烈的真实例子。使用大火的 loguru ，然来用户让来本意是想实现每天生成一个新的日志文件。
结果造成了在所有历史文件中都重复记录当前日志，随着部署的天数越来越长，长时间例如半年 八九个月 如果不重新部署程序，
会造成严重的磁盘紧张和cpu飙升。
"""

from loguru import logger
import time


def f(x):
    """
     用户实际生产是想每一天生成一个日志， time.strftime("%Y-%m-%d")}.log，
     但这里为了节约时间方便演示文件日志重复记录所以换成时分秒演示，不然的话要观察很长的时间每隔一天观察一次才能观察出来。
    """
    logger.add(f'test_{time.strftime("%H-%M-%S")}.log')
    logger.debug(f'loguru 太惨了重复记录 {x}')
    logger.info(f'loguru 太惨了重复记录 {x}')
    logger.warning(f'loguru 太惨了重复记录 {x}')
    logger.error(f'loguru 太惨了重复记录 {x}')
    logger.critical(f'loguru 太惨了重复记录 {x}')


for i in range(100):
    time.sleep(1)
    f(i)

"""
预期是每秒调用一次函数f，但函数里面面有5次记录，debug info warning error  critical，
所以预期是每秒有5条日志只写入当前最新的日志文件中，但结果是每秒都写入到历史所有日志文件中。
只看当前最新的那个日志文件，似乎没有看到重复记录，但如果看所有的历史旧日志文件可以看到每个旧文件都严重重复记录了。
这种问题很难排查，所以用日志要谨慎，要搞懂日志handlers，和设计模式的观察者模式才能用好日志。
"""
```

---
