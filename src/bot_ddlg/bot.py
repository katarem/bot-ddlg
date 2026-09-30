import os
import discord
from dotenv import load_dotenv

load_dotenv()

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        if message.author == self.user:
            return

        if 'hola' in message.content.lower():
            with open('./assets/hola.png', 'rb') as img_src:
                await message.channel.send(file=discord.File(img_src))
                return

        
        if 'adios' in message.content.lower():
            with open('./assets/adios.png', 'rb') as img_src:
                await message.channel.send(file=discord.File(img_src))
                return
pass

intents = discord.Intents.default()
intents.message_content = True
client = BotClient(intents=intents)

if os.getenv('BOT_TOKEN') is None:
    print('You have to put the bot token first!')
    exit(1)

token: str = os.getenv('BOT_TOKEN')

client.run(token)