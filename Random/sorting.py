def test(sorter):
    assert sorter([]) == [] , sorter([])
    assert sorter([0]) == [0] , sorter([0])
    assert sorter([2,4,1,1,3]) == [1,1,2,3,4] , sorter([2,4,1,1,3])


def selection(arr):
    if len(arr) == 0: return []
    lowest = min(arr); arr.remove(lowest)
    return [lowest] + selection(arr)

test(selection)

def swap(duplet):
    if duplet[0] > duplet[1]:
        return [duplet[1]] + [duplet[0]]
    else:
        return [duplet[0]] + [duplet[1]]

def bubble(arr):
    if len(arr) == 0: return []
    for i in range(len(arr) - 1):
        arr = arr[:i] + swap(arr[i:i+2]) + arr[i+2:]
    return bubble(arr[:-1]) + [arr[-1]]

test(bubble)

def insert(elem, arr):
    if arr == []: return [elem]
    for i in range(len(arr)):
        if elem < arr[i]:
            return arr[:i] + [elem] + arr[i:]
    return arr + [elem]

def insertSort(arr):
    if len(arr) < 2: return arr
    output = [arr[0]]
    for i in range(1,len(arr)):
        output = insert(arr[i],output)
    return output

test(insertSort)

