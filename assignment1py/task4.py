a = input("write the sentence")
word=a.split()
count_a={}
for i in word:
    if i in count_a:
        count_a[i]+=1
    else:
        count_a[i]=1
        print(count_a)