import re

string2 = "smogon amo você"

busca = re.search("smogon", string2) # verifica se tem smogon na frase
busca2 = re.search("^smogon", string2) # verifica se tem smogon no começo da frase
busca3 = re.search("smogon$", string2) # verifica se tme smogon no final da frase

print(busca)
print(busca2)
print(busca3)


