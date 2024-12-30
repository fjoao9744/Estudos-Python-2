# auto-completar

from InquirerPy.resolver import prompt
from InquirerPy.validator import NumberValidator

def main():
    questions = [
        {"type": "input", "message": "Qual seu nome:"},
        {
            "type": "input",
            "message": "Qual empresa você deseja trabalhar:",
            "completer": { # o auto-completar
                "Google": None,
                "Facebook": None,
                "Amazon": None,
                "Netflix": None,
                "Apple": None,
                "Microsoft": None,
                "Smogon": None
            },
            "multicolumn_complete": True,
        },
        {
            "type": "input",
            "message": "qual sua expectativa salarial(k):",
            "transformer": lambda result: f"{result}k", #vai rodar antes do result ser mostrado
            "filter": lambda result: int(result) * 1000, # esse é o valor real da variavel
            "validate": NumberValidator(), # verifica se é um numero
        },
    ]

    result = prompt(questions)
    print(result)

if __name__ == "__main__":
    main()