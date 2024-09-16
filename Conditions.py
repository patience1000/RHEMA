# num_1 = 10
# num_2 = 15

# num = num_1 == num_2 
# print(num)

# if num_1 > num_2:
#     print("num_1 is lesser than num_2")
# else:
#     print("not true")

# age = int(input("please enter your age to check for eligibility:"))

# if age < 18 or age > 30:
#     print("sorry you are not eligible")
# else:
#     print("you are eligible")

# total = 0
# counter = 0
# while True:
#     num = int(input("enter three numbers to find average:"))
#     if num < 0:
#         break
#     total += num
#     counter += 1
# average = total / counter
# print(average)    
# var = 3
# while var < 100:
#     print(var)
#     var *= 2 

# total = 0
# while True:
#     tom_b = int(input("enter cost of tombrown sold:"))
#     if tom_b <= 0:
#         break
#     total += tom_b
# print(total)

# weather = input("enter weather condition:")

# if weather == "raining":
#     print("take an umbrella")
# elif weather == "cloudy":
#     print("wear a raincoat")
# elif weather == "sunny":
#     print("wear glasses")
# else:
#     print("unknown weather condition")

# list = [1,3,"dog",2.5,7,10]
# print(list)
# print(list[-5])

# list.append(8)
# print(list)

# list.insert(3,5)
# print(list)

# list.pop(-5)
# print(list)

# list.remove("dog")
# print(list)

# list.extend(["dog",5,15])
# print(list)

# list1.reverse()
# list1.sort()
# num = list1.index(5.9)
# list1.reverse()
# print(num)

# slice = list1[:3]
# print(slice)

# states = ["Abuja","Gombe","Taraba","Yola"]
# for state in states:
#     print(state)

#     even_num = [2,4,6,8,10,20,64]
#     for num in even_num:
#         print(num+10)

# my_list = [1, 2, 3, 4, 6]
# if 5 in my_list:
#     print('5 is in the list')
# else:
#     print('5 is not in the list')
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for num in my_list:
    if num % 2 == 0:
        print(f"{num} is even")
mylist = [-1, 2, -3, 4, 5, -6]
positive_numbers = [num for num in mylist if num > 0]
print(positive_numbers)

dictionary = {
    "Name": "Patience",
    "LastName": "Paul",
    "class": 1
}
print(dictionary["Name"])
print(dictionary ["LastName"])