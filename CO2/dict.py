list1=[ ]
list2=[ ]
n=int(input("enter no:of elements :\n"))
print("enter" ,n, "length")
for i in range(n):
      a=int(input())
      list1.append(a)
print("enter" ,n, "breadth")
for i in range(n):
      a=int(input())
      list2.append(a)
      dict={ }
      value=[ ]
      keys=[ ]
for i in range(n):
      area=list1[i] * list2[i]
      value.append(area)
      keys.append(i+1)
      dict[keys[i]]=value[i]
print("Dictionary is :\n",dict)
print("Largest area is :\n",max(value))
