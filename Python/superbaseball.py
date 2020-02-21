import random

def ovr(list):
    pos = list[0]
    pow = list[3]
    con = list[4]
    spd = list[5]
    fld = list[6]
    arm = list[7]
    vel = list[8]
    jnk = list[9]
    acc = list[10]

    ovr = 0
    if pos=='C':
        ovr += arm * .32
        ovr += fld * .32
        ovr += pow * .14
        ovr += con * .14
        ovr += spd * .08
    elif pos=='1B':
        ovr += pow * .48
        ovr += con * .21
        ovr += spd * .07
        ovr += arm * .12
        ovr += fld * .12
    elif pos=='2B':
        ovr += pow * .07
        ovr += con * .30
        ovr += spd * .20
        ovr += arm * .20
        ovr += fld * .23
    elif pos=='3B':
        ovr += pow * .24
        ovr += con * .16
        ovr += spd * .16
        ovr += arm * .20
        ovr += fld * .24
    elif pos=='SS':
        ovr += pow * .16
        ovr += con * .21
        ovr += spd * .21
        ovr += arm * .21
        ovr += fld * .21
    elif pos=='LF': 
        ovr += pow * .16
        ovr += con * .36
        ovr += spd * .16
        ovr += arm * .16
        ovr += fld * .16
    elif pos=='CF':
        ovr += pow * .10
        ovr += con * .20
        ovr += spd * .25
        ovr += arm * .25
        ovr += fld * .20
    elif pos=='RF':
        ovr += pow * .24
        ovr += con * .14
        ovr += spd * .14
        ovr += arm * .14
        ovr += fld * .34
    elif pos=='SP':
        ovr += vel * .26
        ovr += jnk * .34
        ovr += acc * .40
    elif pos=='RP':
        ovr += vel * .34
        ovr += jnk * .40
        ovr += acc * .26
    elif pos=='CP':
        ovr += vel * .40
        ovr += jnk * .26
        ovr += acc * .34       
    



    list.append(int(ovr))    
    toString(list)


def toString(list):
    p = ['Position','Throw','Bat','Pow','Con','Spd','Fld','Arm','Vel','Jnk','Acc','ovr']
    for i, tup in enumerate(list):
        print(p[i], end=' ')
        print(tup, end=' ')
       

def randArm(pos):
    n = random.randint(1,20)
    if pos=='ath':
        return 'Right' if n<=15 else 'Left'
    elif pos=='C':
        return 'Right' if n<20 else 'Left'
    elif pos=='2B' or pos=='3B' or pos=='SS':
        return 'Right' if n<=17 else 'Left'
    else:
        return 'Right' if n<=12 else 'Left'

def randBat(arm):
    n = random.randint(1,20)
    if arm=='Right': n-=2
    else: n+=2

    if n<=8: return 'Right'
    elif n<=16: return 'Left'
    else: return 'Switch'
    
def stats(l):
    if l=='S': return random.randint(76,88)
    elif l=='A': return random.randint(68,80)
    elif l=='B': return random.randint(60,72)
    elif l=='C': return random.randint(54,66)
    elif l=='D': return random.randint(46,58)
    else: return random.randint(1,30)

def create_ath():
    pos = input("What is the player's position: ")
    pow = input("What is the player's power: ")
    con = input("What is the player's contact: ")
    spd = input("What is the player's speed: ")
    fld = input("what is the player's fielding: ")
    arm = input("What is the player's arm: ")
    vel = input("What is the player's velocity: ")
    jnk = input("What is the player's Junk: ")
    acc = input("What is the player's Accuracy: ")
    throw = randArm('ath')
    bat = randBat(throw)
    pow = stats(pow)
    con = stats(con)
    spd = stats(spd)
    fld = stats(fld)
    arm = stats(arm)
    vel = stats(vel)
    jnk = stats(jnk)
    acc = stats(acc)
    list = [pos,throw,bat,pow,con,spd,fld,arm,vel,jnk,acc]
    ovr(list)

def create_bat():
    pos = input("What is the player's wanted position: ")
    pow = input("What is the player's power: ")
    con = input("What is the player's contact: ")
    spd = input("What is the player's speed: ")
    fld = input("what is the player's fielding: ")
    arm = input("What is the player's arm: ")
    throw = randArm(pos)
    bat = randBat(throw)
    pow = stats(pow)
    con = stats(con)
    spd = stats(spd)
    fld = stats(fld)
    arm = stats(arm)
    list = [pos,throw,bat,pow,con,spd,fld,arm,0,0,0]
    ovr(list)

def create_pit():
    pos = input("Waht does your player pitch: ")
    pow = input("What is the player's power: ")
    con = input("What is the player's contact: ")
    spd = input("What is the player's speed: ")
    fld = input("what is the player's fielding: ")
    vel = input("What is the player's velocity: ")
    jnk = input("What is the player's Junk: ")
    acc = input("What is the player's Accuracy: ")
    throw = randArm('p')
    bat = randBat(throw)
    pow = stats(pow)
    con = stats(con)
    spd = stats(spd)
    fld = stats(fld)
    vel = stats(vel)
    jnk = stats(jnk)
    acc = stats(acc)
    list = [pos,throw,bat,pow,con,spd,fld,0,vel,jnk,acc]
    ovr(list)

def get_traits(list):
    l = []
    for i in list:
        if i == 'A': n = random.randint(1,3)
        elif i is 'B': n = random.randint(1,4)
        elif i is 'C': n=random.randint(2,5)
        elif i is 'D': n=random.randint(2,6)
        elif i is 'F': n=random.randint(3,7)
        else: n=random.randint(1,6)
        if n == 1: l.append('S')
        elif n==2: l.append('A')
        elif n==3: l.append('B')
        elif n==4: l.append('C')
        elif n==5: l.append('D')
        else: l.append('F')
    print(l)

def new_player():
    pos = input("What is the player's wanted position: ")
    r = randArm(pos)
    print(randArm(pos), end=' ')
    print(randBat(r))
    if pos=='C': l = ['C','C','F','A','A']
    elif pos=='1B': l = ['A','C','F','D','D']
    elif pos=='2B': l = ['D','A','B','B','C']
    elif pos=='3B': l = ['A','C','C','B','A']
    elif pos=='SS': l = ['C','B','B','B','B']
    elif pos=='LF': l = ['C','A','C','C','C']
    elif pos=='CF': l = ['D','B','A','A','B']
    elif pos=='RF': l = ['B','C','C','C','A']
    elif pos=='P': l = ['F','F','F','F','U','U','U']
    else: l = ['U','U','U','U','U','U','U','U']
    get_traits(l)

def pot():
    n = int(input("How many pot do you want to caluate: "))
    while n > 0:
        p = random.randint(0,4)
        if p==0:
            print('A', end=' ')
        elif p==1:
            print('B', end=' ')
        elif p==2:
            print('C', end=' ')
        elif p==3:
            print('D', end=' ')
        else: print('F', end=' ')
        n -= 1
        


def main():
    t = True    
    while(t):
        d = input("What type of player are you estimating(A/B/P/N): ")
        if d is 'P' or d is 'p': create_pit()
        elif d is 'B' or d is 'b': create_bat()
        elif d is 'A' or d is 'a': create_ath()
        elif d is 'N' or d is 'n': new_player()
        elif d is 'R' or d is 'r': print(random.randint(0,5))
        elif d is 'T' or d is 't': pot()


        print()
        
        n = input("Enter negative int to stop program: ")
        if int(n)<0: t=False

main()