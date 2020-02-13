from random import *
class Character:
    hp = 100
    atk = 20
    level = 1
    exp = 0
    def __init__(self,name,title):
        self.name=name
        self.title=title
    def talk(self):
        quote = {
            0:'Hello!',
            1:'Who should I kill?',
            2:'What do you want?',
            3:'I hear voices.',
            4:'Something need doing?',
            5:'I can do that',
            6:'Ready to work.',
            7:'May my ancestors watch over me.',
            8:'Taz\'dingo!'}
        a = randint(0,8)
        return print(quote[a])
    def action(self,spellName):
        spells = {
            'Frost bolt':100,#name/dmg
            'Fire bolt':120,
            'Arcane blast':80,
            'Kill shot':150,
            'Heroic strike':40,
            'Sinister strike':60,
            'Shadow bolt':110,
            'Healing wave':55,#heal
            'Heroism':15,#buffAtk
            'Auto attack':20}
        self.spellsName=spells
        return spells[spellName]

    def setRace(self,race):
        self.race = race

    def __del__(self):
        print(self.name,"has died.")
