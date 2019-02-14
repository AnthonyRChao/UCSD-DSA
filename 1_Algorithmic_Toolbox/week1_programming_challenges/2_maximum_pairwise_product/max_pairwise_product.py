# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1, max2 = 0, 0
    max_index_1 = 0
    for index, first in enumerate(numbers):
        if first > max1:
            max1 = first
            max_index_1 = index
    for index, second in enumerate(numbers):
        if second > max2 and index != max_index_1:
            max2 = second

    return max1 * max2 


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
