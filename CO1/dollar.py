s=input('enter your string')
print(str(s))
a='$'
res=s.replace(s[0],a).replace(a,s[0],1)
print(str(res))
