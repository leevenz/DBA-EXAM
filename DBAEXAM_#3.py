print("Sample Output:")
mhire = int(input("Enter the number of newly hired males: "))
fhire = int(input("Enter the number of newly hired females: "))
mperma = int(input("Enter the number of permanent position males: "))
fperma = int(input("Enter the number of permanent position females: "))
mres = int(input("Enter the number of resigned males: "))
fres = int(input("Enter the number of resigned females: "))
print("")
print("===")
print("Thank you for the Information")
print("===")
print("Here is the Summary!!!\n")

totalHired = mhire + fhire
totalPermament = mperma + fperma
totalResigned = mres + fres

print("Number of Hired Employee =", totalHired)
print("Male = %.2f%%" % ((mhire * 100) / totalHired))
print("Female = %.2f%%" % ((fhire * 100) / totalHired))
print("")
print("Number of Permanent Employee =", totalPermament)
print("Male = %.2f%%" % ((mperma * 100) / totalPermament))
print("Female = %.2f%%" % ((fperma * 100) / totalPermament))
print("")
print("Number of Resigned Employee =", totalHired)
print("Male = %.2f%%" % ((mres * 100) / totalResigned))
print("Female = %.2f%%" % ((fres * 100) / totalResigned))