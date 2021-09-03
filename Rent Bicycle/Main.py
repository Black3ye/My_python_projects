import time
#Este programa tiene como objetivo prestar motocicletas y saber si estan prestadas
bicycle = list()
def load_resources():
    f = open("data")
    for i in f:
        bicycle.append(i)
    temp = ["",2]
    for r in range(len(bicycle)):
        temp = bicycle[r]
        temp = temp.strip()
        temp = temp.split(",")
        bicycle[r]=temp

def start():
    for a in range (len(bicycle)):
        status = "Don't Available"
        if (bicycle[a][1] == "1"):
            status = "Available"
        print(str(a) +'- ' + bicycle[a][0]+'     '+status)
    vv=0
    while(vv == 0):
        try:
            pick= int(input("Select ID of the Motocycle: "))
            if (pick<8):
                vv= 1
            else:
                print("Motocycle not found. Try another ID number")
            
        except:
            print("Only can put numbers. Try Again ")
    money = input("You need to insert $2: ")
    money= float(money)
    while (money < 2.00):
        money = str(money)
        total = input("Your total is "+ money +", you need a total of $2: ")
        total = float(total)
        money= float(money)
        money = money + total
    
    bicycle[pick][1]=0
    start = time.time()
    print("Thanks you have 30 minutes. Have fun")
    t=0
    while (t < 1800):
        
        time.sleep(1)
        End = time.time()
        t = round(End - start)
        print(t)

load_resources()
datetime = time.strftime(format("%I : %M %p"))
print(datetime)
start()