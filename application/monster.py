from random import *
class Monster:
    hp = 450
    atk = 25
    expDrop = 50
    
    def __init__(self,name,title):
        self.name=name
        self.title=title
    def setRace(self,race):
        self.race=race
    def talk(self):
        quote = {
            0:'MRLGLRLGLLRLLLRGGRLR',
            1:'DIE!',
            2:'Galtak Ered\'nash',
            3:'Shaza-kiel!',
            4:'From this seal shall arise the doom of men',
            5:'Who, in their arrogance, sought to wield our fire as their own.',
            6:'Now they shall be consumed by the very flame they sought to control.',
            7:'Blindly they build their kingdoms upon stolen knowledge and conceit.',
            8:'Let the echoes of doom resound across this wretched world, that all who live may hear them and despair.',
            9:'Please end my suffering.',
            10:'You too shall fall under my control!',
            11:'Surrender!',
            12:'The rats dare to approach me?'}
        a = randint(0,12)
        return print(quote[a])
    def __del__(self):
        print(self.name,'has died.')
    
        
