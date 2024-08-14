import json
import csv

from syllables import get_syllables


def find_value_in_dict(val, data):
    for key, lst in data.items():
        if val in lst:
            return key
    return None


with open('data-naver.json', 'r') as file:
    full_data = json.load(file)

syllables = get_syllables()
result = []

for hangul, hanja_list in full_data.items():
    for hanja in hanja_list:
        consonant = find_value_in_dict(hangul, syllables)
        unicode_value = ord(hanja['entryName'])
        hex_value = format(unicode_value, 'x')

        result.append({
            'id': hanja['entryId'],
            'hangul': hangul,
            'consonant': consonant,
            'unicode': hex_value,
            'hanja': hanja['entryName'],
            'meaning': hanja['pron'],
        })

    labels = ['hangul', 'consonant', 'unicode', 'hanja', 'meaning', 'id']

try:
    with open('data-naver.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for ele in result:
            writer.writerow(ele)
except IOError:
    print('I/O error')
