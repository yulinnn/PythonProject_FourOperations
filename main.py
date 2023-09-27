import os
import sys
import getopt  # 实现命令行参数读取
import random
from fractions import Fraction  # 生成分数


# 全局变量
OPERATORS = ["+", "-", "×", "÷"]  # 四则运算符
MAX_DEPTH = 2  # 随机生成表达式的最大深度为2，则生成的表达式最多有三个运算符
RANDOM_FRACTION_PROB = 0.2  # 随机数生成中生成分数的概率
RANDOM_NUMBER_PROB = 0.3  # 表达式生成中子节点生成数字的概率
LIMIT = 1e-10  # 若两个数的差的绝对值小于LIMIT，则认为这两个数相等


# 二叉树结构
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# 将字符串写入文件
def write_to_file(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(data + "\n")


# 获取随机数，以一定概率生成分数
def get_random_num(random_max, fraction_available=True):
    if random.random() < 1 - RANDOM_FRACTION_PROB or fraction_available is False:
        return Fraction(random.randint(1, random_max))
    else:
        return Fraction(random.randint(1, random_max), random.randint(1, random_max))


# 将分数转化为字符串类型的带分数
def transform_to_mixed_number(num):
    if num < 1 or num == int(num):  # 若该数小于1，或该数为整数，直接返回该数
        return str(num)
    else:  # 否则将分数化为带分数
        fraction_int_part = int(num.numerator / num.denominator)
        fraction_frac_part = num - fraction_int_part
        return str(fraction_int_part) + "’" + str(fraction_frac_part)


# 根据深度（depth）获取随机表达式
def get_random_expression(depth, ranging, first_item=True):  # first_item：标记是否为根节点，防止出现x = x的情况
    # 以一定概率在子节点直接生成数字；若已到达二叉树最底层（depth == 0），直接生成随机数字
    if (not first_item and random.random() < RANDOM_NUMBER_PROB) or depth == 0:
        return Node(get_random_num(ranging))
    else:  # 未到达二叉树最底层，生成随机运算符
        node = Node(random.choice(OPERATORS))
        node.left = get_random_expression(depth - 1, ranging, first_item=False)
        node.right = get_random_expression(depth - 1, ranging, first_item=False)
        # 检查是否出现计算过程中产生负数的情况，若有则更改左右值
        if (node.left.item not in OPERATORS) and (node.right.item not in OPERATORS) \
                and (node.left.item - node.right.item < 0) and (node.item == "-"):
            while node.left.item - node.right.item < 0:
                node.left.item = get_random_num(ranging)
                node.right.item = get_random_num(ranging)
        return node


# 判断两棵树是否同构（判断表达式是否重复）
def is_isomorphic(root1, root2):
    if root1 == root2:
        return True
    if root1.item == root2.item:
        return is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right) \
               and is_isomorphic(root1.right, root2.left) and is_isomorphic(root1.left, root2.right)
    else:
        return False


# 前序遍历二叉树，计算表达式（若运算过程中出现除法运算右值为0的情况，则返回None）
def cal_expression(root):
    if root is None:
        return Fraction(0)
    if root.left is None and root.right is None:
        return root.item
    else:
        left_item = cal_expression(root.left)
        right_item = cal_expression(root.right)
        if left_item is None or right_item is None:  # 若左值或右值为None，说明计算过程中出现了除法运算右值为0的情况，返回None
            return None
        operator = root.item
        if operator == "+":
            return left_item + right_item
        elif operator == "-":
            return left_item - right_item
        elif operator == "×":
            return left_item * right_item
        elif operator == "÷":
            # 若出现除法运算右值为0的情况，则返回None
            if right_item == 0:
                return None
            else:
                return Fraction(left_item, right_item)


# 前序遍历二叉树，将表达式转化为字符串类型
def get_expression_str_recursion(root):
    if root is None:
        return " "
    if root.left is None and root.right is None:
        return transform_to_mixed_number(root.item)  # 将分数化为带分数
    else:
        left_value = get_expression_str_recursion(root.left)
        right_value = get_expression_str_recursion(root.right)
        operator = root.item
        return f"({left_value} {operator} {right_value})"  # 为子树的表达式添加括号，但会导致最终表达式两边也有括号，故额外设置函数处理


def get_expression_str(root):
    if root is None:
        return " "
    expression_str = get_expression_str_recursion(root)
    expression_str = expression_str[1:-1]  # 防止最终表达式两边有括号
    return expression_str


