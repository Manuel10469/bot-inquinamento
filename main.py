import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\/accesso come {bot.user}')

materiali = {
    'plastica':('la plastica è il materiale più problematico perchè disperde microplastiche e ci mette dai 100 ai 1000 anni per decomporsi'),
    'carta':('la carta ci mette circa 4 settimane e, essendo fatta dagli alberi, non ha un grande impatto ambientale, è comunque meglio riciclarla o riutilizzarla'),
    'alluminio':('anche l alluminio può essere un problema non da poco se disperso in giro, dato che ci mette circa 100 anni a decomporsi lasciando sostanze inquinanti'),
    'vetro':('il vetro è il materiale con il tempo di decomposizione più alto (4000 anni) e, sebbene non rilascia sostanze particolarmente inquinanti può dare problemi')
    }

@bot.command()
async def ciao(ctx):
    await ctx.send('Ciao, sono un bot che può aiutarti a conoscere l inquinamento.')

@bot.command()
async def comandi(ctx):
    await ctx.send('Scrivi "info" e poi un materiale (es. plastica) e ti darò una descrizione utile!')
    
@bot.command()
async def info(ctx, materiale: str):
    if materiale in materiali:
        scelta = materiali[materiale]
        await ctx.send(scelta)
    else:
        await ctx.send('questo materiale purtroppo non è presente nella lista, se pensi sia importante puoi contattare il mio creatore')

bot.run("TOKEN")