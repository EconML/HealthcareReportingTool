import random



def primary():
    dic = {}
    assult = [['Kile 141',44,88],
              ['FAL',89,133],
              ['M4A1',134,177],
              ['FR 5.56',178,221],
              ['Oden',222,265],
              ['M13',267,311],
              ['FN Scar 17',312,355],
              ['AK-47',356,400]]
    dic['assult'] = []
    for i in assult:
        dic['assult'].append(i)
        
    submachine = [['AUG',41,83],
                  ['P90',84,126],
                  ['MP5',127,169],
                  ['Uzi',170,212],
                  ['PP19 Bixon',213,256],
                  ['MP7',257,300]]
    dic['submachine'] = []
    for i in submachine:
        dic['submachine'].append(i)
        
    shotguns = [['Model 680',80,160],
                ['R9-O Shotgun',161,240],
                ['725',241,320],
                ['Orgin 12 Shotgun',321,400]]
    dic['shotguns'] = []
    for i in shotguns:
        dic['shotguns'].append(i)
        
    lmg = [['PKM',100,200],
           ['SA87',201,300],
           ['M91',301,400],
           ['MG34',401,500]]
    dic['lmg'] = []
    for i in lmg:
        dic['lmg'].append(i)
    
    marksman = [['EBR-14',87,174],
                ['MK2 Carbine',175,261],
                ['Kar98k',262,350]]
    dic['marksman'] = []
    for i in marksman:
        dic['marksman'].append(i)
        
    sniper = [['Dragunov',112,224],
              ['HDR',225,336],
              ['AX-50',337,450]]
    dic['sniper'] = []
    for i in sniper:
        dic['sniper'].append(i)
        
    melee = [['Riot Shield',20,100],
             ['Riot Shield',20,100]]
    dic['melee'] = []
    for i in melee:
        dic['melee'].append(i) 
    return dic
    
   
def secondary():
    dic = {}
    
    pistol = [['X16',33,66],
              ['1911',67,99],
              ['.357',100,132],
              ['M19',133,165],
              ['.50 GS',167,200]]
    dic['pistol'] = []
    for i in pistol:
        dic['pistol'].append(i)
        
    launcher = [['PILA',50,100],
                ['Strela-P',101,150],
                ['JOKR',151,200],
                ['RPG-7',201,250]]
    dic['launcher'] = []
    for i in launcher:
        dic['launcher'].append(i)
    

    melee = [['combat knife',0,20],
         ['combat knife',0,20]]
    dic['melee'] = []
    for i in melee:
        dic['melee'].append(i) 
    return dic;
    
    
def attachments():
    dic = {}
    main = [['Muzzle',20,80],
            ['Barrel',20,80],
            ['Laser',10,70],
            ['Optic',40,100],
            ['Stock',20,80],
            ['Underbarrel',20,80],
            ['Ammunition',30,90],
            ['Rear Grip',10,70],
            ['Perk',50,110]]
    dic['attachments'] = []
    for i in main:
        dic['attachments'].append(i)
    
    return dic
    
    
def gernade():
    dic = {}
    lethal = [['Claymore',176,200],
              ['Frag',101,125],
              ['Molotov',76,100],
              ['C4',201,225],
              ['Semtex',126,150],
              ['Throwing knife',50,75],
              ['Proximity Mine',226,250],
              ['Thermite',151,175]]
    dic['lethal'] = []
    for i in lethal:
        dic['lethal'].append(i)
        
    tacitcal = [['Flash',51,75],
                ['Stun',25,50],
                ['Smoke',76,100],
                ['Snapshot',101,125],
                ['Heartbeat',151,175],
                ['Gas',126,150],
                ['Stim',176,200],
                ['Decoy',201,225]]
    dic['tactical'] = []
    for i in tacitcal:
        dic['tactical'].append(i)
        
    return dic
    
def killstreak():
    dic = {}
    killstreak = [['3 Kills',100,200],
                  ['4 Kills',201,300],
                  ['5 Kills',301,400],
                  ['7 Kills',401,500],
                  ['8 Kills',501,600],
                  ['10 Kills',601,700],
                  ['11 Kills',701,800],
                  ['12 Kills',801,900],
                  ['15 Kills',901,1000]]    
    dic['killstreak'] = []
    for i in killstreak:
        dic['killstreak'].append(i)
        
    return dic    
    
def game():
    gamemode = ['team deathmatch',
                'domination',
                'free for all',
                'headquarters',
                'hardpoint',
                'search and destroy',
                'cyber attack',]
    
    maps = ['Shoot House',
            'Azhir Cave',
            'Grazna Raid',
            'Hackney Yard',
            'Arkolv Pear',
            'Gun Runner',
            'Euphrates Bridge',
            'Aniyah Palace',
            'St. Petrograd',
            'Hills',
            'King',
            'Pine',
            'Rammaza',
            'Speedball',
            'Stack',
            'Gulag Showers',
            'Docks',
            'Arklov Peak',
            'Axhir Cave (Night)',
            'Gun Runner (Night)',
            'Hackney Yard (Night)',
            'Rammaza (Night)']
 

    
    g = gamemode[random.randint(0,len(gamemode)-1)]
    m = maps[random.randint(0,len(maps)-1)]
    
    enemy = random.randint(1,6)
    friendly = random.randint(0,5)
    difficulty = ['Recruit',
                  'Regular',
                  'Harened',
                  'Realistic',
                  'Mixed']
    
    dif = difficulty[random.randint(0,len(difficulty)-1)]
    
   
    if random.randint(1,5)==5:
        reward = str(random.randint(10,30)) + ' percent'
    elif random.randint(1,5)>=4:
        reward = 'Personal'
    else:
        reward = 'none'
        
    print('Mission is on ', m)
    print('Thier are ', friendly, ' friendlys and ', enemy, ' enemies on ', dif, ' difficulty')
    print('Reward ', reward)
   
    
    
    
def main():
    dic = {}
    dic['primary'] = primary()
    dic['secondary'] = secondary()
    dic['attachment'] = attachments()
    dic['gernade'] = gernade()
    dic['killstreak'] = killstreak()
    
    
    for i in range(3):
        game()
        print()

    
    
    
   
    for i in dic:
        n = random.randint(0,len(dic[i])-1)
        match = 0
        for i2 in dic[i]:
            if match==n:
                n = random.randint(0,len(dic[i][i2])-1)
                match = 0
                for i3 in dic[i][i2]:
                    if match==n:
                            temp = i3
                            print(temp[0], 'for $', random.randint(temp[1],temp[2]))
                    match +=1
                match += 1
            else:
                match += 1
                
    print('perk $',random.randint(50,100))
        
        
    
    
main()

