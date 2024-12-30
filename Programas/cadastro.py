import re
from sys import stdout
from InquirerPy.resolver import prompt
from collections import deque

pessoas = deque()
while 1:
    pessoa = prompt(
        [{
        "type": "input",
        "message": "Qual o seu nome? ",
        "name": "name"},
        
        {"type": "list",
        "message": "Qual linguagem de programação você mais usa?",
        "name": "lang",
        "choices": ["python", "C++", "JS", "PHP", "Rubi", "Rust", "Dart", "Java", "C", "Kotlin", "C#"]}
    ])
    pessoa["name"] = str(pessoa["name"]).capitalize().strip()
    pessoa["name"] = re.sub(r'[#+=\-{}\[\]]', '', pessoa["name"])
    pessoas.appendleft(pessoa)
    if not prompt({"type":"confirm", "message":"Deseja continuar?"})[0]: break

stdout.write(f"Os programadores cadastrados foram: {[pessoa['name'] for pessoa in pessoas]}\n")
stdout.write(f"As linguagens cadastradas foram: {set([lang['lang'] for lang in pessoas])}")

class num:
    int: int

def coisar(num: num):
    print(num)
    
    
    