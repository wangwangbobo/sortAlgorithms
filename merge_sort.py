# @author: WangBo
# @time：2019/12/23


def merge_sort(sort_list):
    # 归并排序算法实现
    if len(sort_list) <= 1:
        return sort_list
    mid = len(sort_list)//2
    left = merge_sort(sort_list[:mid])
    right = merge_sort(sort_list[mid:])
    return sort(left, right)


def sort(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    sort_list = [9, 2, 3, 1, 7, 6, 4, 8, 5, 10]
    sorted_list = merge_sort(sort_list)
    print(sorted_list)
