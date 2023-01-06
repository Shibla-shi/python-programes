def strng():
       m_str=input("enter the string:")
       n_str ={ }
       for i in m_str :
            if i in n_str:
                  n_str[i] += 1
            else :
                    n_str[i] = 1
print("count of all characters are:\n" , str(n_str))
strng()
