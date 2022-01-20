import csv

import requests
import hashlib
from fake_useragent import UserAgent
from constants import buffer_filename, url

ua = UserAgent()
resp = requests.get(url, headers={'user-agent': ua.google}).json()
sports = list(filter(lambda x: x['name'].find('Футбол') != -1, resp['sports']))
live_games = [game for game in resp['events'] if game['place'] == 'live' and next((x for x in sports if game['sportId'] == x['id']), None) is not None]
out_games = {}
output_fieldnames = ['id', 'gamers']
output = []
for game in live_games:
    if 'team1' not in game or 'team2' not in game:
        continue
    else:
        out_games[hashlib.md5(str(game['id']).encode()).hexdigest()] = f"{game['team1']} - {game['team2']}"
        output.append(
            {
                output_fieldnames[0]: hashlib.md5(str(game['id']).encode()).hexdigest(),
                output_fieldnames[1]: f"{game['team1']} - {game['team2']}"
            })


print(out_games)
with open(buffer_filename, 'w', encoding='UTF-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=output_fieldnames)
    writer.writeheader()
    writer.writerows(output)
