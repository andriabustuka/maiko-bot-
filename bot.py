import discord

# თუ ეს ტოკენი არ იმუშავებს, გამოიყენე Reset Token და ჩასვი ახალი აქ:
TOKEN = 'MTQ5NTQ3MDk4MTEyNzQ3MTIyNA.GAIOv8.MHUimVGIr3M1e2zpW2Iu2y5_NgWEfbfNCOWBRM'

intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'წარმატებით ჩაირთო! ბოტის სახელია: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if "shit" in msg:
        await message.reply("shit კიარა შენივე shit არ გაჭამო უზრდელი ესს 😒")
    
    elif "yle" in msg or "yleo" in msg:
        await message.reply("mut tut es ra uwmawuri sityva droze direqtortan")
    
    elif "bozo" in msg:
        await message.reply("bozi sabozetshia tut")
    
    elif "mogityan" in msg:
        await message.reply("ES RA ARISSSSSSSSSSSSSSSS TUTTTTTTTTTTTT")

client.run(TOKEN)