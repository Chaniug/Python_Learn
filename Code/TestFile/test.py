print("你好，世界 ")
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i} * {j} = {i * j}", end="\t")
#     print()
arr = [1, 2, 3, 4, 5]

double_arr = [arr[i] * 2 for i in range(len(arr))]
print(double_arr)
