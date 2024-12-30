from InquirerPy.resolver import prompt

perguntas = [
    {"type": "list",
    "message": "qual sua linguagem de programação?",
    "choices": ["Python", "C++", "JS", "PHP", "Rubi"],
    }
]

result = prompt(perguntas)

print(result)
print(result[0]) # tem q colocar o zero pq vc recebe um dict com index 0