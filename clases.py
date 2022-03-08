import random
from math import floor

class Character:
    def __init__(self, id, name, stats_dict, al):
        self.id = id
        self.name = name
        # "base modificada de cada stat", luego se aplicará el bonus de equipo
        self.intelligence = (2*int(stats_dict['intelligence']) + random.randint(0,10))/1.1
        self.strength = (2*int(stats_dict['strength']) + random.randint(0,10))/1.1
        self.speed = (2*int(stats_dict['speed']) + random.randint(0,10))/1.1
        self.durability = (2*int(stats_dict['durability']) + random.randint(0,10))/1.1
        self.power = (2*int(stats_dict['power']) + random.randint(0,10))/1.1
        self.combat = (2*int(stats_dict['combat']) + random.randint(0,10))/1.1
        # data auxiliar
        self.alignment = al
        self._FB = 0
        self.hp_mod_AS = (1+random.randint(0,10)/10)
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        pass
    
    # Se considera que se usan los stats "reales" para calcular el hp
    def apply_team_bonus(self, team_alignment):
        if team_alignment == self.alignment:
            self.FB =  1+random.randint(0, 9)
        else:
            self.FB =  (1+random.randint(0, 9))^-1
        
        self.intelligence = floor(self.intelligence*self.FB)
        self.strength = floor(self.strength*self.FB)
        self.speed = floor(self.speed*self.FB)
        self.durability = floor(self.durability*self.FB)
        self.power = floor(self.power*self.FB)
        self.combat = floor(self.combat*self.FB)
        self._hp = floor((self.strength*0.8 + self.durability*0.7 + self.power)*self.hp_mod_AS/2) + 100

    def atacar(self):
        ataque = random.choice([self.mental, self.strong, self.fast])
        return ataque

    def mental(self):
        return (self.intelligence*0.7 + self.speed*0.2+ self.combat*0.1)*self.FB

    def strong(self):
        return (self.strength*0.6 + self.power*0.2+ self.combat*0.2)*self.FB

    def fast(self):
        return (self.speed*0.55 + self.durability*0.25+ self.strength*0.2)*self.FB