# 根据指定数量批量生成表达式和答案
def generate_expressions_and_answers(number, ranging):
    i = 0  # 遍历参数
    root_list = []  # 存放表达式根节点
    answer_list = []  # 存放答案
    while i < number:
        depth = get_random_num(MAX_DEPTH, fraction_available=False)  # 随机生成表达式深度
        new_root = get_random_expression(depth, ranging)  # 获取表达式的根节点
        answer = cal_expression(new_root)  # 计算表达式
        # 检查表达式答案是否为负数，或者计算过程中出现了除法运算右值为0的情况，若有则抛弃该表达式
        if answer is None or answer < 0:
            continue
        # 检查表达式是否重复，若有则抛弃该表达式
        is_repeated = 0
        for root in root_list:
            if is_isomorphic(new_root, root):
                is_repeated = 1
                break
        if is_repeated:
            continue
        # 存入新的表达式和答案
        root_list.append(new_root)
        answer_list.append(answer)
        i += 1

    expression_list = []  # 存放表达式字符串
    # 将表达式转换为字符串形式，并将答案列表中的分数转换为带分数
    i = 0  # 遍历参数
    while i < len(root_list):
        expression = get_expression_str(root_list[i])  # 将表达式转换为字符串形式
        expression_list.append(expression)
        answer_list[i] = transform_to_mixed_number(answer_list[i])  # 将分数转换为带分数
        i += 1

    return expression_list, answer_list


# 给定题目和答案，判断答案对错
def make_correction(exercise_path, answer_path):
    # 检查文件路径
    if not os.path.exists(exercise_path):
        print(f"\nERROR:Invalid File Path<{exercise_path}>\n")
        sys.exit()
    if not os.path.exists(answer_path):
        print(f"\nERROR:Invalid File Path<{answer_path}>\n")
        sys.exit()
    exercise_file = open(exercise_path, 'r', encoding='utf-8')
    answer_file = open(answer_path, 'r', encoding='utf-8')
    line_exe = exercise_file.readline()  # 逐行读题目文件
    line_ans = answer_file.readline()  # 逐行读答案文件
    correct_list = []  # 正确答案编号列表
    wrong_list = []  # 错误答案编号列表

    # 逐行进行答案检测
    while line_exe and line_ans:
        # 清洗读取内容
        exe = line_exe.split(".")
        ans = line_ans.split(".")
        exe_no = int(exe[0])  # 题目编号
        exe_expression = exe[1].strip()  # 题目表达式
        ans = ans[1].strip()  # 待测答案

        # 替换表达式中的乘号
        exe_expression = exe_expression.replace("×", "*")

        # 为保证函数eval正常使用，若表达式中存在分数，则为其加上括号
        while "/" in exe_expression:
            exe_expression = list(exe_expression)
            pos = exe_expression.index("/")
            exe_expression[pos] = "÷"  # 暂时将分号变为除号

            # 插入左括号
            i = pos - 1  # 遍历参数
            if i == 0:
                exe_expression.insert(0, "(")
            else:
                while exe_expression[i] not in ["(", " "] and i > 0:
                    i -= 1
                if i == 0:
                    exe_expression.insert(0, "(")
                else:
                    exe_expression.insert(i + 1, "(")

            # 插入右括号
            i = pos + 1  # 遍历参数
            while i < len(exe_expression) and exe_expression[i] not in [")", " "]:
                i += 1
            exe_expression.insert(i, ")")

            exe_expression = ''.join(exe_expression)

        # 替换表达式中的除号
        exe_expression = exe_expression.replace("÷", "/")

        # 若表达式中存在带分数，则将其转换为分数的一般形式
        while "’" in exe_expression:
            exe_expression = list(exe_expression)
            pos = exe_expression.index("’")

            # 获取带分数的分子部分
            i = pos + 1  # 遍历参数
            numerator = exe_expression[i]  # 带分数的分子部分
            while exe_expression[i + 1] != "/":
                numerator += exe_expression[i + 1]
                i += 1
            divide_pos = i + 1  # 除号下标

            # 获取带分数的整数部分
            i = pos - 1  # 遍历参数
            while exe_expression[i] != "(":
                i -= 1
            sub_start = i + 1  # 将要替换部分的开头下标
            integer = exe_expression[i + 1]  # 带分数的整数部分
            i += 2
            while i < pos:
                integer += exe_expression[i]
                i += 1

            # 获取带分数的分母部分
            i = divide_pos + 1  # 遍历参数
            denominator = exe_expression[i]  # 带分数的分母部分
            while exe_expression[i + 1] != ")":
                denominator += exe_expression[i + 1]
                i += 1
            sub_end = i  # 将要替换部分的结尾下标

            # 求得分数的一般形式
            new_numerator = int(integer) * int(denominator) + int(numerator)  # 分数一般形式的分子部分
            new_fraction = f"{new_numerator}/{denominator}"

            # 将原表达式中的带分数部分替换为分数的一般形式
            while sub_start < sub_end:
                del exe_expression[sub_start]
                sub_end -= 1
            exe_expression[sub_start] = str(new_fraction)

            exe_expression = ''.join(exe_expression)

        # 若待测答案为带分数，将其转换为小数，否则直接用eval计算
        if "’" in ans:
            ans = list(ans)
            pos = ans.index("’")

            # 获取带分数的分子部分
            i = pos + 1  # 遍历参数
            numerator = ans[i]  # 带分数的分子部分
            while ans[i + 1] != "/":
                numerator += ans[i + 1]
                i += 1
            divide_pos = i + 1  # 除号下标

            # 获取带分数的整数部分
            i = 0
            integer = ans[i]  # 带分数的整数部分
            while (i + 1) < pos:
                integer += ans[i + 1]
                i += 1

            # 获取带分数的分母部分
            i = divide_pos + 1  # 遍历参数
            denominator = ans[i]  # 带分数的分母部分
            while (i + 1) < len(ans):
                denominator += ans[i + 1]
                i += 1

            # 求得小数
            decimal = float(int(integer) + int(numerator) / int(denominator))
            ans = decimal
        else:
            ans = eval(ans)

        # 用eval计算原题的答案
        exe_expression_ans = eval(exe_expression)
        # print(exe_expression, "=", exe_expression_ans, ",",  ans)

        # 检测原题答案与待测答案是否相等，若两个数的差的绝对值小于LIMIT，则认为这两个数相等
        if abs(exe_expression_ans - ans) < LIMIT:
            correct_list.append(exe_no)
        else:
            wrong_list.append(exe_no)

        line_exe = exercise_file.readline()
        line_ans = answer_file.readline()

    return correct_list, wrong_list


