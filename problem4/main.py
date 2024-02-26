def find_max_sum_sub_array(k, arr):
    # create sublist l size k
    lk=[]
    for l in range(len(arr)-k):
        lk.append(arr[l:k+l])
    
    max_sum=0
    for s in lk:
        sumlist=sum(s)
        if max_sum < sumlist:
             max_sum= sumlist
    return max_sum



if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8