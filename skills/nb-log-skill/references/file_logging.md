# Nb-Log-Skills - File Logging

**Pages:** 3

---

## 7 nb_log 捕获三方包的日志

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c7.html

**Contents:**
- 7 nb_log 捕获三方包的日志
- 7.1 nb_log 记录三方包日志的方法，requests举例子
- 7.2 nb_log还可以记录flask/django任意三方包
- 7.3 python日志命名空间是树形结构
- 7.4 如何确定有哪些日志命名空间的日志可以被记录，强大的 get_logger(None)

准确来说不是捕获，是给三方包的logger加上handlers，三方包的logger没有观察者例如 streamHandler fileHanlder等，不会自动打印控制台和记录文件啥的。

一般三方包的每个模块都会写 logger = logging.getLogger(name)，很多人非常之蒙蔽对这句话。

这个是创建了当前 包名.文件夹名.模块名 的日志命名空间,但没有创建handler，所以里面 logger.info() 是不会被记录到的。

只有对这个命名空间的logger加上handlers后才会记录到各种地方。

有的人要记录请求了什么，状态是什么，非要自己亲自写日志，那其实urllib3对每个请求和状态码都记录了， 并不需要用户去亲自再重复写logger.info("请求了什么url 耗时多少 状态码是什么")，这些都是多此一举，主要是用户不懂日志命名空间。 如上图，get_logger 对 urllib3 命名空间的日志加上了控制台handler后就会自动记录到请求了什么url和响应情况了，完全不需要用户修复写代码。

requests包会调用urllib3,urllib3包里面记录了日志请求什么了，所以上面是 get_logger('urllib3') 而不是 get_logger('requests'), 一般情况下 get_logger(name=三方包名就可以了)

例如 get_logger(name="werkzeug",log_file_name='myfile.log') ,就会记录到请求flask服务端url的日志到控制台和myfile.log了。

一般情况下 get_logger(name=三方包名就可以了)，get_logger(name='flask') 就可以记录到前端请求的是什么url了， 但是flask是一个基于Python开发并且依赖jinja2模板和Werkzeug WSGI服务的一个微型框架,对于Werkzeug本质是Socket服务端, 其用于接收http请求并对请求进行预处理，所以 get_logger(name="werkzeug") 用于捕获日志，因为记录请求url的是在 werkzeug 包下面写的， 所以命名空间是 werkzeug.xx.yy 。

如果代码中不写 get_logger(name="werkzeug")

假设三方包名是 thp，三方包根目录里面有 xx.py 和 yy.py，并且每个python文件是 logger = logging.getLogger(name) 的， 你如果想捕获thp包所有日志， get_logger('thp') 就好了。

如果你只想捕获 xx.py的debug以上日志， 捕获yy.py的error以上日志，那么应该写 get_logger('thp.xx',log_level_int=10) # 10就是 logging.DEBUG常量。 get_logger('thp.yy',log_level_int=40) # 40就是 logging.ERROR常量。

python的日志命名空间是树形的，用 . 隔开。

假设 日志命名空间是 a.b.c, 那么 a 和a.b 和 a.b.c 都可以捕获 a.b.c 命名空间日志。

例如这个例子，第27行并不会被打印，但是第31行可以打印出来日志。因为a命名空间是a.b.c的父命名空间，a.b.c会先查找 a.b.c，再查找 a.b，再查找a，再查找根命名空间,一直向上查找。

根命名空间是所有一切命名空间的父命名空间。

2） 当name传 None时候意思是根命名空间加上handlers了。根命名空间是无敌的，会捕获所有三方包的日志，如果你不想捕获所有包的日志就别这么用。

get_logger(None) 就可以给根命名空间机上handler了，然后控制台的日志会显示每个日志的命名空间，你把对你有作用的命名空间记录下来，没有作用的干扰日志就不需要记住那些命名空间了。

例如 flask我咋知道是 get_logger(name="werkzeug") 可以使用werkzeug来捕获请求url记录的？这个单词werkzeug太难拼写了，背诵不下来咋办， 那就是简单粗暴的 get_logger(None) 就可以了，然后前端请求url时候，你看到控制台日志会显示 werkzeug 命名空间了， 然后你再把get_logger(None) 换成 get_logger(name="werkzeug") 就好了。

