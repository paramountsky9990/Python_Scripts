def select_second(input_list):
    input_list.sort()  # Use the sort method on the input_list
    second = input_list[1]  # Use square brackets to access elements by index
    return second

n = int(input("Enter the length of the array: "))
array = []
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    array.append(element)

# Assign array to input_list, not input_array
input_list = array

print(select_second(input_list))
