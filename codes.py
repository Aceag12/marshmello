import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp
from discord.utils import get
from random import choice, shuffle


commandprefix = "-"

client = commands.Bot(command_prefix=commandprefix)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='with ' + str(len(set(client.get_all_members())))+' members'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name='in ' + str(len(client.servers))+' servers'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="Marshmello Songs", type=2))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="Mello Gang", type=3))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="for -help", type=3))
@client.event
async def on_ready():
    ...
    client.loop.create_task(status_task())   

@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Pong:- {}ms :hourglass_flowing_sand:".format(round((t2-t1)*1000)))
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
        await client.send_typing(ctx.message.channel)
        await client.send_message(ctx.message.channel, "```Help Commands\n -ping (returns pong)\n -ask (ask questions that has answer as Yes & No.)\n -facts (Some Facts about Marshmello.)```")
@client.command(pass_context = True)
async def ask(ctx):
    choices = ['Yes!', 'No!']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title="Marshmello's Answer Yes/No", description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)        
@client.command(pass_context = True)
async def facts(ctx):
    choices = ['Real Name Of Marshmello is ``Chris Comstock``', 'Marshmello lives in Los Angeles, California.', 'Marshmello was born on May 19, 1992', 'MArshmello is of Dutch nationality.', 'In 2016, he launched his first album called “Joytime” that contained 10 songs.', 'The identity of Marshmello was exposed accidentally on Instagram.', 'Christopher Comstock, known professionally as Marshmello, is an American electronic music producer and DJ. He first gained international recognition by releasing remixes of songs by Jack Ü and Zedd.']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='```Marshmello Fact File```', description=random.choice(choices))
    em.set_thumbnail(url='https://media.giphy.com/media/3bYQeYvVruuWs/giphy.gif')
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
        
@client.command(pass_context = True)
async def welcome(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '✖‿✖-spawn-island',everyone)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
          
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '✖‿✖-spawn-island':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Have a greate time here.', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will follow all the rules of this server :) .**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/X9Gg8hZNa4lxEj3iAN/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            await asyncio.sleep(0.5)
            await client.send_message(channel, embed=embed)
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '✖‿✖-spawn-island':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='We Will Remember You.', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**We hope you will join again :( .**', inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)  
            
client.run('token')
