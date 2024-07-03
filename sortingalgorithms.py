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
    generator = quicksort_algorithm(draw_info, 0, len(draw_info.lst) - 1, ascending)
    for _ in generator:
        yield True
    return draw_info.lst

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


def mergesort(draw_info: DrawInformation, ascending: bool=True):
    generator = mergesort_algorithm(draw_info, 0, len(draw_info.lst) - 1, ascending)

    for _ in generator:
        yield True
    return draw_info.lst


def mergesort_algorithm(draw_info: DrawInformation, i_low: int, i_high: int, ascending: bool):
    if i_low < i_high:
        i_middle = i_low + (i_high - i_low) // 2
        yield True
        yield from mergesort_algorithm(draw_info, i_low, i_middle, ascending)
        yield from mergesort_algorithm(draw_info, i_middle + 1, i_high, ascending)
        yield from mergesort_merge(draw_info, i_low, i_middle, i_high, ascending)


def mergesort_merge(draw_info: DrawInformation, i_low: int, i_middle: int, i_high: int, ascending: bool):
    lst = draw_info.lst
    tmp_lst = []

    i = i_low
    j = i_middle + 1
    while i <= i_middle and j <= i_high:
        if (lst[i] < lst[j] and ascending) or (lst[i] > lst[j] and not ascending):
            tmp_lst.append(lst[i])
            draw_list(draw_info, {i_high: draw_info.BLUE, i: draw_info.GREEN, j: draw_info.RED}, True)

            i += 1
        else:
            tmp_lst.append(lst[j])
            draw_list(draw_info, {i_high: draw_info.BLUE, i: draw_info.GREEN, j: draw_info.RED}, True)
            j += 1
    
    while i <= i_middle:
        tmp_lst.append(lst[i])
        draw_list(draw_info, {i_high: draw_info.BLUE, i: draw_info.GREEN}, True)
        i += 1

    while j <= i_high:
        tmp_lst.append(lst[j])
        draw_list(draw_info, {i_high: draw_info.BLUE, j: draw_info.RED}, True)
        j += 1

    for i in range(len(tmp_lst)):
        lst[i_low + i] = tmp_lst[i]
        draw_list(draw_info, {i_low + i: draw_info.BLUE}, True)
        yield True


def heap_sort(draw_info: DrawInformation, ascending: bool=True):
    lst = draw_info.lst
    heap_lst = []
    for i in range(len(lst)):
        heap_lst.append(lst[i])
        heapify_up(heap_lst, ascending)
        draw_list(draw_info, {i: draw_info.GREEN}, True)
        yield True
    
    n = len(heap_lst)
    for i in range(n):
        lst[i] = heap_lst[0]
        heap_lst[0] = heap_lst[n - 1 - i]
        heapify_down(heap_lst, n - 1 - i, ascending)
        draw_list(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
        yield True


def heapify_up(heap_lst: list, ascending: bool):
    i = len(heap_lst) - 1
    elem = heap_lst[i]
    while (i > 0):
        i_parent = (i - 1) // 2
        parent = heap_lst[i_parent]
        if (elem < parent and ascending) or (elem > parent and not ascending):
            # Swap parent by element
            heap_lst[i] = parent
            heap_lst[i_parent] = elem
            i = i_parent
        else:
            break


def heapify_down(heap_lst: list, i_last: int, ascending: bool):
    i_elem = 0
    elem = heap_lst[i_elem]

    i_left = 2 * i_elem + 1
    while i_left <= i_last:
        # Take lower or higher child according to ascending
        i_right = 2 * i_elem + 2
        if i_right <= i_last:
            if (heap_lst[i_left] < heap_lst[i_right] and ascending) or (heap_lst[i_left] > heap_lst[i_right] and not ascending):
                i_child = i_left
            else:
                i_child = i_right
        else:
            i_child = i_left
        
        if (heap_lst[i_child] < elem and ascending) or (heap_lst[i_child] > elem and not ascending):
            heap_lst[i_elem] = heap_lst[i_child]
            heap_lst[i_child] = elem

            i_elem = i_child
            i_left = 2 * i_elem + 1
        else:
            break
