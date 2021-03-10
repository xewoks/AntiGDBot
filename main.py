import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
	while 1:
		for guild in client.guilds:
			for member in guild.members:
				for x in member.activities:
					if type(x) == discord.Game:
						print(x)
						if str(x) == "Geometry Dash":
							a = await client.get_user_info(member.id)
							await a.send(f'You have been banned from `{guild}`\nReason: playing GD')
							await guild.ban(member)
		await asyncio.sleep(5)
client.run("TOKEN_HHERE")
