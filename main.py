import requests
from data import API_KEY, Character
import random

res = requests.get(f"https://superheroapi.com/api/{API_KEY}/{random.randint(1, 731)}")



if __name__ == "__main__":
    print(res.json()['name'])
    print(res.json()['powerstats'])
    print(res.json()['biography']['alignment'])