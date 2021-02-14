class ReverseArray(object):
    def __init__(self, arr: list):
        self.arr = arr
    def __str__(self):
        return f'{self.arr}'
    def reversal(self):
        for i in range(len(self.arr)//2):
            other = len(self.arr) - i - 1
            if i is not other:
                self.arr[i], self.arr[other] = self.arr[other], self.arr[i]

        return self


if __name__ == '__main__':
    lst = [2,4,7]
    print(ReverseArray(lst).reversal())