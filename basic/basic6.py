import itertools


class Sample():
    def __init__(self, val1):
        self.__instance_val1 = val1

    def __private_method(self):
        print(self.__instance_val1)


s = Sample(10)
# print(s.__instance_val1)
# 'Sample' object has no attribute '__instance_val1'

# s.__private_method()
# 'Sample' object has no attribute '__private_method'

for x, y, z in itertools.product(range(10), range(10), range(10)):
    print("%d,%d,%d" % (x, y, z))

list1 = itertools.product(range(10), range(10), range(10))
print(list1)
