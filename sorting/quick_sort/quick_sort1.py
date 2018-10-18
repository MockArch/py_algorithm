from __future__ import division

class QuickSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data Cant be None')
        print (self._sort(data))


    def _sort(self, data):
        if len(data) < 2:
            return data
        pivot_index = len(data)//2
        pivot_value = data[pivot_index]    
        equal = []
        left = []
        right = []
        for i in data:
            if i == pivot_value:
                equal.append(i)
            elif i < pivot_index:
                left.append(i)
            elif i > pivot_index:
                right.append(i)
        left_ = self._sort(left)
        right_ = self._sort(right)
        return left_ + equal + right_              
                



if __name__ == "__main__":
    d = [5]#, 7, 2, 6, -3, 5, 7, -1]
    quick_sort = QuickSort()
    quick_sort.sort(d)



