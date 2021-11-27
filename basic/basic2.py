import numbers


# 例外処理
def div_num(a, b):
    """ 割り算結果をprint """
    try:
        val = a / b
        print("{} / {} = {}".format(a, b, val))
    except ZeroDivisionError:
        print("0で割ることはできません")
    except TypeError:
        print("数値を入力してください")
    except Exception as e:
        print(e)  # 例外オブジェクトをprint
    else:
        print("正常終了")
    finally:
        print("終了")


div_num(10, 2)
div_num(10, 0)
div_num(10, 3)
div_num("10", 3)


# 例外発生
def calc10times(num):
    """ 10倍して返す """
    if not isinstance(num, numbers.Number):
        raise TypeError("数値を入力してください")
    return num * 10


val = calc10times(10)
print(val)
val = calc10times("10")
print(val)
