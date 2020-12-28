from discord.ext import commands

class blah_blah(commands.Cog):                        # we first need to define a class
	def __init__(self, bot):                          # we pass bot in the __init__ function
		self.bot = bot                                # we need to import the bot variable from main.py file so we can use it here

	@commands.command()                               # we use the @commands.command() decorator to create commands
	async def name(self, ctx):                        # in a class, the "self" argument is necessary in every single function just like ctx
		bot_name = self.bot.user.name                 # we use "self.bot" instead of just "bot" as we used to do in main.py
		await ctx.send(f"My name is {bot_name}")      # You'll see the bot will now return its name 

def setup(bot):                                       # we'll have to setup the bot now
	bot.add_cog(blah_blah(bot))                       # adding the "blah_blah" class to the bot