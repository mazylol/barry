#The file to run everything
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os
from helper import helper, helper
from responses import responses, responses
from scraping import scraping, scraping
from images import images, images
bot = discord.Client()
bot = commands.Bot(command_prefix='~',help_command=None)
bot.add_cog(helper(bot))
bot.add_cog(responses(bot))
bot.add_cog(scraping(bot))
bot.add_cog(images(bot))

@bot.event
async def on_ready():
 game = discord.Game('You like jazz? | ~help')
 await bot.change_presence(status=discord.Status.online, activity=game)
 print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv("TOKEN"))
