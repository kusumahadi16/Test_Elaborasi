from re import X


def GanjilGenap(x):
    if x.isnumeric() == True:
        if int(x)%2 == 0:
            print(x, " adalah bilangan genap")
        else:
            print(x, " adalah bilangan ganjil")
    else:
        print("Please input number")

if __name__=='__main__':
    print("Input angka : ")
    x = input()
    GanjilGenap(x)