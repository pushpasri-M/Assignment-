# Prompt the user for their age 
age = int(input("Enter your age: ")) 
# Check the age and print a message based on the age
if age < 18:   
   print("You are a minor.")
elif age < 65: 
    print("You are an adult.")
else:
    print("You are a senior citizen.")
