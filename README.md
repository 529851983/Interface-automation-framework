# Interface-automation-framework
这是一个接口自动化框架，适合小白搭建练习。
主要功能介绍：
1.用excel来管理用例（每个excel就是一个项目，每个sheet就是一个模块，每个模块中有多个接口，包含正常场景接口和异常场景接口）
2.参数提取：用excel中的一列来指定要提取返回内容的字段，格式{"被赋予的变量":"要提取的字符串"} 如 {"token":"token"}，在程序中用jsonpath来实现提取返回字段的value
3.参数引用：${变量名}引用自定义变量和接口返回提取的变量，${func()}引用自定义的方法变量，前者将变量保存于variables.ini配置文件中，后者写在custom_func.py文件中。原理是利用正则和反射等方法来实现
4.数据驱动：excel处理后的数据为可迭代的列表，每个元素都包含本次请求所需的相关数据，用@pytest.mark.parameters()来进行数据驱动
5.生成报告：生成allure报告和html的报告
6.conftest.py：定义用例传参和用例前后置的内容
7.all.py：程序运行的入口，可指定运行范围，如全部运行，按项目、按模块、运行正常用例等，也可指定运行环境

--todo：1.测试结果回填excel表；2.有异常时发送带报告的报警邮件；3.用django实现web页面；3.容器化运行；4.jenkins定时构建，集成allure报告；