# 主函数
def main(argv):
    number = 0
    ranging = 0
    exercise_file = " "
    answer_file = " "
    opts, args = getopt.getopt(argv[1:], "hn:r:e:a:", ["help", "number=", "range=", "exercise_file=", "answer_file="])

    n_included = 0  # 检测是否包含生成题目数量
    r_included = 0  # 检测是否包含数值范围参数
    e_included = 0  # 检测是否包含题目路径
    a_included = 0  # 检测是否包含答案路径
    for opt, arg in opts:
        if opt in ("-h", "--help"):  # 显示帮助
            print("\n本程序包含以下两种功能，两种功能可以同时使用，请注意每种功能的使用都必须提供完整的参数：\n"
                  "- 1. main.py -n [生成的表达式数量] -r [生成的表达式中数值的范围]，此功能可以随机生成答案非负的四则运算题目与对应答案，"
                  "分别存入执行程序的当前目录下的Exercises.txt文件和Answers.txt文件\n"
                  "- 2. main.py -e [题目路径] -a [答案路径]，此功能可以对给定的题目文件和答案文件，判定答案中的对错并进行数量统计，"
                  "统计结果存入执行程序的当前目录下的Grade.txt文件\n")
            sys.exit()
        if opt in ("-n", "--number"):
            try:
                number = int(arg)
            except:
                print("\n-n选项的参数输入有误，请重新输入。\n输入以下命令以获得帮助：main.py -h\n")
                sys.exit()
            if n_included == 0:
                n_included = 1
        elif opt in ("-r", "--ranging"):
            try:
                ranging = int(arg)
            except:
                print("\n-r选项的参数输入有误，请重新输入。\n输入以下命令以获得帮助：main.py -h\n")
                sys.exit()
            if r_included == 0:
                r_included = 1
        elif opt in ("-e", "--exercise_file"):
            exercise_file = arg
            if e_included == 0:
                e_included = 1
        elif opt in ("-a", "--answer_file"):
            answer_file = arg
            if a_included == 0:
                a_included = 1

    # 检测参数输入错误
    if (r_included == 1 and n_included == 0) or (r_included == 0 and n_included == 1) \
            or (e_included == 1 and a_included == 0) or (e_included == 0 and a_included == 1) or \
            (r_included == 0 and n_included == 0 and e_included == 0 and a_included == 0):
        print("\n参数提供有误，请输入以下命令以获得帮助：main.py -h\n")
        sys.exit()

    # 执行生成四则运算题目功能
    if n_included and r_included:
        expressions, answers = generate_expressions_and_answers(number, ranging)
        no = 1  # 题目编号
        for (expression, answer) in zip(expressions, answers):
            write_to_file("Exercises.txt", f"{no}. " + expression)
            write_to_file("Answers.txt", f"{no}. " + answer)
            no += 1
        print("\n已随机生成四则运算题目与对应答案，分别存入执行程序的当前目录下的Exercises.txt文件和Answers.txt文件\n")

    # 执行判定答案对错功能
    if e_included and a_included:
        correct_list, wrong_list = make_correction(exercise_file, answer_file)
        write_to_file("Grade.txt", f"Correct: {len(correct_list)} {correct_list}")
        write_to_file("Grade.txt", f"Wrong: {len(wrong_list)} {wrong_list}")
        print("\n统计结果已存入执行程序的当前目录下的Grade.txt文件\n")

    sys.exit()


if __name__ == "__main__":
    main(sys.argv)
