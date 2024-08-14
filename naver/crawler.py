import requests
import json
import time

from syllables import get_syllables

syllables = get_syllables()

base_url = 'https://hanja.dict.naver.com/api/cckodict/ko/ccko/getCategoryNameSearchList'

result = {}

num_chars = 0
for consonant, hangul_list in syllables.items():
    for hangul in hangul_list:
        for page in range(1, 5):
            time.sleep(1)
            params = {
                'category1': 'name',
                'category2': consonant,  # You may need to decode these characters
                'category3': hangul,
                'page': str(page)
            }
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data['m_items']:
                    if hangul not in result.keys():
                        result[hangul] = data['m_items']
                    else:
                        result[hangul].extend(data['m_items'])

                    with open('data-naver.json', 'w') as file:
                        json.dump(result, file, indent=4)
                        num_chars += len(data['m_items'])
                        print(f"{consonant} / {hangul} (P.{page})  +{len(data['m_items'])} / Total {num_chars}")
                else:
                    break
            else:
                print(f'Request failed with status code {response.status_code}')
    print('-' * 20)