requests请求时候，我咋知道是get_logger('urllib3') 而不是 get_logger('requests')来捕获请求url的地址和状态码，是一个道理。

线上不建议 get_logger(None) 这样做，这样项目三方包太多了，记录不关心的日志了。 希望用户传入精确的日志命名空间，给不同命名空间设置不同的日志级别和添加不同的handlers。

**Examples:**

Example 1 (python):
```python
from nb_log import get_logger
import requests

get_logger('urllib3')  # 也可以更精确只捕获 urllib3.connectionpool 的日志，不要urllib3包其他模块文件的日志
requests.get("http://www.baidu.com")
```

---

## 2 nb_log的文件日志handler

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c2.html

**Contents:**
- 2 nb_log的文件日志handler
- 2.1 nb_log 支持5中文件日志切割方式
- 2.2 演示nb_log文件日志，并且直接演示最高实现难度的多进程安全切片文件日志
- 2.3 演示文件大小切割在多进程下的错误例子,

这个文件日志的自定义多进程安全按大小切割，filehandler是python史上性能最强大的支持多进程下日志文件按大小自动切割。

关于按大小切割的性能可以看第10章的和loggeru的性能对比，nb_log文件日志写入性能快400%。

nb_log 支持5种文件日志，get_logger 的log_file_handler_type可以优先设置是按照 大小/时间/watchfilehandler/单文件永不切割.

也可以在你代码项目根目录下的 nb_log_config.py 配置文件的 LOG_FILE_HANDLER_TYPE 设置默认的filehandler类型。

nb_log_config.py 的 LOG_PATH 配置默认的日志文件夹位置，如果get_logger函数没有传log_path入参，就默认使用这里的LOG_PATH

**Examples:**

Example 1 (unknown):
```unknown
在各种filehandler实现难度上 
单进程永不切割  < 单进程按大小切割 <  多进程按时间切割 < 多进程按大小切割

因为每天日志大小很难确定，如果每天所有日志文件以及备份加起来超过40g了，硬盘就会满挂了，所以nb_log的文件日志filehandler默认采用的是按大小切割，不使用按时间切割。

文件日志自动使用的默认是多进程安全切割的自定义filehandler，
logging包的RotatingFileHandler多进程运行代码时候，如果要实现向文件写入到规定大小时候并自动备份切割，win和linux都100%报错。

支持多进程安全切片的知名的handler有ConcurrentRotatingFileHandler，
此handler能够确保win和linux切割正确不出错，此包在linux使用的是高效的fcntl文件锁，
在win上性能惨不忍睹，这个包在win的性能在三方包的英文说明注释中，作者已经提到了。

nb_log是基于自动批量聚合，从而减少写入次数（但文件日志的追加最多会有1秒的延迟），从而大幅度减少反复给文件加锁解锁，
使快速大量写入文件日志的性能大幅提高，在保证多进程安全且排列的前提下，对比这个ConcurrentRotatingFileHandler
使win的日志文件写入速度提高100倍，在linux上写入速度提高10倍。
```

Example 2 (python):
```python
from multiprocessing import Process
from nb_log import LogManager, get_logger

# 指定log_filename不为None 就自动写入文件了，并且默认使用的是多进程安全的切割方式的filehandler。
# 默认都添加了控制台日志，如果不想要控制台日志，设置is_add_stream_handler=False
# 为了保持方法入场数量少，具体的切割大小和备份文件个数有默认值，
# 如果需要修改切割大小和文件数量，在当前python项目根目录自动生成的nb_log_config.py文件中指定。

# logger = LogManager('ha').get_logger_and_add_handlers(is_add_stream_handler=True,
# log_filename='ha.log')
# get_logger这个和上面一句一样。但LogManager不只有get_logger_and_add_handlers一个公有方法。
logger = get_logger(is_add_stream_handler=True, log_filename='ha.log')


def f():
    for i in range(1000000000):
        logger.debug('测试文件写入性能，在满足 1.多进程运行 2.按大小自动切割备份 3切割备份瞬间不出错'
                     '这3个条件的前提下，验证这是不是python史上文件写入速度遥遥领先 性能最强的python logging handler')


if __name__ == '__main__':
    [Process(target=f).start() for _ in range(10)]
```

