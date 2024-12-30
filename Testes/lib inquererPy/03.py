from InquirerPy.resolver import prompt

perguntas = [
    {"type": "confirm", 
    "message": "Confirm?"
    }
]
result = prompt(perguntas)