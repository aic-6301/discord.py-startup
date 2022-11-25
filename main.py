import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')
token = os.getenv('token')


@bot.ready
async def on_ready():
  print('ready')

@bot.command()
async def neko(ctx):
  await ctx.send('にゃーん')

bot.run(token)
