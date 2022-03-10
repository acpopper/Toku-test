from time import sleep
from pyrsistent import T
import requests
from clases import Character
from data import API_KEY, mailgun_api
import random
from math import floor

num_superheroes = 731
# res = requests.get(f"https://superheroapi.com/api/{API_KEY}/{random.randint(1, num_superheroes)}")
# print(res.json()['id'])
# print(res.json()['name'])
# print(res.json()['powerstats'])
# print(res.json()['biography']['alignment'])

def build_teams():
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
    
    return team_a, team_b

def simulacion(team_a, team_b, email=None):
    team_a['defeated'] = False
    team_b['defeated'] = False
    pa = 0
    pb = 0
    player_a = team_a['team'][pa]
    player_b = team_b['team'][pb]

    print(' '*10 + '-- INICIA LA PELEA!! --')
    print('Equipo A' + ' '*10 + 'vs' + ' '*10 + 'Equipo B')
    for i in range(0, 5):
        print(f"{team_a['team'][i]} -- {team_b['team'][i]}")
    print('\n \n')

    ronda = 1
    turno = 1
    results = 'Resultados peleas\n'
    while not team_a['defeated'] or not team_b['defeated']:
        print(f'Ronda {ronda}--Turno {turno}')
        player_b.recibir_daño(player_a.name, player_a.atacar())
        if player_b.hp == 0:
            print(f"{player_a.name} ha derrotado a {player_b.name}")
            results + f'Ronda {ronda}: {player_a.name} (winner) vs {player_b.name}\n'
            ronda += 1
            pb += 1
            if pb < 5:
                player_b = team_b['team'][pb]
                player_a.reset_health()
            else:
                team_b['defeated'] = True
        
        sleep(1)
        player_a.recibir_daño(player_b.name, player_b.atacar())
        if player_a.hp == 0:
            print(f"{player_b.name} ha derrotado a {player_a.name}")
            results + f'Ronda {ronda}: {player_a.name} vs {player_b.name} (winner)\n'
            ronda += 1
            pa += 1
            if pa < 5:
                player_a = team_a['team'][pa]
                player_b.reset_health()
            else:
                team_a['defeated'] = True
        
        sleep(1)
        
            

    
    pass

def send_simple_message(to):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox62fd7184edf44a54ad96e60f670bc76d.mailgun.org/messages",
		auth=("api", mailgun_api),
		data={"from": "Alan Popper <acpopper@uc.cl>",
			"to": to,
			"subject": "Resultado simulación",
			"text": ""})


if __name__ == "__main__":
    A, B = build_teams()
    simulacion(A, B)