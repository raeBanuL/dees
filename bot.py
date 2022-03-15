import discord
import random
from discord.ext import commands
from datetime import date
from time import gmtime, strftime

today = date.today()
bot = commands.Bot(command_prefix='==')
bot.remove_command("help")
command = {}


@bot.event
async def on_message(message):
    # Makes the bot say hello to you
    if message.content == 'hello' or message.content == 'hi' or message.content == 'hey':
        await message.channel.send('Hello ' + message.author.mention + '!')

    # jared
    elif message.content == 'jared' or message.content == 'tryhard':
        tryhard_quotes = ['currently tryharding', 'valo tryhard', 'gg ez', 'mad cuz bad', 'stay mad', 'why are you so bad at videogames',
                          '"you probably need to add something about their sexuality"-notdoom']
        await message.channel.send(random.choice(tryhard_quotes))

    elif message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="send help pls",
                       description=f'Use "{bot.command_prefix}help <command>" for more detail on that command.',
                       color=ctx.author.color)

    em.add_field(name="Utility:", value='time\ndate')
    em.add_field(name="Fun:", value='eightball\nroll\nsendgri\nsendback')
    em.add_field(name="Moderation:", value='addrole\nremoverole')
    em.add_field(name="Other:", value='dani\naungel_xoxo')
    await ctx.channel.send(embed=em)


@help.command()
async def time(ctx):
    em = discord.Embed(title="time",
                       description=f'It literally just tells the time (in GMT for some reason)',
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}time')
    await ctx.channel.send(embed=em)


@help.command()
async def date(ctx):
    em = discord.Embed(title="date",
                       description=f'It literally just says the date.',
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}date')
    await ctx.channel.send(embed=em)


@help.command()
async def eightball(ctx):
    em = discord.Embed(title="eightball",
                       description=f'You ask a question, it gives you an answer.',
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}eightball [question]')
    await ctx.channel.send(embed=em)


@help.command()
async def roll(ctx):
    em = discord.Embed(title="roll",
                       description=f'Roll a number from 0 to probably(?) infinty.',
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}roll [number]')
    await ctx.channel.send(embed=em)


@help.command()
async def sendgri(ctx):
    em = discord.Embed(title="sendgri",
                       description="Send some messages to my class' #general channel!",
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}sendgri [message]')
    await ctx.channel.send(embed=em)


@help.command()
async def sendback(ctx):
    em = discord.Embed(title="sendback",
                       description="Send some messages back (to be used only in the Grimaltos Server)!",
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}sendback [message]')
    await ctx.channel.send(embed=em)


@help.command()
async def addrole(ctx):
    em = discord.Embed(title="addrole",
                       description=f'Allows you to give someone a role (Moderator and above only)',
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}addrole [member] [role]')
    await ctx.channel.send(embed=em)


@help.command()
async def removerole(ctx):
    em = discord.Embed(title="removerole",
                       description="Allows you to remove someone's role (Moderator and above only)",
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}removerole [member] [role]')
    await ctx.channel.send(embed=em)


@help.command()
async def dani(ctx):
    em = discord.Embed(title="This is the greatest dani moment of All Time",
                       description="wishlist karlson now",
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}dani')
    await ctx.channel.send(embed=em)


@help.command()
async def aungel_xoxo(ctx):
    em = discord.Embed(title='aungel_xoxo',
                       description="R.I.P. aungel_xoxo\n2020-2021 o7",
                       color=ctx.author.color)

    em.add_field(name="**How do?**", value=f'{bot.command_prefix}aungel_xoxo')
    await ctx.channel.send(embed=em)


@bot.command()
# Tells the time
async def time(ctx):
    await ctx.channel.send(strftime("%H : %M : %S **GMT**", gmtime()))
    print(f'{str(ctx.author)} asks for the time...\n({strftime("%H : %M : %S GMT", gmtime())})')


@bot.command()
# Tells the date
async def date(ctx):
    await ctx.channel.send(today)
    print(f'{str(ctx.author)} asks for the date...\n{str(today)}')


@bot.command()
# Lucky 8 ball
async def eightball(ctx, *, question):
    responses = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', "Don't count on it.", 'It is certain.', 'It is decidedly so.',
                 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.',
                 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.',
                 'Yes – definitely.', 'You may rely on it.']
    answer = f"8ball's response to {ctx.author}'s question: **({question})** is...\n\n*{random.choice(responses)}*"
    await ctx.channel.send(answer)
    print(answer)


@bot.command()
# RNG
async def roll(ctx, number):
    value = random.randint(0, int(number) + 1)
    await ctx.send(value)
    print(str(ctx.author) + ' has rolled a ' + str(value) + '.')
    if value == 727:
        await ctx.send("wysi\ncookiezi best girl btw")
    elif value == 69:
        await ctx.send('**n i c e**')
    elif value <= 7:
        await ctx.send('haha lmao')


@bot.command()
# o7 aungel_xoxo
async def aungel_xoxo(ctx):
    await ctx.channel.send("sorry i'm making tea at 3am")
    print(f'{str(ctx.author)} has called upon thee.')


@bot.command()
@commands.has_role("Moderator")
# add/remove role functions
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send("aight")
    print(f"{str(ctx.author)} has removed someone's role.")


@bot.command()
@commands.has_role("Moderator")
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send("aight")
    print(f"{str(ctx.author)} has removed someone's role.")


@bot.command()
# dani
async def dani(ctx):
    await ctx.send('https://store.steampowered.com/app/1228610/KARLSON/')


@bot.command()
# sends a message (msg) to my class' server
async def sendgri(ctx, *, msg):
    global chid
    chid = ctx.channel.id
    channel = bot.get_channel(872691438050234368)
    await channel.send(f'**{ctx.author}:** ' + msg)
    await ctx.send('**Success!**')
    print(f'{str(ctx.author)} says {msg}')


@bot.command()
# allows for sending back of messages
async def sendback(ctx, *, msg):
    channel = bot.get_channel(chid)
    await channel.send(f'**{ctx.author}:** ' + msg)
    await ctx.send('**Success!**')
    print(f'{str(ctx.author)} says {msg}')


@bot.command()
# supposed to be og feature of this bot
async def bithdayset(ctx):
    print(str(id))

bot.run('ODE5MDA5Nzg3MDQ3MTgyMzc2.YEgYTQ.kOaV283C_Jwh54GQpcvGqelxSZQ')
