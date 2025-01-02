from InquirerPy.resolver import prompt
import sys

def escolha(msg, escolhas: list[str]):
    return prompt({"type": "list", "message": msg, "choices": escolhas})[0]

smog = escolha("escolha um smogon", ["2x", "3x", "4x"])

sys.stdout.write(str(smog))



