######## Reading Files ########

employee_file = open("employees.txt", "r") #read file
# open("employees.txt", "w") #write to file
# open("employees.txt", "a") #append to end of file
# open("employees.txt", "r+") #read and write file


print(employee_file.readable()) #first check if file is readable
#print(employee_file.read()) #read entire file and prints
#print(employee_file.readline()) #reads first line and prints
#print(employee_file.readline()) #reads next line and prints
#print(employee_file.readlines()) #puts every line in list and prints
#print(employee_file.readlines()[1]) #prints element 1 of list

for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # always close the file at some point