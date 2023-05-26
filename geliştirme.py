import discord
from discord.ext import commands
import time
import random
import string

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def toplama(ctx, arg1, arg2):
    sayi1 = int(arg1)
    sayi2 = int(arg2)
    toplam = sayi1 + sayi2
    await ctx.send(f'Birinci sayi: {arg1}, Ikinci sayi: {arg2}, Toplam: {toplam}')

@bot.command()
async def cikarma(ctx, arg6, arg7):
    sayi6 = int(arg6)
    sayi7 = int(arg7)
    fark = sayi6 - sayi7
    await ctx.send(f'Birinci sayi: {arg6}, Ikinci sayi: {arg7}, fark: {fark}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yamukalanbilgi(ctx):
    await ctx.send("yanda verilen sıraya göre verileri giriniz: 1.Üst kenar 2. Alt kenar 3.Yükseklik")

@bot.command()
async def yamukalan(ctx, arg3, arg4, arg5):
    sayi3 = int(arg3)
    sayi4 = int(arg4)
    sayi5 = int(arg5)
    alan = ((sayi3 + sayi4)*sayi5)/2
    await ctx.send(f'Birinci sayi: {arg3}, Ikinci sayi: {arg4}, Toplam: {alan}')

@bot.command()
async def sifreolusturucu(ctx):
    await ctx.send("Lütfen bekleyiniz .Şifreniz oluşturuluyor ...")
    time.sleep(5)
    harf1= (random.choice(string.ascii_letters))
    harf2= (random.choice(string.ascii_letters))
    harf3= (random.choice(string.ascii_letters))
    buyukHarf = chr(random.randint(ord('A'), ord('z')))
    sayi1=(random.randint(1000,10000))
    sayi2=(random.randint(10,100))
    sayi3=(random.randint(100,1000))
    sifre = harf1+str(sayi1)+harf2+str(sayi2)+buyukHarf+str(sayi3)
    await ctx.send(sifre)


bot.run("token burada olacak")
