
# ()        \1   
# () ()     \1 \2
# (())()    \1 \2 \3


import re
from pprint import pprint

texto = '''
<p>Frase 1 </p> <p>Frase 2 </p> <p>Frase 3 </p> <div>Frase 4 </div>
'''

# tags = re.findall(r'(<([pdiv]{,3})>.+?<\/\2>)', texto)

# tags = re.findall(r'(<([pdiv]{,3})>(.+?)<\/\2>)', texto) 

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))

# exemplo de saida 1
# for tag in tags:
#     print(tag)

# exemplo de saida 2
# for tag in tags:
#     um, dois = tag
#     print(um, dois)

# exemplo de saida 3 - pprint
# pprint(tags)

# exemplo de saida 4
# for tag in tags:
#     um, dois, tres = tag
#     print(tres)

# ip = '20.254.12.2'
# print(*re.findall(r'[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}', ip))