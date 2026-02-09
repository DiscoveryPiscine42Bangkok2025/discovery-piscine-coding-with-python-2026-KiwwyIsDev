print("Enter the first number:")
fnum = int(input())
print("Enter the second number:")
snum = int(input())
result = fnum * snum
print(f"{fnum} x {snum} = {result}")
if result == 0:
    print("This number is both positive and negative.")
elif result > 0:
    print("This number is positive.")
else:
    print("This number is negative.")