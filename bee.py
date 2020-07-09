import re
input = ['n','l','a','f','d','w','i']

words = ['wind', 'find', 'law', 'fill', 'falda', 'naal', 'liw', 'wil']


def get_words(chars_seq, words_seq=words):
    s_chars = ''.join(chars_seq)
    s_pat = r'\b[' + s_chars + r']+\b'
    pat = re.compile(s_pat)
    return [word for word in words_seq if pat.match(word)]


chosen_words = get_words(input)
mandatory_letter = input[6]

print(chosen_words)
chosen_words = [word for word in chosen_words if mandatory_letter in word and len(word)>3]

print(chosen_words)
