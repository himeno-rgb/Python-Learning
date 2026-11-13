# 实现单通道和卷积核卷积运算的模块

"""
将卷积计算做一个步骤拆分：
·卷积核对应元素与对应矩阵位置的对应元素做乘法后求和
·求和结果填入结果矩阵成为对应位置的元素
·卷积核在矩阵上滚动，算下一个元素
"""


def cov_mult(C, D):  # 实现第一个步骤的函数
    if len(C) != len(D) or len(C[0]) != len(D[0]):
        return False
    else:
        temp = 0
        for i in range(len(C)):
            for j in range(len(C[0])):
                temp += C[i][j] * D[i][j]
        return temp


# 获得当前B中参与运算的部分，A表示卷积核，B表示卷积对象；
# a b分别表示现在A第一个元素对应的B中元素的行数和列数
def position(A, B, a, b):
    E = []
    if len(A) + a > len(B) or len(A[0]) + b > len(B[0]) or a < 0 or b < 0:
        return False
    else:
        for i in range(a, a + len(A)):
            temp = []
            for j in range(b, b + len(A[0])):
                temp.append(B[i][j])
            E.append(temp)
    return E


def conv(A, B):  # A表示卷积核，B表示卷积对象
    R = []  # 先创建卷积结果矩阵
    # 计算确定卷积结果矩阵的规模
    a = len(B) - len(A) + 1  # 计算卷积结果矩阵的行数
    b = len(B[0]) - len(A[0]) + 1  # 计算卷积结果矩阵的列数
    if a < 1 or b < 1:  # 确定计算前提合法
        return False
    # 实现卷积核滚动功能
    i = 0
    while i + len(A) <= len(B):
        j = 0
        temp = []
        while j + len(A[0]) <= len(B[0]):
            T = position(A, B, i, j)  # 获取当前B中参与运算的部分
            temp.append(cov_mult(A, T))
            j += 1
        R.append(temp)
        i += 1
    return R


# 测试函数功能是否正常
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]  # 测试统一规定采用2*2矩阵作为卷积核（权如代码所示）
    B = [[2, 4, 5, 1], [5, 4, 7, 6], [7, 3, 8, 9], [9, 3, 5, 2]]  # 测试示例

    # 输出测试示例
    print("测试实例如下：")
    print("卷积核：", A)
    print("运算示例：", B)

    # 输出运算结果
    print("卷积运算结果：")
    print(conv(A, B))
