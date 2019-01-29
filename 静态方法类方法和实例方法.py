# coding:utf-8
"""
静态方法
1、如果某些操作不依赖具体实例，那么它就是静态的，反之如果某些操作是依赖具体实例的(例如访问一个特定会员的名称)，那它就应该是实例化的
2、如果某个方法使用频率较高，或者方法本身通用性较强，无需初始化类成员变量，则可以使用静态方法，那样方便，速度也快。
3、一切不需要实例化就可以有确定行为方式的函数都应该设计成静态的
4、还有很多要慢慢总结
"""

class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """
        定义实例方法，至少有一个self参数
        """
        print("实例方法")

    @classmethod
    def class_func(cls):
        """
        定义类方法，至少有一个cls参数
        """
        print("类方法")

    @staticmethod
    def static_func():
        """
        定义静态方法，无默认参数
        """
        print("静态方法")

f = Foo("中国")
# 调用实例方法
f.ord_func()

# 调用类方法
Foo.class_func()

#  调用静态方法
Foo.static_func()







