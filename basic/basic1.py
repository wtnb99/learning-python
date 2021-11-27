# 三項演算子
age = 20
is_adult = "大人です" if age >= 20 else "子供です"
print(is_adult)


# リスト内表記
list1 = [1, 2, 3, 4, 5]
list2 = [val * 2 for val in list1]
print(list2)


# 可変長引数
def func(x, y, *args):
    print(f"1番目の引数：{x}")
    print(f"2番目の引数：{y}")
    if args:
        print(f"3番目以降の引数：{args}")


func(1, 2)
print("------")
func(1, 2, 3, 4, 5)


# 可変長キーワード引数
def func(x, y, **kwargs):
    print(f"1番目の引数：{x}")
    print(f"2番目の引数：{y}")
    if kwargs:
        print(f"3番目以降の引数：{kwargs}")


func(x=1, y=2)
print("------")
func(x=1, y=2, z=3, w=4, t=5)


# 関数オブジェクト
def add_num(x, y):
    return x + y


f = add_num
z = f(100, 200)
print(z)
