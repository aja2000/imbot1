import discord

file = open("key.txt", "r")
key = file.read()


class Client(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("Rewddy")

    # we are now connected to discord's API
    async def on_message(self, message):
        if message.guild.name == "Test" and str(message.content).lower().__contains__("poop"):
            print(message.content, message.author)
            await message.channel.send("Die")


client = Client()
client.run(key)
