# Sast_python自由测试

> 本次测试，请严格按照要求答题,因为我用了某些测试文件去检测你们答案的正确与否，所以如果你们不按照要求做题的话，我的测试文件是没法跑成功的。

> 请在对应题号的py文件里做答

> 不要修改非question开头的其他文件，包括他们的路径

> 你们会用到的数据全部存在data.py文件内，使用时，请使用import等语句导入...不要复制粘贴那些数据，这也是测试中的一项

## 基础题

### 第一题

#### 题目要求：

操作data.py内的**operating\_system\_dict**字典，然后将发行时间在**year**(函数参数)之后的操作系统名称按照发行时间从近至远放入列表。

全部操作放入一个名为get_os的函数，最后的列表作为返回值

两个参数：os_dict 和 year， 一个对应字典，一个对应年份

如果参数 year 为 1990

执行函数获得的返回值：

	['Windows7', 'Red Hat Enterprise Linux', 'Debian']

### 第二题

#### 题目要求：

在sast\_python\_exam目录下，有一个exam\_file文件，我们现在的任务是实现一个名为**get\_special\_line**的函数

- 函数功能：读取上面的文件，获取其内容，然后将其中以特定字符串开头的行，存储到一个列表中。

- 函数参数：第一个参数为文件名，第二个参数为打开模式，第三个参数为特定字符串，其余参数自己随意添加，但前三个要保持顺序不变。

- 函数返回一个保存结果的列表


测试样例：

	print(get_special_line('exam_file', 'rt', 'Name'))

结果：

	["Namespaces are one honking great idea -- let's do more of those!"]

### 第三题

#### 题目要求：

从data.py中导入str_demo，然后建立一个名为**get\_most\_common\_char**的函数，
第一个参数为实际参数为刚才导入的字节序列，第二个参数为n，其他参数随意。

再写一个名为save\_data的函数，将get\_most\_common\_char的返回值，存储至当前目录下的**result_three**文件内，以便我们以后可以读取该文件来还原这个数据。

函数功能为：

- 调用函数，返回字符串内出现次数大于等于n的英文字母（区分大小写，顺序按找从多到少排列，如果出现次数相同，顺序不做要求）和他们出现的次数，返回值为包含这些信息的列表

- 内置的**collections**库中有一个很优秀的东西，滑稽，可以使用dir看一下。

测试样例：

	str_demo = b'Windows 3.1, made generally available on March 1, 1992, featured a facelift. In August 1993, Windows for Workgroups, a special version with integrated peer-to-peer networking features and a version number of 3.11, was released.'
	print(get_most_common_char(str_demo, 10))

结果：

	[('e', 23), ('a', 17), ('r', 15), ('n', 12), ('o', 11), ('i', 10), ('s', 10)]

### 第四题

#### 题目要求：

导入data.py中给定的路径path_name，构建一个名为add_log装饰器（现阶段，直接把装饰器的参数写死就可以），当被装饰的函数被执行的时候，该装饰器会将当前时间和当前文件的绝对路径以及当前的函数名保存在给定的path_name路径中的文件去（使用追加模式）。

- 提醒：我们需要处理路径不存在的情况，通过代码解决路径或者文件不存在的问题。

- 如果文件不存在，我们会创建这个文件。

- 老要求：不要改变被装饰函数的属性。

- 对于时间问题： **内置库datetime**

测试样例：

	@add_log
	def test():
    	pass
	test()
	test()

结果：

	2017-12-07 17:39:46.122810-----D:/pycode/sast_python_exam/question_four.py-----test
	2017-12-07 17:39:46.131312-----D:/pycode/sast_python_exam/question_four.py-----test

### 第五题

#### 题目要求：

创建两个异常类，一个为RunningError，一个为PowerError.内部实现均为pass就好。

创建一个Sensor类，内部包含两个保护变量power和running（都是布尔值），默认全部为False，通过使用@property将方法设为属性，实现设置与获取这两个变量

- 如果没有上电，就运行会抛出PowerError.(将running变量改为True)

- 如果在运行状态下(running为True)，将供电关闭，那么运行也会关闭。

创建一个TemperatureSensor类，继承Sensor类，继承Sensor类的构造方法。内部拥有一个队列保存最近n次的数据(私有属性)。

两个方法，一个是add_data向队列中添加数据，另一个是get_data获取队列内所有数据的平均值。（其实就是第二次的讨论课作业）

- 两个方法中要包含完整的错误处理，不论是添加数据，还是获取数据，机器没有运行则会抛出RunningError，如果没有运行是因为没有上电，则会抛出PowerError。

### 第六题

#### 题目要求：

将你认为自己写的比较好的py代码附上比较恰当的注释放入question_six文件夹。