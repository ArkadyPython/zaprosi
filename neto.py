import requests
heroes_man = ['Hulk', 'Captain America', 'Thanos']
heroes_man_dict = {}
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url).json()
for name in heroes_man:
    for hero in resp:
        if hero['name'] == name:
            heroes_man_dict[name] = hero['powerstats']['intelligence']
print(max(heroes_man_dict, key=heroes_man_dict.get))
