######################################################################################
#                                                                                    #
#   To run this bot repl, fork it, create a file named .env and put this inside it   #
#                                                                                    #
#   TOKEN=your_token_here                                                            #
#                                                                                    #
#   of course you'll have to put your token inside the variable without any quotes.  #
#   For more info on why it is a good practise to use .env files,                    #
#   read my post on securing your tokens                                             #
#                                                                                    #
#   https://repl.it/talk/learn/securing-discord-bot-token-on-replit/48012            #
#                                                                                    #
######################################################################################																	


from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '!')

""""
Before going further, please read these two files:
blah.py (the 1st cog)    -    https://repl.it/@HarshVardhan19/cogs-tuto#cogs/blah.py
foo.py  (the 2nd cog)    -    https://repl.it/@HarshVardhan19/cogs-tuto#cogs/foo.py
"""

# assuming you went through blah.py and foo.py, we now create a list of the cogs we wrote so far

cogs = ["cogs.blah", "cogs.another_cog.foo"]

# here, taking example of "cogs.blah", we just reference it to the blah.py file
# we literally tell it: find the file named 'blah' in the folder named 'cogs'
# earlier, you'd have linked files in the format "cogs/blah.py"
# but here, instead of "cog/blah.py", we use "cogs.blah"
# yes, we do not add the file extension, just the folder name, a dot, and the file name

# now for the "cogs.another_cog.foo", it is an example to show you can even add multiple folders
# you can also learn how to use events in a cog in the foo.py file
# so you can create nested folders, to organize your code in a better way
# for "cogs.another_cog.foo" we tell it: find the file named 'foo' in the folder named 'another_cog' which is inside the folder named 'cogs'
# neat? huh?

# The below part just needs to be written once
# and it will load the cogs whenever you update the list above
# and ofcourse you'll have to rerun the bot after you update the list

@bot.event
async def on_ready():
	print("The bot is ready!")                # The bot sends this when it's ready, there isn't really need of it, but looks good in the terminal
	print("Loading cogs . . .")               # This again, no actual need, but looks in the terminal
	for cog in cogs:                          # Now, we iterate through the "cogs" list we created up there
		try:                                  # we put up a "try" so it doesn't break the loop when one of the cogs return any error
			bot.load_extension(cog)           # and now, we actually just load the extension
			print(cog + " was loaded.")       # and, again, for terminal's appearance sake, also it would tell you if the cogs got loaded successfully
		except Exception as e:                # now, the "except" part, we simply reference a variable "e" as the Exception(error)
			print(e)                          # and we tell it to print "e" which is actually the Exception i.e. error in the cog

@bot.command()
async def ping(ctx):
	await ctx.send("Pong!!")

"""
To run this bot repl, fork it, create a file named .env and put this inside it

TOKEN=your_token_here

of course you'll have to put your token inside the variable without any quotes
for more info on why it is a good practise to use .env files,
read my post on securing your tokens

https://repl.it/talk/learn/securing-discord-bot-token-on-replit/48012
"""

token = os.environ.get("TOKEN")
bot.run(token, reconnect = True, bot = True)