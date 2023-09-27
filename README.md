# PythonProject_FourOperations
| 这个作业属于哪个课程 | <center>[软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12)</center> |
| ----------------- | --------------- |
| 这个作业要求在哪里 | <center>[结对项目](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13016)</center> |
| 这个作业的目标 | 实现自动生成四则运算题目功能，以及给定题目和答案、判断答案对错的功能 |

注：main.py为程序源代码，requirements.txt为依赖，文件Answer_Vertification_test1、Answer_Vertification_test2中存放了运行测试中题目生成功能测试的结果，文件Expression&Answer_Generation_test1、Expression&Answer_Generation_test2、Expression&Answer_Generation_test3中存放了运行测试中错误检测功能测试的结果。

# <font color=#484891>项目需求</font>
题目：实现一个自动生成小学四则运算题目的命令行程序。   

需求：
1. 使用 -n 参数控制生成题目的个数。例如：
```
Myapp.exe -n 10
```
2. 使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围。例如：
```
Myapp.exe -r 10
```
将生成10以内（不包括10）的四则运算题目。该参数可以设置为1或其他自然数。该参数必须给定，否则程序报错并给出帮助信息。

3. 生成的题目中计算过程不能产生负数，也就是说算术表达式中如果存在形如e1 − e2的子表达式，那么e1 ≥ e2。
4. 生成的题目中如果存在形如e1 ÷ e2的子表达式，那么其结果应是真分数。
5. 每道题目中出现的运算符个数不超过3个。
6. 程序一次运行生成的题目不能重复，即任何两道题目不能通过有限次交换+和×左右的算术表达式变换为同一道题目。
7. 生成的题目存入执行程序的当前目录下的Exercises.txt文件，格式如下：
```
四则运算题目1
四则运算题目2
……
```
8. 在生成题目的同时，计算出所有题目的答案，并存入执行程序的当前目录下的Answers.txt文件，格式如下：
```
答案1
答案2
……
```
9. 真分数在输入输出时采用如下格式：真分数五分之三表示为3/5，真分数二又八分之三表示为2’3/8。特别的，真分数的运算如下例所示：1/6 + 1/8 = 7/24。
10. 程序应能支持一万道题目的生成。
11. 程序支持对给定的题目文件和答案文件，判定答案中的对错并进行数量统计，输入参数如下：
```
Myapp.exe -e <exercisefile>.txt -a <answerfile>.txt
```
&emsp;&emsp;统计结果输出到文件Grade.txt，格式如下：
```
Correct: 5 (1, 3, 5, 7, 9)
Wrong: 5 (2, 4, 6, 8, 10)
```
&emsp;&emsp;其中“:”后面的数字5表示对/错的题目的数量，括号内的是对/错题目的编号。为简单起见，假设输入的题目都是按照顺序编号的符合规范的题目。

# <font color=#484891>PSP</font>
| PSP2.1 | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| ----------------- | --------------- | --------------- | --------------- |
| Planning | 计划 | 25 | 25 |
| Estimate | 估计这个任务需要多少时间 | 10 | 10 |
| Development | 开发 | 600 | 480 |
| Analysis | 需求分析 (包括学习新技术) | 30 | 50 |
| Design Spec | 生成设计文档 | 20 | 20 |
| Design Review | 设计复审 | 10 | 10 |
| Coding Standard | 代码规范 (为目前的开发制定合适的规范) | 10 | 10 |
| Design | 具体设计 | 30 | 30 |
| Coding | 具体编码 | 210 | 240 |
| Code Review | 代码复审 | 30 | 60 |
| Test | 测试（自我测试，修改代码，提交修改） | 90 | 90 |
| Reporting | 报告 | 180 | 150 |
| Test Repor | 测试报告 | 60 | 60 |
| Size Measurement | 计算工作量 | 20 | 20 |
| Postmortem & Process Improvement Plan | 事后总结, 并提出过程改进计划 | 10 | 20 |
| overall | 合计 | 1335 | 1275 |

# <font color=#484891>开发环境</font>
## <font color=#6495ED>计算机配置</font>
<table border="1" width="500px" cellspacing="10">
<tr>
  <td>CPU</td>
  <td>AMD Ryzen 7 6800H</td>
</tr>
<tr>
  <td>内存大小</td>
  <td>16GB</td>
</tr>
<tr>
  <td>操作系统</td>
  <td>Windows 11, version 22H2</td>
</tr>
</table>

## <font color=#6495ED>编程语言与IDE</font>
<table border="1" width="500px" cellspacing="10">
<tr>
  <td>编程语言</td>
  <td>Python</td>
