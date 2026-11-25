def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("简单计算器")
    print("支持的运算：+  -  *  /")

    while True:
        try:
            left = float(input("请输入第一个数字："))
            operator = input("请输入运算符：").strip()
            right = float(input("请输入第二个数字："))

            if operator not in operations:
                print("错误：只支持 +、-、*、/")
                continue

            result = operations[operator](left, right)
            print(f"结果：{result:g}")

        except ValueError as error:
            print(f"输入错误：{error}")

        choice = input("继续计算吗？(y/n)：").strip().lower()
        if choice != "y":
            print("程序结束")
            break


if __name__ == "__main__":
    main()
# update

# update

# clone

# branch
