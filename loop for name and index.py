user=[]
for i in range(5):
    print("ENTER THE NAME")
    user_input=input()
    user.append(user_input)
for index, user_input in  enumerate(user):
    print(f"{index}: {user_input}")