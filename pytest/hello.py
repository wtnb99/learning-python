import re


def say_hello(person="Taro"):
    return f"Hello, {person}"


def extract_pattern(text):
    pattern = r"\S (PASS|FAIL) (S.*)$"
    r = re.search(pattern, text)
    if r:
        return r.group(1), r.group(2)


def main():
    print(say_hello("Taro"))
    print(say_hello("Jiro"))


if __name__ == '__main__':
    main()
