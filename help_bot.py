import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

banned_words = ['fuck', 'cock', 'bitch', 'cocksucker', 'cocksuck', 'cunt', 'shit', 'whore', 'coon']

starter_warning = "Bad words are not allowed in this server, please refrain from using them."

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('.tips for bots command list'))
    print('Bot is online.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if any(word in message.content for word in banned_words):
        await message.channel.send(starter_warning)

    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases = ['link'])
async def usefull_link(ctx):
    await ctx.send("this is a usefull link")

@client.command(aliases = ['tips'])
async def com(ctx):
    embed = discord.Embed(title = 'Helpful bot tips')
    
    embed.add_field(name = 'Help Bot', value = (f"{'`Command prefix : .`'}\n{'`Show useful link/s added by tutors : .link`'}\n{'`Show Help Bot ping : .ping`'}"), inline = False)
    embed.add_field(name = 'Utix Bot', value = (f"{'`Command prefix : >`'}\n{'`Help command : >help`'}"), inline = False)
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)


client.run('token here')
