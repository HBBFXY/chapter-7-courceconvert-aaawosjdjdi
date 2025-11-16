import keyword

reserved_words = set(keyword.kwlist)

with open('random_int.py', 'r') as f:
    content = f.read()

result = []
for word in content.split():
    if word.islower() and word not in reserved_words:
        result.append(word.upper())
    else:
        result.append(word)

converted_content = ' '.join(result)

with open('converted_random_int.py', 'w') as f:
    f.write(converted_content)
