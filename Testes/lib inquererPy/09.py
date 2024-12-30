from InquirerPy import inquirer

result = inquirer.text(message="FooBoo:", multiline=True).execute() # poder digitar em multi linhas

print(result)