# @author: WangBo
# @time：2019/12/23


def bubble_sort(sort_list):
    # 冒泡排序算法实现
    for i in range(len(sort_list) - 1, 0, -1):
        for j in range(i):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
sorted_sort_list = bubble_sort(sort_list)
print(sorted_sort_list)
