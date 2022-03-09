import random
from math import floor

class Character:
    def __init__(self, id, name, stats_dict, al):
        self.id = id
        self.name = name
        # hay muchos superheroes con stats null, se reemplazarán con 0
        for k in stats_dict:
            if stats_dict[k] == 'null':
                stats_dict[k] = 0
        # "base modificada de cada stat", luego se aplicará el bonus de equipo
        self.intelligence = (2*int(stats_dict['intelligence']) + random.randint(0,10))/1.1
        self.strength = (2*int(stats_dict['strength']) + random.randint(0,10))/1.1
        self.speed = (2*int(stats_dict['speed']) + random.randint(0,10))/1.1
        self.durability = (2*int(stats_dict['durability']) + random.randint(0,10))/1.1
        self.power = (2*int(stats_dict['power']) + random.randint(0,10))/1.1
        self.combat = (2*int(stats_dict['combat']) + random.randint(0,10))/1.1
        # data auxiliar
        self.alignment = al
        self.hp_mod_AS = (1+random.randint(0,10)/10)
    
    # Se considera que se usan los stats "reales" para calcular el hp
    # Hay heroes 'neutral', no se les aplicará ni buff ni debuff
    def apply_team_bonus(self, team_alignment):
        if team_alignment == self.alignment:
            self.FB = 1+random.randint(0, 9)
        elif self.alignment == 'neutral':
            self.FB = 1
        else:
            self.FB = (1+random.randint(0, 9))**(-1)
        
        self.intelligence = floor(self.intelligence*self.FB)
        self.strength = floor(self.strength*self.FB)
        self.speed = floor(self.speed*self.FB)
        self.durability = floor(self.durability*self.FB)
        self.power = floor(self.power*self.FB)
        self.combat = floor(self.combat*self.FB)
        self.hp = floor((self.strength*0.8 + self.durability*0.7 + self.power)*self.hp_mod_AS/2) + 100
        self.full_hp = self.hp

    def atacar(self):
        ataque = random.choice([self.mental, self.strong, self.fast])
        return ataque()

    def mental(self):
        daño = (self.intelligence*0.7 + self.speed*0.2+ self.combat*0.1)*self.FB
        print(f"{self.name} ha usado ataque mental!")
        print(f"Inflige {daño} de daño!")
        return daño

    def strong(self):
        daño = (self.strength*0.6 + self.power*0.2+ self.combat*0.2)*self.FB
        print(f"{self.name} ha usado ataque strong!")
        print(f"Inflige {daño} de daño!")
        return daño

    def fast(self):
        daño = (self.speed*0.55 + self.durability*0.25+ self.strength*0.2)*self.FB
        print(f"{self.name} ha usado ataque fast!")
        print(f"Inflige {daño} de daño!")
        return daño

    def reset_health(self):
        self.hp = self.full_hp

    def __repr__(self):
        return f'{self.name} [{self.hp}/{self.full_hp}]'

if __name__ == "__main__":
    a = ['Professor Zoom'
    ,{'intelligence': '94', 'strength': '10', 'speed': '100', 'durability': '20', 'power': '83', 'combat': '20'}
    ,'bad']

    c = Character(1, a[0], a[1], a[2])
    c.apply_team_bonus('bad')
    print(c)
    c.atacar()