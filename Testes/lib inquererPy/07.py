# keybindings
from InquirerPy.resolver import prompt

keybindings = {
    "skip": [{"key": "c-c"}], # ctrl + c skip
    "interrupt": [{"key": "c-d"}], # ctrl + d interrompe e para o programa
    "toggle-all": [{"key": ["c-a", "space"]}], # se apertar o espaço vc consegue selecionar mais de um e se apertar ctrl + a vc selecioa tudo
}

result = prompt(
    questions=[
        {
            "type": "list",
            "message": "Select one:",
            "choices": ["Fruit", "Meat", "Drinks", "Vegetable"],
            "multiselect": True
        },
    ],
    keybindings=keybindings, # declara as keybings
)