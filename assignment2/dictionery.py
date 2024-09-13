users = {}
total_users = int(input("Enter total number users : "))

for i in range(total_users):
    userid = int(input("Enter id :"))
    username = input("Enter name :")
    userage = int(input("Enter age : "))
    users[userid] = {
        "userid" : userid,
        "username" : username,
        "userage" : userage
    }

get_user = int(input("Enter userid to view details : "))

if get_user in users:
    print(users[get_user])

list = [1,2,3,4,5]
for i in list:
    print(i)

# for j in users.values():
    # print(j)