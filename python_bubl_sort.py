import random

class Buble:
    def small_arr_sorting(self):
        li = [5,2,7,4,0,9,8,6]
        print("before sorting: ", li)
        n = 1
        while n < len(li):
            for i in range(len(li)-n):
                if li[i] > li[i+1]:
                   li[i],li[i+1] = li[i+1],li[i]
            n += 1
        print("after sorting:  ", li)

    def big_arr_sorting(self, arr_size):
        li = []
        for i in range(0, arr_size):
            li.append(random.randint(0, 200))
        if len(li)<10:
            print("before sorting: ", li)
        else:
            print("before sorting: ", li[0:5], "...", li[arr_size-6:arr_size-1])
        n = 1
        while n < len(li):
            for i in range(len(li)-n):
                if li[i] > li[i+1]:
                   li[i],li[i+1] = li[i+1],li[i]
            n += 1
        print("after sorting:  ", li[0:5], "...", li[arr_size-6:arr_size-1])


obj = Buble()