</tr>
<tr>
  <td>IDE</td>
  <td>PyCharm Community Edition 2022.2.2</td>
</tr>
</table>

## <font color=#6495ED>依赖</font>
<font size=3>python == 3.9.13</font>

# <font color=#484891>程序流程图</font>
![](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927175501218-724297925.png)

# <font color=#484891>模块接口的设计与实现</font>
## <font color=#6495ED>接口设计</font>
| <center>函数</center> | <center>功能</center> |
| ----------------- | --------------- |
| write_to_file(path, data) | 将参数data写入参数path指定的文件中 |
| get_random_num(random_max, fraction_available=True) | 随机生成范围在[1, random_max]的整数或分数 |
| transform_to_mixed_number(num) | 将分数num转化为字符串类型的带分数 |
| get_random_expression(depth, ranging, first_item=True) | 根据深度depth和数值的范围ranging生成随机表达式，该随机表达式以二叉树结构存储 |
| is_isomorphic(root1, root2) | 判断两棵二叉树是否同构，即判断两个表达式是否重复 |
| cal_expression(root) | 计算以二叉树结构存储的表达式 |
| get_expression_str_recursion(root), get_expression_str(root) | 将以二叉树结构存储的表达式转化为字符串类型 |
| generate_expressions_and_answers(number, ranging) | 根据数量number和数值的范围ranging批量生成字符串类型的表达式和答案 |
| make_correction(exercise_path, answer_path) | 根据题目文件的路径和答案文件的路径，判定答案中的对错并进行数量统计 |
| main(argv) | 主函数，以接受命令行参数的形式运行程序，将程序生成的结果存储到文件中 |
## <font color=#6495ED>具体实现</font>
### <font>二叉树结构</font>
&emsp;&emsp;采用二叉树结构生成表达式，存储形式如下：

![](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927143038420-474536264.png)

&emsp;&emsp;二叉树结构定义如下：
```
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
```
### <font>获取随机数</font>
&emsp;&emsp;随机生成范围在[1, random_max]的整数或分数，有0.2的概率（RANDOM_FRACTION_PROB）生成分数，并且可以通过参数fraction_available控制是否生成分数。具体实现如下：
```
def get_random_num(random_max, fraction_available=True):
    if random.random() < 1 - RANDOM_FRACTION_PROB or fraction_available is False:
        return Fraction(random.randint(1, random_max))
    else:
        return Fraction(random.randint(1, random_max), random.randint(1, random_max))
```
### <font>将分数转化为带分数</font>
&emsp;&emsp;将分数转化为字符串类型的带分数。具体实现如下：
```
def transform_to_mixed_number(num):
    if num < 1 or num == int(num):  # 若该数小于1，或该数为整数，直接返回该数
        return str(num)
    else:  # 否则将分数化为带分数
        fraction_int_part = int(num.numerator / num.denominator)
        fraction_frac_part = num - fraction_int_part
        return str(fraction_int_part) + "’" + str(fraction_frac_part)
```
### <font>获取随机表达式</font>
&emsp;&emsp;根据二叉树的深度depth递归创建随机表达式，在叶子节点随机生成数字、在非叶子节点生成运算符。函数在递归过程中有0.3的概率（RANDOM_NUMBER_PROB）直接生成数字而停止递归，并且设置了参数first_item以防止出现最终表达式为“x = x”的情况。此外，函数在递归过程中还会检查是否出现计算过程中产生负数的情况，若有则更改左右数值。具体实现如下：
```
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
```
### <font>判断表达式是否重复</font>
&emsp;&emsp;通过判断两棵二叉树是否同构来判断这两个表达式是否重复。具体实现如下：
```
def is_isomorphic(root1, root2):
    if root1 == root2:
        return True
    if root1.item == root2.item:
        return is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right) \
               and is_isomorphic(root1.right, root2.left) and is_isomorphic(root1.left, root2.right)
    else:
        return False
```
### <font>计算表达式</font>
&emsp;&emsp;通过前序遍历二叉树来计算表达式，并且包含对计算过程中出现除法运算右值为0的情况的处理，若有此现象发生则返回None。具体实现如下：
```
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
```
### <font>将表达式转化为字符串类型</font>
&emsp;&emsp;采用了两个函数实现该功能，通过前序遍历二叉树将以二叉树结构存储的表达式转化为字符串类型。为了避免歧义，二叉树每个子树所构成的表达式都要添加括号，但也会导致最终表达式两边也有括号，故额外设置函数处理该情况。具体实现如下：
```
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
```
### <font>批量生成表达式和答案</font>
&emsp;&emsp;调用上述函数，根据指定的数量number和数值范围ranging，批量生成字符串类型的表达式和答案。最终生成的表达式和答案满足以下条件：
- 所有表达式均不重复
- 每道题目中出现的运算符个数不超过3个（0 < depth < 3）
- 表达式的计算过程中不会出现负数，表达式的答案不为负数
- 表达式和答案中的真分数都为带分数形式

