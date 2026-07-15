# TeleBirr Tip Calculator

total_bill = int(input("Enter Total bill  .."))

people=4

# Function
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

# Calculate each person's share
share = split_bill(total_bill, people)

# List of names
names = ["Sabona", "zarihun", "Tolasa", "Dawit"]

# Print each person's share
print("TeleBirr Tip Calculator")
print(f"Total Bill: {total_bill} ETB")
print(f"Tip Rate: 10%")
print(f"Each person pays: {share:.2f} ETB\n")

# Loop through names
for name in names:
    print(f"{name} pays {share:.2f} ETB")