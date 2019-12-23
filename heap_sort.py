# @author: WangBo
# @time：2019/12/23


def heap_sort(sort_list):
    # 堆排序算法实现
    n = len(sort_list)
    first = int(n / 2 - 1)
    for start in range(first, -1, -1):
        max_heapify(sort_list, start, n - 1)
    for end in range(n - 1, 0, -1):
        sort_list[end], sort_list[0] = sort_list[0], sort_list[end]
        max_heapify(sort_list, 0, end - 1)
    return sort_list


def max_heapify(sort_list, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and sort_list[child] < sort_list[child + 1]:
            child += 1
        if sort_list[root] < sort_list[child]:
            sort_list[root], sort_list[child] = sort_list[child], sort_list[root]
            root = child
        else:
            break


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = heap_sort(sort_list)
    print(sorted_list)
