import discord
from discord.ext import commands
import math

token = ""  # put your bot token here
tax_channel = 12345  # put tax channel id here

# Intents declaration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}.")


@bot.event
async def on_message(message):
    global num
    num = ""
    global i
    i = 0
    global command
    global answered
    global warned
    warned = False
    answered = False
    if message.author == bot.user:
        return
    else:
        if message.content.lower().startswith("^tax") and message.channel.id == tax_channel:
            if len(message.content.lower().split(" ")) == 1:
                await message.channel.send("You have to put a number.")
            elif len(message.content.lower().split(" ")) == 2:
                command = message.content.lower().split(" ")[1]
                for letter in message.content.lower().split(" ")[1]:
                    if letter in "1234567890.":
                        if command.split(letter, 1)[1] != "":
                            if i < 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                                i = i + 1
                            elif i >= 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                        elif command.split(letter, 1)[1] == "":
                            if not answered:
                                num = num + letter
                                total_num = math.ceil(float(num) * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                            elif answered:
                                return
                    elif letter in "k":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the K")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "m":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the M")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "b":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the B")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000000000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    else:
                        print(letter)
                        if not warned:
                            await message.channel.send("Please put a proper number")
                            warned = True
                        elif warned:
                            return
            elif len(message.content.lower().split(" ")) >= 3:
                await message.channel.send("Only 1 argument allowed.")

        elif message.content.lower().startswith("^tax") and message.channel.id != tax_channel:
            if len(message.content.lower().split(" ")) == 1:
                await message.channel.send("You have to put a number.")
            elif len(message.content.lower().split(" ")) == 2:
                command = message.content.lower().split(" ")[1]
                for letter in message.content.lower().split(" ")[1]:
                    if letter in "1234567890.":
                        if command.split(letter, 1)[1] != "":
                            if i < 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                                i = i + 1
                            elif i >= 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                        # if there is nothing after the number
                        elif command.split(letter, 1)[1] == "":
                            if not answered:
                                num = num + letter
                                total_num = math.ceil(float(num) * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                            elif answered:
                                return
                    elif letter in "k":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the K")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "m":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the M")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "b":
                        if i < 1:
                            if not warned:
                                await message.channel.send("You have to put a number.")
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    await message.channel.send("You can't put anything after the B")
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000000000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    else:
                        if not warned:
                            await message.channel.send("Please put a proper number")
                            warned = True
                        elif warned:
                            return
            elif len(message.content.lower().split(" ")) >= 3:
                await message.channel.send("Only 1 argument allowed.")
        elif message.channel.id == tax_channel and message.content.lower().startswith("^tax") == False:
            if len(message.content.lower().split(" ")) == 1:
                command = message.content.lower()
                for letter in message.content.lower():
                    if letter in "1234567890.":
                        if command.split(letter, 1)[1] != "":
                            if i < 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                                i = i + 1
                            elif i >= 1:
                                command = command.replace(letter, "", 1)
                                num = num + letter
                        elif command.split(letter, 1)[1] == "":
                            if not answered:
                                num = num + letter
                                total_num = math.ceil(float(num) * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                            elif answered:
                                return
                    elif letter in "k":
                        if i < 1:
                            if not warned:
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "m":
                        if i < 1:
                            if not warned:
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                num = float(num) * 1000000
                                total_num = math.ceil(num * 1.0526315789473683)
                                embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                f"What you need "
                                f"to transfer for it to reach full: **${str(total_num)}**\n"
                                f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                      color=discord.Colour.teal())
                                embed.set_author(name=f"Requested by {message.author.name}",
                                                 icon_url=message.author.avatar.url)
                                embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                await message.channel.send(content=None, embed=embed)
                    elif letter in "b":
                        if i < 1:
                            if not warned:
                                warned = True
                            elif warned:
                                return
                            i = i + 1
                        elif i >= 1:
                            if command.split(letter, 1)[1] != "":
                                if not warned:
                                    warned = True
                                elif warned:
                                    return
                            elif command.split(letter, 1)[1] == "":
                                if not warned:
                                    num = float(num) * 1000000000
                                    total_num = math.ceil(num * 1.0526315789473683)
                                    embed = discord.Embed(title="ProBot Taxes", type="rich", description=
                                    f"What you need "
                                    f"to transfer for it to reach full: **${str(total_num)}**\n"
                                    f"How much will reach if you transfer that: **${str(int(float(num) - (float(num) / 20)))}**\n"
                                    f"Double Tax (MM used): **${math.ceil(total_num * 1.0526315789473683)}**",
                                                          color=discord.Colour.teal())
                                    embed.set_author(name=f"Requested by {message.author.name}",
                                                     icon_url=message.author.avatar.url)
                                    embed.set_footer(text="This bot has been created by Clockodilee#6667")
                                    await message.channel.send(content=None, embed=embed)
                                elif warned:
                                    pass
                    else:
                        if not warned:
                            warned = True
                        elif warned:
                            return


bot.run(token)
