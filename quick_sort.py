# @author: WangBo
# @time：2019/12/23


def quick_sort(sort_list, start, end):
    # 快速排序算法实现
    if start >= end:
        return
    pivot = sort_list[start]
    low = start
    high = end
    while low < high:
        while low < high and pivot < sort_list[high]:
            high -= 1
        sort_list[low] = sort_list[high]
        while low < high and sort_list[low] < pivot:
            low += 1
        sort_list[high] = sort_list[low]
    sort_list[low] = pivot
    quick_sort(sort_list, start, low-1)
    quick_sort(sort_list, low+1, end)
    return sort_list


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = quick_sort(sort_list, 0, 9)
    print(sorted_list)
