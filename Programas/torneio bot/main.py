from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import pandas as pd

# permissões(intents) que o bot vai ter
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia  mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

bot = commands.Bot(command_prefix="! ", intents=intents)

# Evento que ocorre quando o bot se conecta ao Discord
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    
@bot.command()
async def pontos(ctx):
    df = pd.DataFrame({
        "Smogon": [0],
        "JF": [0],
        "Giovana": [0],
        "Kédao kook": [0]
        })

    # Converte o DataFrame para string
    df = df.to_string(index=False)
    
    await ctx.send(f"```\n{df}\n```")
    
load_dotenv() 
token = os.getenv("DISCORD_BOT_TOKEN_TEST") 

bot.run(token)