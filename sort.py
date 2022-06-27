from typing import *


def _swap(array, i, j):
    array[i], array[j] = array[j], array[i]


class Sort:
    def __init__(self, array: List, size: int) -> None:
        self.array = array
        self.size = size

    def quick_sort(self) -> List:
        array = self.array
        size = self.size
        self.quick_sort_rec(array, 0, size - 1)
        return array

    def quick_sort_rec(self, array, left, right) -> None:
        if left < right:
            pivot = self.partition(array, left, right)
            self.quick_sort_rec(array, left, pivot - 1)
            self.quick_sort_rec(array, pivot + 1, right)

    def partition(self, array, left, right) -> int:
        pivot = array[right]
        i = left - 1
        for j in range(left, right):
            if array[j] <= pivot:
                i += 1
                _swap(array, i, j)
        array[i + 1], array[right] = array[right], array[i + 1]
        return i + 1

    def insert_sort(self) -> List:
        array = self.array
        size = self.size
        for i in range(1, size):
            for j in range(i, 0, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array

    def select_sort(self) -> List[int]:
        array = self.array
        size = self.size
        for i in range(size - 1):
            min_index = i
            for j in range(i + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

    def bubble_sort(self) -> List[int]:
        array = self.array
        size = self.size
        for i in range(size - 1):
            for j in range(size - i - 1):
                if array[j] > array[j + 1]:
                    _swap(array, j, j + 1)
        return array

    def merge_sort(self) -> List:
        array = self.array
        size = self.size
        self.merge_sort_rec(array, 0, size - 1)
        return array

    def merge_sort_rec(self, array, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort_rec(array, left, mid)
            self.merge_sort_rec(array, mid + 1, right)
            self.merge(array, left, mid, right)

    def merge(self, array, left, mid, right):
        temp = [0] * (right - left + 1)
        i = left
        j = mid + 1
        k = 0
        while i <= mid and j <= right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
            k += 1

    def heap_sort(self) -> List:
        array = self.array
        size = self.size
        self.heap_sort_rec(array, size)
        return array

    def heap_sort_rec(self, array, size):
        self.build_max_heap(array, size)
        for i in range(size - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self.heapify(array, 0, i - 1)

    def build_max_heap(self, array, size):
        for i in range(size // 2, -1, -1):
            self.heapify(array, i, size - 1)

    def heapify(self, array, i, size):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left <= size and array[left] > array[largest]:
            largest = left
        if right <= size and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, largest, size)


sort_instance = Sort([5, 2, 4, 6, 1, 3], 6)
print(sort_instance.quick_sort())
print(sort_instance.bubble_sort())
print(sort_instance.merge_sort())
