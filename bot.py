import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
#prefix 
bot = commands.Bot(command_prefix="!", intents=intents)

#Bot online olduğu zaman print fonksiyonu ile bunu belirtelim
@bot.event
async def on_ready():
  print("Burayı kişileştirebilirsiniz.")

#Gelen mesajları algılama ve yanıtlama başlarında prefix olması lazım
@bot.command()
async def sa(msg):
  await msg.reply("as")
#Biz burada "reply" kullanarak mesajı yanıtlayarak gönderdik

@bot.command()
async def merhaba(msg):
  await msg.send("Merhaba!")
#burada mesajı yanıtlamadan direk mesaj gönderiyoruz

bot.run("Buraya botun tokenini yazın")



  
  
  
