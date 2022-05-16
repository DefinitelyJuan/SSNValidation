import re
regexp = "^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$"
#Function that uses regexp to check if an string fulfills conditions for a valid Social Security Number.
def ValidateSSN(ssn : str):
    if(re.match(regexp,ssn)):
        return True
    else:
        return False


print("Welcome to the SSN Validator! \nMade by Juan Avila ID 1100378")
while(True):
    ssn = input("Write the SSN number you want to validate: ")
    if(ValidateSSN(ssn)):
        print(f"{ssn} is a valid Social Security Number") #if its valid then we tell the user it is
    else:
        print(f"{ssn} is not valid Social Security Number") #if its valid then we tell the user it is
    ans = input("Do you want to try another SSN? (Y/N): ")
    if(ans.upper() == "N"):
        break

print("Thanks for using my program! Have a nice day!")
input()