Example 3 (unknown):
```unknown
注意说的是多进程，任何handlers在多线程下都没有问题，任何handlers在记录时候都加了线程锁了，完全不用考虑多线程。
线程锁不能跨进程特别是跨不同批次启动的脚本运行的解释器。
所以说的是多进程，不是多线程。

下面这段代码会疯狂报错。因为每达到100kb就想切割，多个文件句柄引用了同一个文件，某个进程想备份改文件名，别的进程不知情。

解决这种问题，有人会说用进程锁，那是不行的，如果把xx.py分别启动两次，没有共同的父子进程，属于跨解释器的，进程锁是不行的。

nb_log是采用的文件锁，文件锁在linux性能比较好，在win很差劲，导致日志拖累真个代码的性能，所以nb_log是采用把每1秒内的日志
聚合起来，写入一次文件，从而大幅减少了加锁解锁次数，
对比有名的concurrent_log_handler包的ConcurrentRotatingFileHandler，在win上疯狂快速写日志的性能提高了100倍，
在linux上也提高了10倍左右的性能。
```

Example 4 (python):
```python
"""
只要满足3个条件
1.文件日志
2.文件日志按大小或者时间切割
3.多进程写入同一个log文件，可以是代码内部multiprocess.Process启动测试，
  也可以代码内容本身不用多进程但把脚本反复启动运行多个来测试。

把切割大小或者切割时间设置的足够小就很容易频繁必现，平时有的人没发现是由于把日志设置成了1000M切割或者1天切割，
自测时候只随便运行一两下就停了，日志没达到需要切割的临界值，所以不方便观察到切割日志文件的报错。

这里说的是多进程文件日志切割报错即多进程不安全，有的人强奸民意转移话题老说他多线程写日志切割日志很安全，简直是服了。
面试时候把多进程和多线程区别死记硬背 背的一套一套很溜的，结果实际运用连进程和线程都不分。
"""
from logging.handlers import RotatingFileHandler
import logging
from multiprocessing import Process
from threading import Thread

logger = logging.getLogger('test_raotating_filehandler')

logger.addHandler(RotatingFileHandler(filename='testratationg.log', maxBytes=1000 * 100, backupCount=10))


def f():
    while 1:
        logger.warning('这个代码会疯狂报错，因为设置了100Kb就切割并且在多进程下写入同一个日志文件' * 20)


if __name__ == '__main__':
    for _ in range(10):
        Process(target=f).start()  # 反复强调的是 文件日志切割并且多进程写入同一个文件，会疯狂报错
        # Thread(target=f).start()  # 多线程没事，所有日志handler无需考虑多线程是否安全，说的是多进程文件日志切割不安全，你老说多线程干嘛？
```

---

## 6. 对比 loguru 10胜

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c6.html

**Contents:**
- 6. 对比 loguru 10胜
- 6.1 先比控制台屏幕流日志颜色，nb_log三胜。
- 6.2 比文件日志性能，nb_log比loguru快400%。
  - 6.2.1 loguru快速文件写入性能，写入200万条代码
  - 6.2.2 nb_log快速文件写入性能，写入200万条代码
- 6.3 多进程下的文件日志切割，nb_log不出错，loguru出错导致丢失大量日志。
- 6.4 写入不同的文件，nb_log采用经典日志的命名空间区分日志，比loguru更简单
- 6.5 按不同功模块能作用的日志设置不同的日志级别。loguru无法做到。
- 6.6 nb_log内置自带的log handler种类远超loguru
- 6.7 比第三方的日志handler扩展数量，nb_log完胜loguru

nb_log对比 loguru，必须对比，如果比不过loguru就不需要弄nb_log浪费精力时间

2）nb_log 自动使用猴子补丁全局改变任意print

3）nb_log 支持控制台点击日志文件行号自动打开并跳转到精确的文件和行号。

