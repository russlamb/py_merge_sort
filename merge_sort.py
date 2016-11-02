def merge_sort(array):
    #print("array={0}".format(array))
    
    size = len(array)

    middle = int(size/2)
    #print("middle={0}".format(middle))
    if size>1:
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)
    else:
        return array

def merge(left, right):
    result = []

    i=0
    j=0

    while i<len(left) and j<len(right):
        #print("i={0} j={1}".format(i,j))
        l = left[i]
        r = right[j]
        if l<r:
            result.append(l)
            i = i+1
        else:
            result.append(r)
            j=j+1

    while i<len(left):
        result.append(left[i])
        i=i+1

    while j<len(right):
        result.append(right[j])
        j=j+1

    return result
            

def test():
    array = [5,4,9,3,1,2,8,2,3]
    print(array)
    print( merge_sort(array))

if __name__=="__main__":
    test()
    
