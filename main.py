banana = "Test"
# age = 22
avg = 4.5

name = input("First Name: ")
# Cast a string to an int
try:
  age = int(input("Age: "))
  print(f"You picked {age}")
except:
  print("Not a valid input")


is_enrolled = True


print(type(banana))
print(type(name))
print(type(age))
print(type(avg))
print(type(is_enrolled))

empty = None

print(type(empty))
