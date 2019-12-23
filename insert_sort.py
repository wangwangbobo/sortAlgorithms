# @author: WangBo
# @time：2019/12/23


def insert_sort(sort_list):
    # 插入排序算法实现
    for i in range(1, len(sort_list)):
        for j in range(i, 0, -1):
            if sort_list[j] < sort_list[j-1]:
                sort_list[j-1], sort_list[j] = sort_list[j], sort_list[j-1]
    return sort_list


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = insert_sort(sort_list)
    print(sorted_list)
