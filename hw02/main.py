def bsearch(data,target):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if target>data[mid]:
            low=mid+1
        elif target<data[mid]:
            high=mid-1
        else:
            return mid
            break
data=[1,2,3,4,5]
target=int(input("请输入需要查找的元素："))
pt= bsearch(data,target)
print(pt)
