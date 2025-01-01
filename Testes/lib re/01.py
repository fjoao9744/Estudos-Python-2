import re
string = "eu amo smogon"

busca = re.search("smogon", string) # faz uma busca

print(busca)

if busca:
    print("tem smogon na frase")
else:
    print("Não tem smogon na frase")