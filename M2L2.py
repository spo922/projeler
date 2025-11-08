
import discord 
from discord.ext import commands 
import os
import random
import requests

intents = discord.Intents.default()  
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event 
async def on_ready(): 
    print(f'{bot.user} olarak giriş yaptık') 

@bot.command() 
async def hello(ctx): 
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
@bot.command() 

async def yardim(ctx): 
    await ctx.send(f'Üzgünüm :sob: böyle bir konuda sana yardımcı olamam. https://discordapp.com/channels/1426830868634144790/1426831600511094804 ama burdan yardım desteği alabilirsin!')
    

@bot.command()
async def joined(ctx, member: discord.Member):  
    """Bir kişinin sunucuya ne zaman katıldığını söyler."""

    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
  

@bot.command()
async def meme(ctx):
    files = os.listdir('images')
    selected_file = random.choice(files)
    with open(f'images/{selected_file}', 'rb' )as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('ordek')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_wolf_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('kopke')
async def anime(ctx):
    '''anime komutunu çağırdığımızda, program wolf_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_wolf_image_url()
    await ctx.send(image_url)

bot.run("tokenime bakma")
