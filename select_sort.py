# @author: WangBo
# @time：2019/12/23


def select_sort(sort_list):
    # 选择排序算法实现
    for i in range(len(sort_list)-1):
        min_index = i
        for j in range(i+1, len(sort_list)):
            if sort_list[j] < sort_list[min_index]:
                min_index = j
        if min_index != i:
            sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
    return sort_list


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = select_sort(sort_list)
    print(sorted_list)
