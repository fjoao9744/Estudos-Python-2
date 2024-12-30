from InquirerPy import prompt

completer = {
    "hello": {
        "world": None
    },
    "foo": {
        "boo": None # auto completar do auto completar
    },
    "fizz": {
        "bazz": None
    }
}

questions = [
    {
        "type": "input",
        "message": "FooBoo:",
        "completer": completer
    }
]

result = prompt(questions=questions)
print(result)