lst_fruit=['Fruit',['Apple','Banana','Mango','Orange']]
for i in lst_fruit:
    if isinstance(i,list):
        print(f"{lst_fruit}conatins list{i}")
    else:
        print(f"{lst_fruit} not contains list{i}")
            