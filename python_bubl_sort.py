import random
from tqdm import tqdm

class Buble:
    def arr_sorting(self, arr_size):
        li = []
        for i in range(0, arr_size):
            li.append(random.randint(0, 200))

        if len(li)<10:
            print("before sorting: ", li)
        else:
            print("before sorting: ", li[0:5], "...", li[arr_size-6:arr_size-1])

        pbar = tqdm(total= (arr_size))
        n = 1
        pbar.update(1)
        while n < len(li):
            for i in range(len(li)-n):
                if li[i] > li[i+1]:
                   li[i],li[i+1] = li[i+1],li[i]
            n += 1
            pbar.update(1)
        pbar.close()
        print("after sorting:  ", li[0:5], "...", li[arr_size-6:arr_size-1])


obj = Buble()