# @author: WangBo
# @time：2019/12/23


def shell_sort(sort_list):
    # 希尔排序算法实现
    gap = len(sort_list)//2
    while gap > 0:
        for i in range(gap, len(sort_list)):
            j = i
            while (j-gap) >= 0 and sort_list[j-gap] > sort_list[j]:
                sort_list[j-gap], sort_list[j] = sort_list[j], sort_list[j-gap]
                j -= gap
        gap //= 2
    return sort_list


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = shell_sort(sort_list)
    print(sorted_list)
