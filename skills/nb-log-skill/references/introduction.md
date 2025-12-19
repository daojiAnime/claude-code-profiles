# Nb-Log-Skills - Introduction

**Pages:** 2

---

## 1.nb_log 简介

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c1.html

**Contents:**
- 1.nb_log 简介
- tips: 要想更简单简化使用日志,请安装kuai_log
- nb_log logging loguru 快速比较
- 1.0 nb_log 安装
- 1.0.1 nb_log不仅是日志，还对print以及sys.stdout(sys.stderr) 打了强力的猴子补丁
- 1.0.2 nb_log 新增支持loguru包模式来记录日志，原汁原味的loguru来打印控制台和写入日志文件，见文档1.10.b
- 1.1 nb_log 简单使用例子
  - 1.1.a nb_log 写入日志文件
  - 1.1.a2 nb_log 写入日志文件,并将错误日志同时写到另外的错误日志文件中
  - 1.1.b nb_log 的最核心函数 get_logger入参说明

nb_log readthedocs文档链接

文中文档较长，但其中大部分不是 讲解nb_log 的用法，是复习内置logging的概念。 是由于python人员不懂logging包的日志命名空间和python日志树形命名空间结构，不懂handlers和logger的关系是什么。 所以需要很长的篇幅。

很多pythoner到现在都不知道python的 logging.getLogger() 第一个入参的意义和作用，造成nb_log也不知道怎么使用多命名空间。

| 维度 | loguru | logging | nb_log | | ------ | ------- | ------- | ----------------- | | 易用性 | ✅ 简单 | ❌ 繁琐 | ✅ 简单 | | 命名空间 | ❌ 无 | ✅ 完善 | ✅ 完善 | | 第三方库兼容 | ❌ 容易污染 | ✅ 安全 | ✅ 安全 | | 美化输出 | ✅ 默认很好看 | ❌ 需配置 | ✅ 默认美观 | | 拓展性 | ⚠️ 不够灵活 | ✅ 高 | ✅ 更高（支持多 handler） | | 上手体验 | ✅ 快速爽 | ❌ 枯燥复杂 | ✅ 一秒用上好日志 |

对代码里面的print打了猴子补丁，自动显示print所在地方的文件名和精确行号，不怕有人胡乱print，找不到在哪里print的了。

对代码里面的 print 以及 streamHanlder日志调用的sys.stdout/stderr 打了猴子补丁，能支持所有标准输出自动写入到文件中,每天生成一个文件。 (见1.1.d配置文件说明的 SYS_STD_FILE_NAME 和 PRINT_WRTIE_FILE_NAME)。

有了这，还有什么理由还说nb_log不如loguru，loguru只是nb_log的一个子集。

nb_log不仅日志有极其绚烂的各种色彩,print也自动有色彩,色彩绚烂远超loguru。传统 logging 无论什么级别日志都是暗红色loguru 稍微区分了日志级别,对日志级别字段,有各种不同的前景色nb_log 对各种日志级别和print,采用了背景色 + 前景色渲染,色彩极其夸张,例如 error是粉红背景色,critical是血红背景色在超高速运行的程序里面,哪怕日志一秒上万条,只要使用nb_log,哪怕是800度近视,距离电脑屏幕10米之外,瞟一眼就能知道程序报错没

nb_log默认是只打印到控制台，不会把日志写入到文件、kafka、mongo、es、发邮件和钉钉的，nb_log 记录到每一种地方都有单独的控制参数。

只有get_logger 设置了log_filename，那么该logger才会写到这个文件，日志文件夹的路径是 nb_log_config.py 的 LOG_PATH 配置的。

get_logger 传参了 error_log_filename 后，error级别以上的日志会单独写入到错误文件中。 或者 在nb_log_config.py 配置文件中 配置 AUTO_WRITE_ERROR_LEVEL_TO_SEPARATE_FILE = True # 自动把错误error级别以上日志写到单独的文件，根据log_filename名字自动生成错误文件日志名字。

log_filename 用于设置是否写入日志文件和写入什么文件中。有的人不看入参文档，就问nb_log为什么不写入日志文件中。 logger和handler是观察者模式，日志记录到哪些地方，是由添加了什么handlers决定的。

项目中任意脚本使用nb_log,第一次运行代码时候，会自动在 sys.path[1] 目录下创建 nb_log_config.py文件并写入默认值。 之后nb_log 会自动 import nb_log_config, 如果import到这个模块了，控制台会提示读取了什么文件作为配置文件。

如果是 cmd或者linux运行不是pycharm，需要 设置 PYTHONPATH为项目根目录，这样就能自动在当前项目根目录下生成或者找到 nb_log_config.py了。

用户可以print(sys.path) print(sys.path[1]) 来查看 sys.path[1]的值是什么就知道了。

连PYTHONPATH作用是什么都不知道的python小白，一定要看下面文章 。

以上只是部分配置的例子，其他配置在你项目根目录下的 nb_log_config.py中都有默认值，自己按需修改设置。 其他例如日志模板定义，默认日志模板选择什么，都可以在 nb_log_config.py文件中设置。

