import json
import csv

from syllables import get_syllables


def find_value_in_dict(val, data):
    for key, lst in data.items():
        if val in lst:
            return key
    return None


with open('data-gov.json', 'r') as file:
    full_data = json.load(file)

syllables = get_syllables()
result = []
# single_char = []

for data in full_data:
    hangul = data['ineum']
    consonant = find_value_in_dict(hangul, syllables)

    hex_string = data['cd']
    unicode_value = int(hex_string, 16)
    hanja = chr(unicode_value)

    result.append({
        'hangul': hangul,
        'consonant': consonant,
        'unicode': hex_string,
        'hanja': hanja,
    })
    # single_char.append(hanja)

labels = ['hangul', 'consonant', 'unicode', 'hanja']

try:
    with open('data-gov.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for ele in result:
            writer.writerow(ele)
except IOError:
    print('I/O error')
