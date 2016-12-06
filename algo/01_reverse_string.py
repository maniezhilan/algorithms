def reverse_string(start,end,str):
    while(start < end):
        tmp = str[start]
        str[start] = str[end]
        str[end] = tmp
        start+=1
        end-=1
arr = ['h','e','l','l','o']
reverse_string(0,len(arr)-1,arr)
print arr