nb_log_config.py中是设置全局设置，get_logger是针对单个logger对象生成的设置。

例如 nb_log_config.py 中写 FORMATTER_KIND = 4，get_logger 传参 formatter_template=6，那么最终还是使用第6个日志模板。 如果get_logger函数没有传参指定就使用 nb_log_config.py中的配置。 就是说 get_logger 是优先级高的，nb_log_config.py 是优先级低的配置方式。

如图：日志彩色符合交通灯颜色认知。绿色是debug等级的日志，天蓝色是info等级日志， 黄色是warnning等级的警告日志，粉红色是error等级的错误日志，血红色是criticl等级的严重错误日志

nb_log支持自动彩色，也支持关闭背景色块只要颜色，也支持彻底不要颜色所有日志显示为正常黑白颜色。

可以在你项目根目录下自动生成的nb_log_config.py配置文件中修改相关配置，来控制是否需要颜色，或者要颜色但不要大块的背景色块。

有的人听说了python显示颜色的博客，例如这种

nb_log 是基于python自带的原生logging模块封装的， nb_log.get_logger()生成的日志类型是 原生logging.Logger类型， 所以nb_log包对常用三方包日志兼容性替换芯做到了100%。是否是原生日志非常重要，logbook和loguru都不是python自带的原生日志， 所以和三方包结合或者替换性不好。

内置了一键入参，每个参数是独立开关，可以把日志同时记录到10几个常用的地方的任意几种组合， 包括 控制台 文件 钉钉 邮件 mongo kafka es 等等 。

有的人以为日志只能记录到控制台和文件，其实是错的，日志可以记录到很多种地方，日志记录到哪里，是由logger添加了什么handler决定的。

python命名空间非常重要,有的人太笨了,说设置了级别为logging.WARN,但是debug还是被记录,就是因为他牛头不对马嘴,忽视了是对什么命名空间设置的日志级别,debug日志又是什么命名空间的日志打印出来的

搜索一下文档的"命名空间"4个字,文档里面谈了几百次这个概念了,有的人logging基础太差了,令人吐血,需要在nb_log文档来讲,这样导致nb_log文档很长.

有些人简直是怕了原生logging了，为了创建一个好用的logger对象，代码步骤复杂的吓人，很多人完全没看懂这段代码意义， 因为他是一步步创建观察者handler，给handler设置好看的formattor，给给被观察者添加多个观察者对象。 大部分人不看设计模式，不仅不懂观察者模式，而且没听说观察者模式，所以这种创建logger方式完全蒙蔽的节奏。 其实这样一步步的写代码是为了给用户最大的自由来怎么创建一个所需的logger对象。如果高度封装创建logger过程那是简单了， 但是自定义自由度就下降了。 logging是原生日志，每个三方包肯定使用logging了，为了兼容性和看懂三方包，那肯定是要学习logging的，对logging望而却步， 想投机取巧只使用loguru是行不通的，三方包不会使用loguru，三方包里面各种命名空间的日志，等待用户添加handlers来记录日志， loguru缺点太大了。

nb_log把logging创建logger封装了，但同时get_logger暴露了很多个入参，来让用户自由自定义logger添加什么handler和设置什么formattor。 所以nb_log有原生logging的普遍兼容性，又使用简单

这种方式和上面1.8.1的方式差不多, 但不需要写大量python代码来创建logger对象。 虽然不需要写大量python代码来构建logger对象，但是需要写 LOGGING_CONFIG 字典， 这种字典如果写错了导致配置不生效或者报错，还是很麻烦的。很多人对这个配置完全蒙蔽，不知道什么意思。

先创建formattor，创建文件和控制台handler(当然也可以自定义发送钉钉的handler)，handler设置日志过滤级别，handler设置formattor， 不同的handler可以设置不同的formattor，例如同样是 logger.debug("hello world"),可以使文件和控制台记录的这条日志的前缀和字段不一样。

对不同命名空间的logger添加不同的handlers， 例如你只想打印控制台 就 logger = logging.getLogger("console_logger")，然后用这个logger.info(xxx)就可以打印控制台了。 例如你只想打写入文件 就 logger = logging.getLogger("file_logger")，然后用这个logger.info(xxx)就可以打印控制台了。 例如你打写入文件并且打印控制台 就 logger = logging.getLogger("console_plain_file_logger")，然后用这个logger.info(xxx)就可以打印控制台并且同时写入文件了。

对1.8.1和1.8.2不理解造成恐惧，是使大家使用loguru的主要原因。

nb_log ,你想简单不想get_loger,你想粗暴的导入就能记录日志到控制台和文件，代码如下：

综上所述 nb_log既使用简单，又兼容性高。

运行上面可以发现 logger1和logger2对象是同一个id，logger3对象是另外一个id。 通过不同的日志命名空间，可以设置不同级别的日志显示，设置不同类型的日志记录到不同的文件，是否打印控制台，是否发送邮件 钉钉消息。

