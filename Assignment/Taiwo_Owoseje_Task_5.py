# Task 1: Create and Display
dish1 = input("Enter your favourite Nigerian dish: ")
dish2 = input("Enter another favourite Nigerian dish: ")
dish3 = input("Enter another favourite Nigerian dish: ")
dish_tuple = (dish1, dish2, dish3)
print(dish_tuple)
print("\n".join(dish_tuple))

# Task 2: Tuple and Input
best_friends = input("Enter the names of your 5 best friends (seperated only by space): ")
friends = tuple(best_friends.split())
reverse_friends = friends[::-1]
print(reverse_friends)

# Task 3: Tuple Operations
states = ("Ogun", "Osun", "Oyo", "Ondo", "Lagos")
print(states[0])
print(states[-1])
print("Lagos" in states)
print(len(states))

# Task 4: Tuple Unpacking
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
favcolor = input("Enter your favourite color: ")
htown = input("Enter your hometown: ")
details = first_name, age, favcolor, htown
print(type(details))
print(details)
print("\n".join(details))
print(f"Firstname: \t{first_name} \nAge: \t\t{age} \nFavourite colour: {favcolor} \nHometown: \t{htown}")

Task 5 Modify Tuple indirectly
print("Enter 3 items for your shopping list")
slist1 = input("Item 1: ")
slist2 = input("Item 2: ")
slist3 = input("Item 3: ")
slist = (slist1, slist2, slist3)
shlist = list(slist)
print(shlist)
shlist.append("salt")
shlist.append("cheese")
print(shlist)
slist = tuple(shlist)
print(slist)
print(" | ".join(slist))

# Task 6 Attendance Tracker
weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
yearmonth = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
name = input("Enter Student Name: ")
gender = input("Enter Gender: ")
course = input("Enter Course Track: ")
month = int(input("Enter Current Month in number(1-12): ")) - 1
day = int(input("Enter Current Day in number(1-7): ")) - 1

print("Days of the week", weekdays)
print("Months of the year", yearmonth)
print(f'''
    Student Name:   {name}
    Student Gender: {gender}
    Course Track:   {course}
    Current Month:  {yearmonth[month]}
    Current Day:    {weekdays[day]}
''')