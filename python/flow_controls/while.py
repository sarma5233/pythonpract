n = int(input("enter a number:"))
sum = 0
total_numbers = 1
while total_numbers <= n:
    sum += total_numbers
    total_numbers += 1
print("sum =", sum)


average = sum/n
print("Average = ", average)