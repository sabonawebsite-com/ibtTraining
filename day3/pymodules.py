#citys=["addis","Adama","bahir dar","mekele","gondar"]
# citys.sort()
# citys.reverse()
# citys.append("hawassa")
# citys.insert(2,"dire dawa")
# citys.pop(4)
# for city in citys.sort():
#     print(city)
#enumerete
# for i, city in enumerate(citys):
#     print(f"{i}: {city}")
# # print(citys[1:4])
# # print(citys[0])
# #this is example of list slicing
# for city in citys:
#     print(city)
# #print(len(citys))

#
# location=(253,465,798)
# print(location[0])
#
# customers={"chaltu": 25, "joba": 30, "Boba": 35}
# customers["Boba"]=40
# print(customers["Boba"])

#sets
# numbers={12,35,85,23,23}
# num={12,35,45,1}
# print(set(numbers | num))

# import random
# name=random.choice(["sabona","usman","fantaa"])
# print(name)
# import math
# print(math.sqrt(25))
# import sys  
# from PIL import Image  

# # Check if at least one argument is passed  
# if len(sys.argv) < 2:  
#     print("Usage: python your_script.py image1 image2 ...")  
#     sys.exit(1)  

# images = []  

# # Load images  
# for arg in sys.argv[1:]:  
#     try:  
#         image = Image.open(arg)  
#         images.append(image)  
#     except Exception as e:  
#         print(f"Error loading image {arg}: {e}")  

# # Check if any images were successfully loaded  
# if not images:  
#     print("No images were loaded, exiting.")  
#     sys.exit(1)  

# # Save the images as a GIF  
# output_file = "fota.gif"  # Change to GIF format for animated output  
# try:  
#     images[0].save(  
#         output_file, save_all=True, append_images=images[1:], duration=200, loop=0  
#     )  
#     print(f"Saved {output_file} successfully.")  
# except Exception as e:  
#     print(f"Error saving the image: {e}")   
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())
#end code
try:
    num = int(input("Enter number: "))
    print(100 / num)
except:
    print("Invalid input")
print('Thanks')