
class Sort:
    def __init__(self, array, size):
        self.array = array
        self.size = size

    def quick_sort(self):
        array = self.array
        size = self.size
        self.quick_sort_rec(array, 0, size - 1)
        return array

    def quick_sort_rec(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.quick_sort_rec(array, left, pivot - 1)
            self.quick_sort_rec(array, pivot + 1, right)


    def partition(self, array, left, right):
        pivot = array[right]
        i = left - 1
        for j in range(left, right):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[right] = array[right], array[i + 1]
        return i + 1


sort_instance = Sort([5, 2, 4, 6, 1, 3], 6)
print(sort_instance.quick_sort())

