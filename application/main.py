from character import *
from monster import *
from backstory import *
def lvlUP(Character):
    lvls = {
        2:50,
        3:100,
        4:200,
        5:400}
    if(Character.exp>=lvls[2]):
        Character.level +=1
    if(Character.exp>=lvls[3]):
        Character.level +=1
    if(Character.exp>=lvls[4]):
        Character.level +=1
    if(Character.exp>=lvls[5]):
        Character.level +=1
    return print('Congratulations on the level up!')


def combat(Character,Monster):
    while(Character.hp>0):
        print('Select an action:')
        playerInfo = input()
        if(playerInfo != 'Heroism' and playerInfo != 'Healing wave'):
            if(playerInfo == 'Auto attack'):
                Monster.hp = Monster.hp - (Character.action(playerInfo)+Character.atk)
                Character.hp = Character.hp - Monster.atk
            else:
             Monster.hp = Monster.hp - Character.action(playerInfo)
             Character.hp = Character.hp - Monster.atk
        elif(playerInfo == 'Heroism'):
            Character.atk = Character.atk + Character.action(playerInfo)
            Character.hp = Character.hp - Monster.atk
            print('Char atk:',Character.atk)
        
        elif(playerInfo == 'Healing wave'):
            if(Character.hp>0 and Character.hp<=100):
                Character.hp = Character.hp + Character.action(playerInfo)
                if(Character.hp>100):
                    Character.hp = 100
                Character.hp = Character.hp - Monster.atk
            elif(Character.hp>100):
                Character.hp = 100
                Character.hp = Character.hp - Monster.atk
        # Nqma jivot
        if(Character.hp <=0):
            print(Monster.name,'has killed',Character.name)
            break;
        elif(Monster.hp<=0):
            print(Character.name,'has killed',Monster.name)
            Character.atk = 20
            Character.exp = Character.exp + Monster.expDrop
            print(Character.name,'has earned',Monster.expDrop,'exp')
            lvlUP(Character)
            break;
        print(Character.name,'\'s HP:',Character.hp,'|',Monster.name,'\'s HP:',Monster.hp)



gosho = Character('Gruuz','The Terrible')
gosho.talk()
gosho.setRace('Orc')
print(gosho.name,gosho.title)
print('Frost bolt\'s damage:',gosho.action('Frost bolt'))# vrushta dmg
print(gosho.name,'\'s race:',gosho.race,sep = '')
print('Usable spells/attacks{spell name : damage}:',gosho.spellsName)
print(gosho.name,'\'s HP:',gosho.hp,sep = '')
print(gosho.name,'\'s ATK:',gosho.atk,sep = '')
print(gosho.name,'\'s LV:',gosho.level,sep = '')
print(gosho.name,'\'s EXP:',gosho.exp,sep = '')
Khazduul = Monster('Khazduul','Legion\'s flame')
Khazduul.setRace('Demon')
Khazduul.talk()
print(Khazduul.name,Khazduul.title)
a = Backstory()
a.story(gosho.name,gosho.title)
combat(gosho,Khazduul)
del gosho
del Khazduul
