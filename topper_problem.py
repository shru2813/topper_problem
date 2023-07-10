n = str(n)
l = list(n)
even = 0
odd = 0
for num in l:
    if int(num) % 2 == 0:
        even += int(num)
    else:
        odd += int(num)
if(even == odd):
    print("True")
else:
    print("False")
