import discord
import random
from discord.ext.commands import Bot

BOT_PREFIX = ('!')
TOKEN = 
client = Bot(command_prefix=BOT_PREFIX)
SPEC_USER_ID = int()


@client.command(pass_context=True)
async def echo(context):
    if isSpecUser(context):
        print("test complete!")
        await client.say("...")
        pass
    
    pass

@client.command(pass_context=True)
async def clean(context, n):
    if isSpecUser(context):
        channel = context.message.channel
        await client.purge_from(channel, limit=int(n)+int(1))
        pass
    
    pass

@client.command(pass_context=True)
async def stop(context, n):
    await client.say("It's time to stop " + n)
    pass
@client.command(pass_context=True)
async def rip(context):
    responses = [
        "Ooo! That's a big rip!",
        "He's gonna need some flex tape for that one!",
        "That's a LOTTA damage!",
        "OOH! THAT'S IKONIC!"
    ]
    await client.say(random.choice(responses))

    
    pass

@client.command(pass_context=True)
async def skip(context):
    if isSpecUser(context):
        #author = context.message.author
        #await bot.join_voice_channel()
        pass

    pass

@client.command(pass_context=True)
async def no(context, word):
    if isSpecUser(context):
        if word == 'u':
        #author = context.message.author
            await client.say("no u")
        pass

    pass


def isSpecUser(context):
    if int(context.message.author.id) == SPEC_USER_ID:
        return True
    else:
        return False
pass

client.run(TOKEN)