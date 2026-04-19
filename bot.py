import discord
from flask import Flask
from threading import Thread
import os

# 1. Render-ისთვის საჭირო ვებ-სერვერი
app = Flask('')

@app.route('/')
def home():
    return "Maiko is alive and watching!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. ბოტის ძირითადი ნაწილი
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

# 3. ბოტის გაშვება (ტოკენს იღებს Render-ის სეიფიდან)
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
