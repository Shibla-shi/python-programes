lst_num=input("enter list of integers")
lst_num=lst_num.split()
lst_num=[int (x) for x in lst_num]
lst_num=['over' if x>100 else x for x in lst_num]
print("all list",lst_num)

