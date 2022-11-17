import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

resp = requests.get(url).json()

list_heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], resp))
intel_heroes = {}
for hero in list_heroes:
    intel_heroes[hero['name']] = hero['powerstats']['intelligence']

super_hero = max(intel_heroes, key=intel_heroes.get)

print('Самый умный герой:', super_hero)