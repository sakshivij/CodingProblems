import math
count = 0
print("Enter the values")
lst=[]
s=int(input())
for k in range (0,s):
    lst.append(int(input()))
for i in range (0,len(lst)):
    for j in range(0,len(lst)):
        if(i!=j):
            if(lst[i]==math.sqrt(lst[j])):
                count+=1
                print("The pair is ({},{}) and index values are i ={} & j = {}".format(lst[i],lst[j],i,j))
print(count)
           
