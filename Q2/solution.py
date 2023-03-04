n = int(input())

allValid = True
errorCodes = []

for i in range(n):
    record = input().split()
    isValid = record[0]
    if isValid == "false":
        allValid = False
        errorCodes.append(record[1])

if allValid:
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))
