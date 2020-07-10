import requests
import re

input = ['f','i','t','u','d','c','l']

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "e6c04543b8mshb20abe55a63ac78p179ebbjsn371b9f80cb32"
    }

li = []

def appendz(response, li):
    for word in response.json()['results']['data']:
        li.append(word)
    return li


def get_list(input, li):
    for letter in input:
        for n in range(4, 8):
            s = "?letterPattern=^" + letter + ".{" + str(n) + "}$"
            url = f"https://wordsapiv1.p.rapidapi.com/words/" + s
            response = requests.request("GET", url, headers=headers)
            appendz(response, li)


    return li

print(get_list(input, li))

def get_words(chars_seq, words_seq=li):
    s_chars = ''.join(chars_seq)
    s_pat = r'\b[' + s_chars + r']+\b'
    pat = re.compile(s_pat)
    return [word for word in words_seq if pat.match(word)]

chosen_words = get_words(input)
mandatory_letter = input[6]

print(chosen_words)

chosen_words = [word for word in chosen_words if mandatory_letter in word and '-' not in word and ' ' not in word and '\'' not in word]