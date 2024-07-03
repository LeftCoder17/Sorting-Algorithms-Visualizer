#Bubble Sort, Insertion Sort, Quicksort, Merge Sort, Heap Sort

from draw import draw_list
from drawinformation import DrawInformation


def bubble_sort(draw_info: DrawInformation, ascending: bool=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if (lst[j] > lst[j + 1] and ascending) or (lst[j] < lst[j + 1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst


def insertion_sort(draw_info: DrawInformation, ascending: bool=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        value2insert = lst[i]
        j = i - 1
        while ((lst[j] > value2insert and ascending) or (lst[j] < value2insert and not ascending)) and j >= 0:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, True)
            yield True
            j = j - 1
    
    return lst


def quicksort(draw_info: DrawInformation, ascending: bool=True):
    lst = draw_info.lst
    generator = quicksort_algorithm(draw_info, 0, len(lst) - 1, ascending)
    for _ in generator:
        yield True
    return lst

def quicksort_algorithm(draw_info: DrawInformation, i_low: int, i_high: int, ascending: bool=True):
    if i_low < i_high:
        partition_index = quicksort_partition(draw_info, i_low, i_high, ascending)
        yield True
        yield from quicksort_algorithm(draw_info, i_low, partition_index - 1, ascending)
        yield from quicksort_algorithm(draw_info, partition_index + 1, i_high, ascending)

def quicksort_partition(draw_info: DrawInformation, i_low: int, i_high: int, ascending: bool=True):
    lst = draw_info.lst

    # Median of three
    i_middle = i_low + (i_high - i_low) // 2
    if (lst[i_low] > lst[i_middle]) and (lst[i_low] < lst[i_high]):
        i_median = i_low
    elif (lst[i_middle] > lst[i_low]) and (lst[i_middle] < lst[i_high]):
        i_median = i_middle
    else:
        i_median = i_high
    
    if i_median != i_high:
        lst[i_median], lst[i_high] = lst[i_high], lst[i_median]

    pivot = lst[i_high]
    i = i_low

    for j in range(i_low, i_high):
        if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
            lst[i], lst[j] = lst[j], lst[i]
            draw_list(draw_info, {i_high: draw_info.BLUE, j: draw_info.RED, i: draw_info.GREEN}, True)
            i += 1
    
    # Put pivot in correct position
    lst[i], lst[i_high] = lst[i_high], lst[i]

    return i
