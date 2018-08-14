id = []
dpt = []
firstName = []
lastName = []
number = []
blood = []


def data():
    with open('sample.txt', 'r') as f:
        for l in f:
            z = l.split()
            id.append(int(z[0]))
            dpt.append(z[1])
            firstName.append(z[2])
            lastName.append(z[3])
            number.append(z[4])
            blood.append(z[5])


def show():
    with open('sample.txt', 'r') as f:
        for i in range(len(id)):
            print("Student data: ")
            print("ID: {}".format(id[i]))
            print("Department: {}".format(dpt[i]))
            print("First Name: {}".format(firstName[i]))
            print("Last Name: {}".format(lastName[i]))
            print("Contact Number: {}".format(number[i]))
            print("Blood Group: {}".format(blood[i]))
            print()


def entry(a):
    with open('sample.txt', 'a') as f:
        f.write(a + '\n')
    z = a.split()
    id.append(int(z[0]))
    dpt.append(z[1])
    firstName.append(z[2])
    lastName.append(z[3])
    number.append(z[4])
    blood.append(z[5])


def find(a):
    for i in range(len(id)):
        if id[i] == a:
            print("Student data: ")
            print("ID: {}".format(id[i]))
            print("Department: {}".format(dpt[i]))
            print("First Name: {}".format(firstName[i]))
            print("Last Name: {}".format(lastName[i]))
            print("Contact Number: {}".format(number[i]))
            print("Blood Group: {}".format(blood[i]))
            print()
            break
        print("Data not found for id: {}".format(a))


def dataAt(a):
    if a >= 0 and a < len(id):
        for i in range(len(id)):
            if i == a:
                print("Student data: ")
                print("ID: {}".format(id[i]))
                print("Department: {}".format(dpt[i]))
                print("First Name: {}".format(firstName[i]))
                print("Last Name: {}".format(lastName[i]))
                print("Contact Number: {}".format(number[i]))
                print("Blood Group: {}".format(blood[i]))
                print()
                break
    else:
        print("Invalid index")


def findByDpt(a):
    for i in range(len(id)):
        if a == dpt[i]:
            print("Student data: ")
            print("ID: {}".format(id[i]))
            print("Department: {}".format(dpt[i]))
            print("First Name: {}".format(firstName[i]))
            print("Last Name: {}".format(lastName[i]))
            print("Contact Number: {}".format(number[i]))
            print("Blood Group: {}".format(blood[i]))
            print()

def sorting():
    for i in range(len(id)):
        for j in range(len(id)):
            if id[i]< id[j]:
                temp = id[i]
                id[i] = id[j]
                id[j] = temp

                temp1 = dpt[i]
                dpt[i] = dpt[j]
                dpt[j] = temp1

                temp1 = firstName[i]
                firstName[i] = firstName[j]
                firstName[j] = temp1

                temp1 = lastName[i]
                lastName[i] = lastName[j]
                lastName[j] = temp1

                temp1 = number[i]
                number[i] = number[j]
                number[j] = temp1

                temp1 = blood[i]
                blood[i] = blood[j]
                blood[j] = temp1

    with open('sample.txt', 'w') as f:
        for i in range(len(id)):
            strn = str(id[i])+ " " + dpt[i] + " "+ firstName[i]+" "+lastName[i]+" "+number[i]+" "+blood[i]
            f.write(strn+'\n')
def stdRemove(a):
    for i in range(len(id)):
        if a == id[i]:
            id.remove(id[i])
            dpt.remove(dpt[i])
            firstName.remove(firstName[i])
            lastName.remove(lastName[i])
            number.remove(number[i])
            blood.remove(blood[i])
            break
    with open('sample.txt', 'w') as f:
        for i in range(len(id)):
            strn = str(id[i])+ " " + dpt[i] + " "+ firstName[i]+" "+lastName[i]+" "+number[i]+" "+blood[i]
            f.write(strn+'\n')

def main():
    data()
    x = input("Press y to continue or n to quit: ")
    if x == "y":
        while x != "n":
            print(
                "Press 1 to see data\n press 2 to enter data\n press 3 to find data\n press 4 to find data using "
                "index\n "
                " press 5 to sort data\n press 6 to search for student by department\n press 7 to remove student info\n")

            n = int(input("Press the desired key: "))

            if n == 1:
                show()

            elif n == 2:
                a = "\n"
                print("Data input format: ")
                print("ID First name Last name contact number blood group{} ".format(a))
                str = input("Input your data accordingly: ")
                entry(str)
            elif n == 3:
                src = int(input("Enter id number: "))
                find(src)
            elif n == 4:
                idx = int(input("Enter your index from {} to {} : ".format(0, len(id) - 1)))
                dataAt(idx)
            elif n == 5:
                sorting()
            elif n == 6:
                dpt = int(input("Enter department: "))
                findByDpt(dpt)
            elif n == 7:
                rmv = int(input("Please enter Student ID to remove: "))
                stdRemove(rmv)
            x = input("Do you wish to continue: ")


main()
