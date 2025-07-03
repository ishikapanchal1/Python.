text = input("enter a string")
if len(text) < 3:
    print(text)
elif text[-3:] == "ing":
    print(text + "ly")
else:
    print(text + "ing")
    
