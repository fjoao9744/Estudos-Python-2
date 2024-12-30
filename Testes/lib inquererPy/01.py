from InquirerPy.resolver import prompt

perguntas = [
    {"type": "input", # tipo da pergunta
    "message": "qual o seu nome?", # oq vai ser perguntado
    "name":"name"} # variavel q vai a resposta
]

result = prompt(perguntas)

print(result)