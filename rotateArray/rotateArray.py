arr = ["1","2","3","4","5","6","7","8","9","10"]
n = int(input("Enter value of P: "))
d = int(input("Enter value of d (0 or 1): "))
# print(val)
# n = 3
output = arr.copy()

for key,val in enumerate(arr):
    if(d == 0):
        posit = (key - n)
        if(posit < 0):
            posit = len(arr) + posit
        output[posit] = val
    if(d == 1):
        posit = (key + n)
        if(posit >= len(arr)):
            posit = posit - len(arr)
        output[posit] = val
print(output)