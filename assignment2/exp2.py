# Creating a list 
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
# Accessing elements
print("Accessing element at index 2:", my_list[2])




# Slicing
print("Slicing from index 1 to 3:", my_list[1:3])
# Modifying elements my_list[2] = 10
print("List after modifying element at index 2:", my_list)

# Adding elements my_list.append(6)
print("List after adding element 6:", my_list)
# Removing elements my_list.remove(4)
print("List after removing element 4:", my_list)
# Sorting my_list.sort()
print("Sorted List:", my_list)
# Reversing my_list.reverse()
print("Reversed List:", my_list)

# Finding length
print("Length of List:", len(my_list))

# Looping through list for i in my_list:
for i in my_list:
    print(i)