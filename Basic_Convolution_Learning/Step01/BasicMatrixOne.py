# 用列表形式描述矩阵
# 实现矩阵基础的运算：包括加法，乘法，转置


def matrix_add(a, b):  # 矩阵加法函数
    C = []
    if len(a) != len(b) or len(a[0]) != len(b[0]):  # 矩阵相加前提是矩阵必须同型
        return False
    else:
        for i in range(len(a)):  # 使用双循环遍历矩阵
            temp = []
            for j in range(len(a[0])):
                temp.append(a[i][j] + b[i][j])
            C.append(temp)
        return C


def matrix_mult(a, b):  # 矩阵乘法函数
    if len(a[0]) != len(b):  # 矩阵能相乘的前提是前者列数等于后者行数
        return False
    else:
        D = []
        for i in range(len(a)):  # 使用双循环遍历矩阵
            temp = []
            for j in range(len(b[0])):
                item = 0
                for k in range(len(a[0])):  # 第三层循环累加
                    item = a[i][k] * b[k][j] + item
                temp.append(item)
            D.append(temp)
        return D


def matrix_cir(a):  # 矩阵转置运算函数
    E = []
    for i in range(len(a[0])):
        temp = []
        for j in range(len(a)):
            temp.append(a[j][i])
        E.append(temp)
    return E


# 测试函数功能是否正常
if __name__ == "__main__":  # 实现只在直接使用该文件时才执行以下测试代码
    # 测试示例
    A = [[2, 5], [4, 6]]
    B = [[9, 2], [4, 7]]

    # 输出测试示例
    print("测试实例如下：")
    print(A)
    print(B)

    # 输出运算结果
    print("矩阵相加：")
    print(matrix_add(A, B))
    print("矩阵相乘：")
    print(matrix_mult(A, B))
    print("示例1矩阵转置：")
    print(matrix_cir(A))
