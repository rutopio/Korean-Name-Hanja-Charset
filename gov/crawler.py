import requests
import json
import time

from syllables import get_syllables

syllables = get_syllables()

base_url = 'https://efamily.scourt.go.kr/webhanja/whjsearch'

result = []

for consonant, hangul in syllables.items():
    for char in hangul:
        unicode_value = ord(char)
        hex_value = format(unicode_value, 'x')
        time.sleep(1)
        params = {
            'mode': 'listUnicodeByKsnd',
            'ksnd': hex_value,
            'ext': '0',
            'pgmode': '1',
            'pgno': '1',
            'pgsize': '10000',
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['resultlist']:
                result.extend(data['resultlist'])
                with open('data-gov.json', 'w') as file:
                    json.dump(result, file, indent=4)
                    print(f"{consonant} / {char} ({hex_value}) +{len(data['resultlist'])} / Total {len(result)}")
            else:
                break
        else:
            print(f'Request failed with status code {response.status_code}')
    print('-' * 20)
