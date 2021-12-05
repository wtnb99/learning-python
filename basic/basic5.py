# func = lambda x: "★" + str(x) + "★"
def func(x): return "★" + str(x) + "★"


print(func("バナナ"))


# func = lambda x: x % 2 == 1
def func(x): return x % 2 == 1


is_odd = func(5)
print(is_odd)  # True

is_odd = func(6)
print(is_odd)  # False


# lambda 引数: 戻り値
def higher_order(datas, is_target):
    """ 高階関数のサンプル """
    for i in datas:
        if is_target(i):
            print(i)


datas = [1, 102, 900, 5, 3]
higher_order(datas, lambda x: x % 2 == 1)

print("----")


# ジェネレータ
def sample_generator():
    """ ジェネレータのサンプル """
    for i in range(10):
        yield i


gen_obj = sample_generator()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
