# TODO DETECT MORE THAN ONE SWEAR PER MESSAGE





import discord

file = open("key.txt", "r")
key = file.read()

swears = open("swears.csv", "r")
swears_list = swears.read()

split = swears_list.split(",")


# print(split)


def bad_word_test(message):
    for n in split:
        if str(message).lower().__contains__(n):
            return True
    return False


class Client(discord.Client):
    def __init__(self):
        super().__init__()
        self.swear_count = 0

    async def on_ready(self):
        print("API Ready")

    # we are now connected to discord's API
    async def on_message(self, message):
        if message.guild.name == "Test" and not message.author.bot:
            if message.content == "!swears":
                if self.swear_count == 0:
                    await message.channel.send("Swear Words: **" + str(self.swear_count) + ".** Keep it Up!")
                else:
                    await message.channel.send("Swear Words: **" + str(self.swear_count) + ".** Bad Job.")
            elif message.content == "!clear":
                self.swear_count = 0
            elif bad_word_test(message.content):
                self.swear_count += 1

        print(self.swear_count)


client = Client()
client.run(key)
