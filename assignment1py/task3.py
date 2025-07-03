a=input("enter the first string :")
b=input("enter the second string :")
n_stringa=a[:2]+b[2:]
n_stringb=b[2:]+a[:2]
ans=n_stringa +' ' + n_stringb
print(ans)