from InquirerPy import inquirer # outra sintaxe

name = inquirer.text(message="Qual o seu nome? ").execute()
lang = inquirer.select(message="qual sua linguagem favorita?", choices=["Go", "Python", "Rust", "JavaScript"]).execute()
confirm = inquirer.confirm(message="Confirm?").execute()

print(name, lang, confirm)