有人问我是怎么知道要记录 werkzeug 和 myapp 这两个日志命名空间的日志?

nb_log比logurur有10个优点方面

get_logger 传参 is_use_loguru_stream_handler=True 或者 nb_log_config.py 设置 DEFAULUT_IS_USE_LOGURU_STREAM_HANDLER = True，那么就是使用loguru来打印控制台。

get_logger 传参 log_file_handler_type=7 或者 nb_log_config.py 设置 LOG_FILE_HANDLER_TYPE = 7，那么就使用loguru的文件日志handler来写文件。

通过nb_log操作logurur很容易实现 a函数的功能写入a文件，b函数的功能写入b文件。

之前有人还是质疑怀疑nb_log不如loguru，现在nb_log完全支持了 loguru，那还有什么要质疑的。

就如同有人怀疑funboost框架，那么funboost就增加支持celery整体作为broker，完全使用celery的调度核心来执行函数，还比亲自操作celery简单很多。

作者一直是包容三方框架的，说服不了你，就兼容第三方包。

要精通python logging.getLogger第一个入参意义，非常非常重要。

nb_log readthedocs文档链接

**Examples:**

Example 1 (unknown):
```unknown
kuai_log 是没有基于logging封装,但kuai_log是100%兼容logging包的方法名和入参.
kuai_log的KuaiLogger方法和入参在logging的Logger一定存在且相同, 但是logging包有的小众方法,kuai_log不存在

kuai_log比logging和loguru快30倍,比nb_log快4倍.

kuai_log 不需要配置文件,全部用入参

kuai_log 没有依赖任何三方包,nb_log依赖某些三方包
```

Example 2 (python):
```python
print('导入nb_log之前的print是普通的')

from nb_log import get_logger

logger = get_logger('lalala',)   # get_logger 只有一个name是必传递的，其他的参数不是必传。
# logger = get_logger('lalala',log_filename='lalala.log',formatter_template=5,log_file_handler_type=2) # get_logger有很多其他入参可以自由定制logger。


logger.debug(f'debug是绿色，说明是调试的，代码ok ')
logger.info('info是天蓝色，日志正常 ')
logger.warning('黄色yello，有警告了 ')
logger.error('粉红色说明代码有错误 ')
logger.critical('血红色，说明发生了严重错误 ')

print('导入nb_log之后的print是强化版的可点击跳转的')
```

Example 3 (python):
```python
from nb_log import get_logger
logger = get_logger('logger_namespace',
                    log_filename='namespace_file.log',
                    error_log_filename='f4b_error.log')
logger.debug('这条日志会写到文件中')
```

Example 4 (python):
```python
from nb_log import get_logger
logger = get_logger('logger_namespace',
                    log_filename='namespace_file.log',
                    error_log_filename='namespace_file_error.log')
logger.debug('这条日志会写到普通文件中')
logger.error('这条日志会写到普通文件中，同时会单独写入到错误文件中')
```

---

## 10 nb_log 更新记录

**URL:** https://nb-log-doc.readthedocs.io/zh-cn/latest/articles/c10.html

**Contents:**
- 10 nb_log 更新记录
- 10.1 2023.07 nb_log 新增 print和标准输出 自动写入到文件中
- 10.2 2023.12 新增 错误error级别以上日志文件写入单独的日志文件中
- 10.3 2023.12 新增 支持loguru来打印控制台和写入文件

按照网友的建议，nb_log 新增 print和标准输出 自动写入到文件中

此功能是通过对print和sys.stdout/stderr打强力的猴子补丁的方式实现的，用户的print和没有添加fileHandler只有streamHandler的日志可以自动写入到文件中。

此项功能可以通过nb_log_config.py 或者环境变量来配置，是否自动写入到文件和写入到什么文件名字。

**Examples:**

Example 1 (unknown):
```unknown
# 项目中的print是否自动写入到文件中。值为None则不重定向标准输出到文件中。 自动每天一个文件， 2023-06-30.my_proj.out,生成的文件位置在定义的LOG_PATH
# 如果你设置了环境变量，export PRINT_WRTIE_FILE_NAME="my_proj.print" (linux临时环境变量语法，windows语法自己百度这里不举例),那就优先使用环境变量中设置的文件名字，而不是nb_log_config.py中设置的名字
PRINT_WRTIE_FILE_NAME = Path(sys.path[1]).name + '.print' 

# 项目中的所有标准输出（不仅包括print，还包括了streamHandler日志）都写入到这个文件。自动每天一个文件， 2023-06-30.my_proj.std,生成的文件位置在定义的LOG_PATH
# 如果你设置了环境变量，export SYS_STD_FILE_NAME="my_proj.std"  (linux临时环境变量语法，windows语法自己百度这里不举例),那就优先使用环境变量中设置的文件名字，，而不是nb_log_config.py中设置的名字
SYS_STD_FILE_NAME = Path(sys.path[1]).name + '.std'
```

---