&emsp;&emsp;具体实现如下：
```
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
```
### <font>答案检测</font>
&emsp;&emsp;根据指定题目文件和答案文件，判定答案中的对错并进行数量统计。函数的具体流程为：
1. 逐行读取题目文件和答案文件
2. 对读取的表达式字符串和答案字符串进行清洗，仅保留表达式、题目编号和答案自身
3. 将表达式中的乘号“×”替换为“*”
4. 为表达式中的分数两边加上括号，避免最终计算错误
5. 将表达式中的除号“÷”替换为“/”
6. 将表达式中的带分数全部化为分数的一般形式
7. 若答案为带分数，则将其化为分数的一般形式
8. 用eval函数计算表达式字符串
9. 将表达式的计算结果与待测答案相减，若其绝对值小于一个特定值LIMIT（设置为1e-10），则认为这两个值相等，否则认为这两个值不等
10. 若表达式的计算结果与待测答案相等，将本题目的编号存入“正确”列表，否则存入“错误”列表
11. 若题目文件和答案文件未读取完成，返回步骤1.，否则转至步骤12.
12. 返回“正确”列表和“错误”列表

&emsp;&emsp;本功能通过函数make_correction实现。由于实现较为复杂，请在[Github](https://github.com/yulinnn/PythonProject_FourOperations)中查看函数make_correction的具体实现。
### <font>命令行的输入输出</font>
&emsp;&emsp;采用sys.argv和getopt库实现命令行选项和参数读取。本程序有五种命令行选项：
1. -h，显示帮助
2. -n [生成的题目数量]，控制生成题目的个数
3. -r [生成的表达式中数值的范围]，控制题目中数值（自然数、真分数和真分数分母）的范围
4. -e [题目路径] -a [答案路径]，对给定的题目文件和答案文件，判定答案中的对错并进行数量统计

&emsp;&emsp;其中选项-n、-r必须配合使用，选项-e、-a必须配合使用。同时使用选项-n、-r，则激活题目生成功能，结果存入执行程序的当前目录下的Exercises.txt文件和Answers.txt文件；同时使用选项-e、-a，则激活答案检测功能，统计结果存入执行程序的当前目录下的Grade.txt文件。这两种功能可以同时使用。
<br />&emsp;&emsp;若用户输入的选项中出现以下情况，则抛出错误提示：
1. -n和-r选项未搭配使用，-e和-a选项未搭配使用，或没有输入任何选项
2. 使用-n和-r选项时未能提供正确的参数（即整数）
3. 使用-e和-a选项时未能提供正确的文件路径（文件路径检测在函数make_correction中实现）

&emsp;&emsp;具体实现如下：
```
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
```
# <font color=#484891>测试运行</font>
## <font color=#6495ED>差错检测</font>
&emsp;&emsp;命令行参数输入错误时抛出错误提示，显示如下：
![screenshot1](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927162912322-632796611.png)
![screenshot2](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927162929336-1678351722.png)
![screenshot3](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927163008359-433795035.png)
&emsp;&emsp;文件路径错误时抛出错误提示，显示如下：
![screenshot4](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927163020864-1134781519.png)
## <font color=#6495ED>显示帮助</font>
&emsp;&emsp;输入命令main.py -h，程序使用帮助显示如下：
![screenshot5](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927163510002-1064907396.png)
## <font color=#6495ED>题目生成功能测试</font>
### <font>测试1</font>
&emsp;&emsp;生成20个题目，数值范围[1, 10]。输入参数-n 20 -r 10，结果如下：
![screenshot6](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927170903126-723369887.png)
![screenshot7](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927170910975-706358423.png)![screenshot8](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927170906801-1406123216.png)
### <font>测试2</font>
&emsp;&emsp;生成30个题目，数值范围[1, 30]。输入参数-n 30 -r 30，结果如下：
![screenshot9](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927171511543-2086293770.png)
![screenshot10](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927171609690-915078602.png)![screenshot11](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927171617278-931062477.png)
### <font>测试3</font>
&emsp;&emsp;生成10000个题目，数值范围[1, 20]。输入参数-n 10000 -r 20，结果如下（仅部分截图）：
![screenshot12](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927171903131-1658430804.png)
![screenshot13](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927171934747-276064059.png)![screenshot14](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927172001955-896654847.png)
## <font color=#6495ED>答案检测功能测试</font>
&emsp;&emsp;先通过程序的题目生成功能生成20个题目，再对生成的Answers.txt中的部分答案进行修改，然后用生成的表达式Exercises.txt与修改后的答案进行答案检测功能测试。
### <font>测试1</font>
&emsp;&emsp;生成20个题目，数值范围[1, 20]。输入参数-n 20 -r 20，结果如下：
![screenshot15](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927190545078-202777820.png)
![screenshot16](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927190627813-765766032.png)![screenshot17](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927190632541-233324859.png)
<br />&emsp;&emsp;对原答案进行修改，塞入几个错误答案，然后将修改后的答案作为待测答案，结果如下：
![screenshot18](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191032532-1354647363.png)
<br />&emsp;&emsp;将题目表达式的地址和修改后答案的地址输入命令行，结果如下：
![screenshot19](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191256119-875407996.png)
![screenshot20](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191405217-2020111862.png)
<br />&emsp;&emsp;可以看到错误的答案全部被检出。
### <font>测试2</font>
&emsp;&emsp;生成20个题目，数值范围[1, 40]。输入参数-n 20 -r 40，结果如下：
![screenshot21](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191631436-149520620.png)
![screenshot22](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191702270-316967460.png)![screenshot23](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927191740401-2060155727.png)
<br />&emsp;&emsp;对原答案进行修改，塞入几个错误答案，然后将修改后的答案作为待测答案，结果如下：
![screenshot24](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927193144669-688188374.png)
<br />&emsp;&emsp;将题目表达式的地址和修改后答案的地址输入命令行，结果如下：
![screenshot25](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927193236828-2109002240.png)
![screenshot26](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927193320670-1462372081.png)
<br />&emsp;&emsp;可以看到错误的答案全部被检出。
# <font color=#484891>性能分析</font>
&emsp;&emsp;使用Python自带的性能分析模块cProfile进行性能分析。由于答案检查功能只用到单个函数make_correction，性能分析意义较小，故仅对题目生成功能进行性能分析。
<br />&emsp;&emsp;在终端中输入对应命令，并以cumtime（指定的函数及其所有子函数从调用到退出消耗的累积时间）降序排序，分别测试在生成100个题目、1000个题目、10000个题目时的程序性能（表达式的数值范围均为[1, 20]），结果如下：
<br />&emsp;&emsp;生成100个题目时：
![screenshot27](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927194918593-967303774.png)
&emsp;&emsp;生成1000个题目时：
![screenshot28](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927195134345-895342271.png)
&emsp;&emsp;生成10000个题目时：
![screenshot29](https://img2023.cnblogs.com/blog/3270349/202309/3270349-20230927195150186-596325689.png)
&emsp;&emsp;可以看到，在生成100个题目、1000个题目、10000个题目时，分别耗时0.066s、0.840s、36.176s，题目生成效率分别为：1515.15题/s、1190.48题/s、276.43题/s，说明生成的题目越多、题目生成的效率越低，并且效率的降低呈非线性特征，生成的题目越多、效率降低的速度越快。
<br />&emsp;&emsp;分析函数占用的时间，发现在生成100个题目、1000个题目、10000个题目时，函数is_isomorphic的耗时占总耗时的比例分别为：3.03%、26.90%、67.12%，可以看到：随着题目生成增多，函数is_isomorphic的耗时占用比例呈非线性增高，在生成10000个题目时占比达到最高（函数generate_expressions_and_answers为生成题目功能的整合函数，故不计入）。函数is_isomorphic的作用是判断两颗二叉树是否同构、即判断两个表达式是否重复，每一个新生成的表达式都要与先前生成的表达式进行对比；随着生成表达式的增多，新生成的表达式需要对比的次数也增多，故生成n个题目需要对比的总次数遵循等差数列求和公式：n(n - 1) / 2，这也解释了为什么生成的题目越多、题目生成的效率越低。针对此性能问题暂未想到优化方案。
# <font color=#484891>项目小结</font>
&emsp;&emsp;本项目的开发过程中，遇到了很多边界问题导致的程序报错，以及很多由于表达式括号添加不当、带分数和分数的一般形式之间的转化操作有误而导致的计算错误，这些问题在错误检测功能、函数make_correction的实现过程中尤为突出，提醒了我对于功能设计和边界情况的处理应当更加小心谨慎，对于各种情形的判断应当有更加周全的考虑。
