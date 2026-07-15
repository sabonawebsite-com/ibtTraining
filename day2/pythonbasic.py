# #temperature calculater
# temp = int(input("s: "))

# if temp < 15:
#     print(f" The temprature is {temp} 0C you should wear fat clothes")
# elif temp <= 28:
#     print(f" The temprature is {temp} 0C you should wear thin clothes")
# else:
#     print("You need more water to sastiand")
# #end

# #for loop expl
# for i in range(1, 11):
#     print(f"Receipt #{i}")

# #end

# #even or odd
# for i in range(1, 29):
#     if i % 2 == 0:
#         print(i)
# #end

# def apply_discount(price, percent=10):
#     return price - (price * percent / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 20))
# #end
# count = 9

# while count > 0:
#     print(count)
#     count -= 1

# print("Liftoff!")
# #end
# customers = [("bona", 1200), ("Sara", 700), ("mota", 300)]

# def tier(balance):
#     if balance >= 1000:
#         return "Premium"
#     elif balance >= 500:
#         return "Standard"
#     return "Basic"

# for name, balance in customers:
#     print(name, tier(balance), balance)
# #end
# fruits = ["dinich", "muz", "qara"]
# print(fruits[0])    

# fruits.append("timatim")
# print(fruits)



# #end
# student = {
#     "name": "sabo",
#     "age": 25
# }
# print(student["name"])


# print(student["name"])

# #end code
# numbers = {1, 2, 2, 3}
# print(numbers)
# #end code
# nums = [1, 2, 3, 4]
# squares = [x * x for x in nums]

# print(squares)
# #end code

# import math

# print(math.sqrt(25))
#end code
with open("names.txt", "r") as file:
    print(file.read())
#end code
try:
    num = int(input("Enter number: "))
    print(100 / num)
except:
    print("Invalid input")

# this is all concept of Day 2 
print('Thanks')