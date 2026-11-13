from BasicConvolutionOne import conv

# 测试示例（读者可自行更改）
A = [[1, 2], [3, 4]]  # 卷积核
B = [[2, 4, 5, 1], [5, 4, 7, 6], [7, 3, 8, 9], [9, 3, 5, 2]]  # 卷积对象

# 输出测试示例
print("测试实例如下：")
print("卷积核：", A)
print("运算示例：", B)

# 输出运算结果
print("卷积运算结果：")
print(conv(A, B))
