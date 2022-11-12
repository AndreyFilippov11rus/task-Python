import requests
import json


if __name__ == '__main__':
    text = requests.get('https://www.breakingbadapi.com/api/deaths')
    date_death = json.loads(text.text)
    max_death = max(date_death, key=lambda episode: episode["number_of_deaths"])
    with open('death.json', 'w', encoding='utf-8') as file:
        json.dump(max_death, file, indent=4)