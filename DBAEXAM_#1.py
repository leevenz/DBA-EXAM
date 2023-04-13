x = [5, 1, 4, 6, 7, 3, 5, 7, 3]

print(x)
print("On the array above print the duplicate elements.")

solo = []
dupli = []
 
for i in x:
    if i not in solo:
        solo.append(i)
    elif i not in dupli:
        dupli.append(i)

print("----------")
print("Duplicated Elements are the following:")
for i in dupli:
    print(i)