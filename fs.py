import re

a=("x","y","z")
b=("","","")

def zipper(j,k):
    return list(zip(j,k))

def assign_input(x,y,z):
    global b
    b=(x,y,z)

def add():
        i0 = input("x: ")
        i1 = input("y: ")
        i2 = input("z: ")
        assign_input(i0,i1,i2)
        x = zipper(a,b)
        with open('log','a') as log:
            log.write("\n")
            X=x[0][0]+": "+x[0][1]
            X1=x[1][0]+": "+x[1][1]
            X2=x[2][0]+": "+x[2][1]
            log.write(X+"\n"+X1+"\n"+X2+"\n")
        print("\nEntry has been saved.\n")

def edit(num,name):
        indexNUM=0
        if name=='x':
            index = input("x: ")
            indexNum = 0
        if name=='y':
            index = input("y: ")
            indexNUM = 1
        if name=='z':
            index = input("z: ")
            indexNUM = 2

        number = num+indexNUM

        with open('log','r+') as log:
            data = log.readlines()

        data[number] = name+": "+index+"\n"
        data_string = ''.join(data)

        with open('log','w+') as log:
            log.writelines(data_string)

        print("\nEntry has been edited.\n")

x=[]
entire=""
q=0
while q == 0:
    n=0
    listen = input()

    if listen=="add":add()

    elif listen=="read":
        with open('log') as log:
            for l, line in enumerate(log):
                    entire = log.read()
                    entire = re.sub(r"x","x value",entire )
                    entire = re.sub(r"y","y value",entire )
                    entire = re.sub(r"z","z value",entire )
        print(entire)

    elif listen=="edit":
        spec = input("entry num: ")
        name = input("index name: ")
        specint = int(spec)
        num=1
        real = specint-1
        eq=4*real
        if specint != 1: num = eq+1
        edit(num,name)

    elif listen=="q":q=1
    elif listen=="":break
    else:print("Unrecognised command.")
