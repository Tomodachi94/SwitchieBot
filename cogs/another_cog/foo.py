from discord.ext import commands

class foocog(commands.Cog):       # again we define a class
	def __init__(self, bot):      # passing bot in __init__
		self.bot = bot
	
	@commands.Cog.listener()                 # a simple command
	async def on_message(self, message):     # this returns "Bar!" when you use !foo in discord
		print(message.content)               # the bot will print the message content in terminal whenever it reads a message

def setup(bot):                   # we again define the setup command
	bot.add_cog(foocog(bot))      # and we add the cog content to the bot