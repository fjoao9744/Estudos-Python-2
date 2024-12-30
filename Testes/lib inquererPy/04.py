from InquirerPy.resolver import prompt # sintaxe basica

perguntas = [
    {"type": "input", 
    "message": "qual o seu nome?", 
    "name":"name"},
    {"type": "list",
    "message": "qual sua linguagem de programação?",
    "choices": ["Python", "C++", "JS", "PHP", "Rubi"],
    },
    {"type": "confirm", 
    "message": "Confirm?"
    }
]

result = prompt(perguntas)

print(result)