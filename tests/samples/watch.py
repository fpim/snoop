import pysnooper


class Foo(object):
    def __init__(self):
        self.x = 2

    def square(self):
        self.x **= 2


@pysnooper.snoop(watch=(
        'foo.x',
        'io.__name__',
        'len(foo.__dict__["x"] * "abc")',
))
def main():
    foo = Foo()
    for i in range(2):
        foo.square()


expected_output = """
12:34:56.78 call        17 def main():
12:34:56.78 line        18     foo = Foo()
........... foo = <tests.samples.watch.Foo object at 0xABC>
........... foo.x = 2
........... len(foo.__dict__["x"] * "abc") = 6
12:34:56.78 line        19     for i in range(2):
........... i = 0
12:34:56.78 line        20         foo.square()
........... foo.x = 4
........... len(foo.__dict__["x"] * "abc") = 12
12:34:56.78 line        19     for i in range(2):
........... i = 1
12:34:56.78 line        20         foo.square()
........... foo.x = 16
........... len(foo.__dict__["x"] * "abc") = 48
12:34:56.78 line        19     for i in range(2):
12:34:56.78 return      19     for i in range(2):
Return value: None
"""