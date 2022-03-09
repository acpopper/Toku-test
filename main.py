import requests
from clases import Character
from data import API_KEY
import random
from math import floor

num_superheroes = 731
# res = requests.get(f"https://superheroapi.com/api/{API_KEY}/{random.randint(1, num_superheroes)}")
# print(res.json()['id'])
# print(res.json()['name'])
# print(res.json()['powerstats'])
# print(res.json()['biography']['alignment'])

def simulation():
    team_a = {'team': [], 'alignment': 'bad'}
    team_b = {'team': [], 'alignment': 'bad'}
    drafts = set()
    # seleccionamos id's que no se repitan
    while len(drafts) < 10:
        drafts.add(random.randint(1, num_superheroes))
    
    # poblamos los equipos
    team_a_al = 0
    team_b_al = 0
    for i, hero in enumerate(drafts):
        personaje = requests.get(f"https://superheroapi.com/api/{API_KEY}/{hero}").json()
        if i < len(drafts)/2:
            team_a['team'].append(Character(personaje['id'], personaje['name'], personaje['powerstats'], personaje['biography']['alignment']))
            if personaje['biography']['alignment'] == 'good':
                team_a_al += 1
                if team_a_al == 3:
                    team_a['alignment'] = 'good'

        else:
            team_b['team'].append(Character(personaje['id'], personaje['name'], personaje['powerstats'], personaje['biography']['alignment']))
            if personaje['biography']['alignment'] == 'good':
                team_b_al += 1
                if team_b_al == 3:
                    team_b['alignment'] = 'good'

    for i in team_a['team']:
        i.apply_team_bonus(team_a['alignment'])
    for i in team_b['team']:
        i.apply_team_bonus(team_b['alignment'])
    print('Team A')
    for i in team_a['team']:
        print(i)
    print('Team B')
    for i in team_b['team']:
        print(i)


if __name__ == "__main__":
    simulation()