这个代码如果rotation设置10000 Kb就切割，那么达到切割会疯狂报错，为了不报错测试性能只能设置为1000000 KB

例如a模块的功能希望控制台日志可以显示debug，b模块的功能只显示info以上级别。

原生日志设置添加控制台和文件日志并设置日志格式是比loguru麻烦点，但这个麻烦的过程被nb_log封装了。

**Examples:**

Example 1 (unknown):
```unknown
nb_log为了保证多进程下按大小安全切割，采用了文件锁 + 自动每隔1秒批量把消息写入到文件，大幅减少了加锁解锁和判断时候需要切割的次数。
nb_log的file_handler是史上最强的，超过了任何即使不切割文件的内置filehandler,比那些为了维护自动切割的filehandler例如logging内置的
RotatingFileHandler和TimedRotatingFileHandler的更快。比为了保证多进程下的文件日志切割安全的filehandler更是快多了。

比如以下star最多的，为了确保多进程下切割日志文件的filehandler  
https://github.com/wandaoe/concurrent_log
https://github.com/unlessbamboo/ConcurrentTimeRotatingFileHandler
https://github.com/Preston-Landers/concurrent-log-handler

nb_log的多进程文件日志不仅是解决了文件切割不出错，而且写入性能远超这些4到100倍。
100倍的情况是 win10 + https://github.com/Preston-Landers/concurrent-log-handler对比nb_log
nb_log的文件日志写入性能是loguru的4倍，但loguru在多进程运行下切割出错。
```

Example 2 (python):
```python
import time

from loguru import logger
from concurrent.futures import ProcessPoolExecutor

logger.remove(handler_id=None)

logger.add("./log_files/loguru-test1.log", enqueue=True, rotation="10000 KB")


def f():
    for i in range(200000):
        logger.debug("测试多进程日志切割")
        logger.info("测试多进程日志切割")
        logger.warning("测试多进程日志切割")
        logger.error("测试多进程日志切割")
        logger.critical("测试多进程日志切割")


pool = ProcessPoolExecutor(10)
if __name__ == '__main__':
    """
    100万条需要115秒
    15:12:23
    15:14:18
    
    200万条需要186秒
    """
    print(time.strftime("%H:%M:%S"))
    for _ in range(10):
        pool.submit(f)
    pool.shutdown()
    print(time.strftime("%H:%M:%S"))
```

Example 3 (python):
```python
from nb_log import get_logger
from concurrent.futures import ProcessPoolExecutor

logger = get_logger('test_nb_log_conccreent', is_add_stream_handler=False, log_filename='test_nb_log_conccreent.log')


def f(x):
    for i in range(200000):
        logger.warning(f'{x} {i}')


if __name__ == '__main__':
    # 200万条 45秒
    pool = ProcessPoolExecutor(10)
    print('开始')
    for i in range(10):
        pool.submit(f, i)
    pool.shutdown()
    print('结束')
```

Example 4 (unknown):
```unknown
将10.2的代码运行就可以发现，loguru设置了10M大小切割，疯狂报错，因为日志在达到指定大小后切割需要备份重命名，
造成其他的进程出错。

win10 + python3.6 + loguru 0.5.3(任何loguru版本都报错，已设置enqueue=True)
出错如下。
Traceback (most recent call last):
  File "F:\minicondadir\Miniconda2\envs\py36\lib\site-packages\loguru\_handler.py", line 287, in _queued_writer
    self._sink.write(message)
  File "F:\minicondadir\Miniconda2\envs\py36\lib\site-packages\loguru\_file_sink.py", line 174, in write
    self._terminate_file(is_rotating=True)
  File "F:\minicondadir\Miniconda2\envs\py36\lib\site-packages\loguru\_file_sink.py", line 205, in _terminate_file
    os.rename(old_path, renamed_path)
PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'F:\\coding2\\nb_log\\tests\\log_files\\loguru-test1.log' -> 'F:\\coding2\\nb_log\\tests\\log_files\\loguru-test1.2021-08-25_15-12-23_434270.log'
--- End of logging error ---
```

---
