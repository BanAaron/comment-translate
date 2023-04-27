# 招呼用户的功能
def greeter(name: str):
    print(f"Hello {name}")


# 仅当这是主文件时运行
if __name__ == "__main__":
    # 向用户询问他们的名字
    print("What is your name?")
    # 获取用户输入
    user_intput = input()
    # 使用用户提供的文本调用问候器功能
    greeter(user_intput)
