import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Vibes bot")
    game = discord.Game("Vibe's Bot")
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="New Message!", value=msg, inline=True)
                        embed.set_footer(text="Made by Vibe!")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzUxOTY3MzI1MTI4ODg0Mzg2.X1QyJQ.Svms5dwOPgiCLeZv77WReZkTfDs')
