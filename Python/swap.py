#swap two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print(f"num1 = {num1}")
print(f"num2 = {num2}")



# swap elements in an array

arr = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

print("Before swap:", arr)

i = int(input("Enter first position: "))
j = int(input("Enter second position: "))

temp = arr[i]
arr[i] = arr[j]
arr[j] = temp

print("After swap:", arr)
