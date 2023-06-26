import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
#prefix 
bot = commands.Bot(command_prefix="!", intents=intents)
#Prefix bota verilecek komutların başında bulunacak karakterdir bu karakteri kullandığımız zaman bot komutlarınıza cevap verir ben ! koydum siz başka alternatifler kullanabilirsiniz

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

#Sunucudan kişileri atmak için
@bot.command()
async def kick(ctx, member = discord.Member, *,  reason = 'No reason'):
    
    if ctx.message.author.guild_permissions.kick_members  == True:
        await member.kick(reason=reason)
        await ctx.send(f'**{member}** was kicked.\nReason: _{reason}_')

    elif ctx.message.author.guild_permissions.kick_members  == False:
        await ctx.channel.send('You do not have permissions to do that.')

bot.run("Buraya botun tokenini yazın")
#tokeni bulmak için https://discord.com/developers kısmına girin. 



  
  
  
