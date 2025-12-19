# Nb-Log-Skills - Troubleshooting

**Pages:** 1

---

## 9 nb_log常见疑问解答

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c9.html

**Contents:**
- 9 nb_log常见疑问解答
- 9.1 怎么把普通debug info日志写入文件a，把错误级别日志写到文件b？
- 9.2 没有使用pycahrm run运行，直接在linux或cmd运行，生成的nb_log_config.py 位置错误，或者导入不了nb_log_config模块
- 9.4 pyinstaller 打包后运行报错，no such file nb_log_config_default.py
  - 9.4.2 打包报错 no such file nb_log_config_default.py，解决方式2
- 9.5 怎么屏蔽和打开某一部分日志？（选择性关闭和打开某部分日志）
  - 9.5.1 真实代码例子，说明怎么屏蔽某个日志。
  - 9.5.2 你如何知道日志的命名空间 (name) 是什么?
  - 9.5.3 经常看到三方包中写 logger = logging.getLogger(_name_) 啥意思？这个logger对象的name命名空间是什么？
  - 9.5.4 日志命名空间是树形的

项目中任意脚本使用nb_log,第一次运行代码时候，会自动在 sys.path[1] 目录下创建 nb_log_config.py文件并写入默认值。 之后nb_log 会自动 import nb_log_config, 如果import到这个模块了，控制台会提示读取了什么文件作为配置文件。

如果是 cmd或者linux运行不是pycharm，需要 设置 PYTHONPATH为项目根目录，这样就能自动在当前项目根目录下生成或者找到 nb_log_config.py了。

用户可以print(sys.path) print(sys.path[1]) 来查看 sys.path[1]的值是什么就知道了。

连PYTHONPATH作用是什么都不知道的python小白，一定要看下面文章 。

说明完全不看文档，到现在还不知道PYTHONPATH的python人员太懒惰low了，文章说了很多次掌握PYTHONPATH的用途和好处了。

是因为导入不了 nb_log_config 模块，因为nb_log包是动态 importlib('nb_log_config')的，所以不能检测到需要打包nb_log_config.py

需要在pyinstaller打包时候生成的spec文件中去定义 hiddenimports 的值， hiddenimports=['nb_log_config'] ， 这样就会打包包括nb_log_config.py了，不会去自动新建配置文件了。

pyinstaller 使用spec文件来打包exe。 pyinstaller xxxx.spec 就可以了。

百度吧，连pyinstaller的spec文件的意义是什么都不知道就非要去打包，要先学习pystaller用法。

只要在你的代码中写上 import nb_log_config ，那么打包就会自动包括了，这样就不需要在spec文件中去定义 hiddenimports 的值了。

不懂日志命名空间的是不可能精通怎么设置日志级别的。

logger_a 和logger_b 是三方包里面的日志，你要调整日志级别，不可能去骚操作去三方包里面的源码修改日志级别吧？

你的原来代码，调用函数funa。啰嗦输出 模拟a函数里面啰嗦打印你不关心的日志aaaaa 这句话到控制台 x1.py

优化日志级别后的代码,这个代码的调用funa函数将不再啰嗦的输出INFO级别日志打扰你了,funb函数仍然正常的输出INFO日志。 x2.py

假设三方包 package1 的目录如下：

requests请求百度，requests使用的是urllib3封装的，urllib3中已经有日志已经记录了请求状态码和url了。只需要给urllib3添加handlers就行了。

有的日志 logger对象 是随着 类实例化时候动态创建的，不方便去修改日志级别。 因为有的日志是动态的在函数或者内里面去创建logger和设置日志级别。如果你提前设置日志级别，还是会被动态调用时候生成的logger的日志级别覆盖掉，

nb_log提供了提前锁定日志级别的方法，nb_log通过猴子补丁patch了 logging.Logger.setLevel方法，

使用 nb_log.LogManager('name1').preset_log_level(20) 可以给某个命名空间提前锁定日志级别，锁定日志级别后，后续再修改他的级别会使设置无效。

nb_log.LogManager('name1').preset_log_level(20) 比官方自带的设置日志级别方法 setLevel 的 nb_log.LogManager('name1').setLevel(20) 更强力， preset_log_level是锁定日志级别，后续无法再对name1命名空间修改日志级别；而setLevel 设置日志级别后，后续还可以修改日志级别。

实现控制台消息过滤的原理是对 sys.stdout.write 打了猴子补丁。

**Examples:**

Example 1 (unknown):
```unknown
有的人真的很头疼，老是问这种基础的低级问题，比如funboost的日志级别如何调，如何做到希望显示某个函数/模块的debug打印，但却又要关闭另一个模块/函数的info打印？
任何python日志只要是logging包实现的，日志就可以设置不显示和设置打开。

老是问这种问题，主要是不懂日志命名空间基本概念，尽管文档已经重复了不下50次这个名词，还是再在解答章节统一再啰嗦一次,说了无数次这个logging.getLogger第一个入参的意义，这就是文档长的原因。

这个问题从最基本的日志树形命名空间说起必须，不去了解日志name入参作用的人，永远搞不懂怎么关闭和打开特定日志，也不可能从根本性知道为什么不用print而要用日志。
```

Example 2 (unknown):
```unknown
在文档 1.6和 1.9 中就已经说明了， nb_log.get_logger  以及官方内置的 logging.getLogger 函数的第一个入参的name作用和意义了，
第一个入参作用是什么，这是python官方日志的重要特性，包括java语言的日志也是这样的，
如果连日志的name是什么都完全不知道，那就别说自己会使用日志了，请不要使用日志了，干脆自己封装个函数里面print和file.write算了，不懂name的作用的情况下使用日志毫无意义，不如print到底算了。
日志命名空间是python官方日志以及任何语言的最基本作用。

在nb_log文档中搜索 命名空间，会有很多讲解日志命名空间作用的，有的人嫌弃文档长，主要是花了很大篇幅讲解日志命名空间，这是官方日志的基本知识，
主要是有的人完全不懂官方内置日志的logging.getLogger(name) 入参的意义，所以造成文档长。
因为 nb_log使用的是官方logging实现的，于第三方包和各种扩展兼容性无敌， nb_log.get_logger 和 logging.getLogger 函数返回的都是原生logging.Logger对象，
所以兼容性无敌，这一点上远远的暴击loguru这种独立实现的logger对象。
```

Example 3 (python):
```python
import logging
from nb_log import get_logger

"""
logging.DEBUG 是个常量枚举，值是10
logging.INFO 是个常量枚举，值是20
logging.WARNING 是个常量枚举，值是30
logging.ERROR 是个常量枚举，值是40
logging.CRITICAL 是个常量枚举，值是50

用数字和常量枚举都可以。
"""


logger_a = get_logger('aaaa',log_level_int=logging.INFO)

logger_b = get_logger('bbbb',log_level_int=20)

def funa():
    logger_a.info('模拟a函数里面啰嗦打印你不关心的日志aaaaa')

def funb():
    logger_b.info('模拟b函数里面，对你来说很重要的提醒日志打印日志bbbbb')
```

Example 4 (unknown):
```unknown
import funa,funb
funa()
funb()
```

---
