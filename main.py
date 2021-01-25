import discord
from discord.ext import commands
import asyncio
import webserver
from webserver import keep_alive
import time
import subprocess
import platform
import os
import flask
import json
import requests
import re
from bs4 import BeautifulSoup as bs
import json
import calendar
import wikipedia
from random import randint
from flask import Flask
from threading import Thread
import datetime
import urllib.parse
from dotenv import load_dotenv
import random
from discord.ext.commands import cooldown
from aiohttp import request
import aiohttp
import asyncio
import pyfiglet
import os
import typing
import asyncio
import os
import hashlib



client = discord.Client()
client = commands.Bot(command_prefix='>')

print('bot made by mondomodsv5')
client.remove_command('help')
       
 

@client.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(title="commands", description="List of Commands" , color=0xff0000)
	embed.add_field(
	    name=">serverstat", value=f"Shows Server Info", inline=False)
	embed.add_field(name=">leader", value=f"Shows MERC Leader", inline=False)
	embed.add_field(name=">leader", value=f"Shows dxwnmy Leader", inline=False)
	embed.add_field(name=">server", value=f"Shows Server Info", inline=False)
	embed.add_field(name=">PING", value=f"Shows Server Ping", inline=False)
	embed.add_field(
	    name=">clear  +  amount",
	    value=f"Clears the channel of messages",
	    inline=False)
	embed.add_field(
	    name=">user + @User", value=f"Shows a Users Info", inline=False)
	embed.add_field(
	    name=">warn + @User", value=f"Warns a UserIn Server", inline=False)
	embed.add_field(
	    name=">kick + @User", value=f"Kicks User from Server", inline=False)
	embed.add_field(
	    name=">Ban + @User", value=f"Bans User From Server", inline=False)
	embed.add_field(
	    name=">Unban + @User", value=f"Unbans User From Server", inline=False)
	embed.add_field(
	    name=">roles + @User", value="Shows Top Role of User", inline=False)
	embed.add_field(
	    name=">joined + @User",
	    value="Says When a User Joined the server",
	    inline=False)
	embed.add_field(
	    name=">perms + @User",
	    value="Says what Permissions a User Has",
	    inline=False)
	embed.add_field(
	    name=">avatar + @user", value="Shows user avatar", inline=False)
	embed.add_field(name=">ownerinfo", value="owners contact and other shit", inline=False)
	embed.add_field(name=">Fun", value= "sends fun commands", inline=False)
	await ctx.send(embed=embed)


@client.command(pass_context=True)
async def Fun(ctx):
	embed = discord.Embed(
	    title="fun Commands", description="Fun commands down", color=0xff0000)
	embed.add_field(
	    name=">bottles", value=f"plays bottles game", inline=False)
	embed.add_field(name=">user", value=f"bot says a users info ", inline=False)
	embed.add_field(name=">avatar", value=f"Shows pfp of somone", inline=False)
	embed.add_field(name=">slap", value=f"Slaps somone", inline=False)
	embed.add_field(name=">Punch", value=f"punches a bitch", inline=False)
	await ctx.send(embed=embed)
  
	
	





@client.command()
async def Catto(self, ctx):

	colour_choices = [
	    0x400000, 0x997379, 0xeb96aa, 0x4870a0, 0x49a7c3, 0x8b3a3a, 0x1e747c,
	    0x0000ff
	]

	cat_url = "http://aws.random.cat/meow"
	async with request("GET", cat_url, headers={}) as response:
		if response.status == 200:
			data = await response.json()
			image_link = data["file"]
			embed = discord.Embed(colour=random.choice(colour_choices))
			embed.set_image(url=image_link)
			await ctx.send(embed=embed)

		else:
			await ctx.send(f'The API seems down, says {response.status}')


@client.event
async def on_ready():
	game = discord.Game(f'GRANNY')
	await client.change_presence(status=discord.Status.idle, activity=game)
	print('Bot is ready!\n\nServer\'s info\n')
	print(f"serving in {len(client.guilds)} servers")
	for server in client.guilds:
		print(
		    f"Server name: {server.name}; Members: {server.member_count}; ID: {server.id}"
		)


@client.command()
async def test(ctx, *args):
	await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


#leader of crew
@client.command()
async def leader(ctx):
	await ctx.send('Leader of dxwnmy is DXWNMYOVH')
	await ctx.send('leader of merc is mondo and dxwnmyserver')


	#just says bruh
@client.command()
async def Bruh(ctx):
	await ctx.send('Bruh')


#just says bruh
@client.command()
async def ownerinfo(ctx):
	await ctx.send('name:mondo bot version: v4	contact info: dxwnmycrew@outlook.com')


#server stats
@client.command()
async def serverstat(ctx):
	wlist = []
	for w in await ctx.guild.webhooks():
		wlist.append(f"{w.name} - {w.url}")
	content = "\n".join(wlist)
	lk = len(wlist)
	server_name = str(ctx.guild.name)
	server_owner = str(ctx.guild.owner)
	users = (ctx.guild.member_count)
	arb = int(users)
	countas = 0
	for user in list(ctx.guild.members):
		if user == user.bot:
			countas += 1
	server_region = str(ctx.message.guild.region)
	role_count = len(ctx.message.guild.roles)
	emoji_count = len(ctx.message.guild.emojis)
	channel_count = len([
	    x for x in ctx.message.guild.channels
	    if type(x) == discord.channel.TextChannel
	])
	voice_count = len(ctx.guild.voice_channels)
	created_on = ctx.message.guild.created_at.__format__(
	    '%A, %d. %B %Y @ %H:%M:%S')
	verification_level = ctx.message.guild.verification_level
	idserver = ctx.message.guild.id
	iconurl = ctx.message.guild.icon_url
	await ctx.send("server info!")
	await ctx.send(f"""***SERVER STATS ARE: ***
**Server Name: `{server_name}`
Server Owner: `{server_owner}`
Server ID: `{str(idserver)}`
Full Count Of Users: `{str(arb)}`
Number Of Members: `{str(arb-countas)}`
Number Of Bots: `{str(countas)}`
Number Of Channels: `{str(channel_count)}`
Number Of Voice Channels: `{str(voice_count)}`
Number Of Roles: `{str(role_count)}`
Number Of Emojis: `{str(emoji_count)}`
Number Of Boosts: `{str(ctx.message.guild.premium_subscription_count)}`
Number Of Webhooks: `{str(lk)}`
Verification Level: `{str(verification_level)}`
Server Region: `{str(server_region)}`
Server Created On: `{str(created_on)}`**""")

	await ctx.send(iconurl)
	await ctx.send("ADVANCED SERVER INO COMPLETE!!")
	await ctx.send("MAKING THIS COMMAND EMBED SOON :MAD:")


#shows pfp of you or mentioned user
@client.command(aliases=['av'])
async def avatar(ctx, member: discord.Member = None):
	if not member:
		member = ctx.message.author
	show_avatar = discord.Embed(
	    description="[Avatar URL](%s)" % member.avatar_url)
	show_avatar.set_image(url="{}".format(member.avatar_url))
	show_avatar.set_footer(text=f'{member}')
	await ctx.send(embed=show_avatar)


@client.event
async def on_ready():
	game = discord.Game('mondobotsv3')
	await client.change_presence(status=discord.Status.dnd, activity=game)
	print('Bot is ready!\n\nServer\'s info\n')
	print(f"serving in {len(client.guilds)} servers")
	for server in client.guilds:
		print(
		    f"Server name: {server.name}; Members: {server.member_count}; ID: {server.id}"
		)


#advanced user info
@client.command()
async def user(ctx, member: discord.Member = None):
	if member is None:
		member = ctx.message.author
		pronoun = "Your"
	else:
		pronoun = str(member)
	name = f"{member.name}#{member.discriminator}"
	status = ctx.author.status.name
	created_on = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
	userAvatarUrl = member.avatar_url
	join = member.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
	statoos = member.activity
	house = member.top_role
	permissions = member.permissions_in(ctx.message.channel)
	#userhighest role
	await ctx.send("suck it")
	await ctx.send(
	    f"""**`Here's the info i got out your moms bra:` {member.mention}!:
Username is: `{str(member.name)}`
UserTag is: `{str(member.discriminator)}`
User ID is: `{str(member.id)}`
User Presence is: `{str(status)}`
User Is Playing: `{str(statoos)}`
User Highest Role: `{str(house)}`
User Created On: `{str(created_on)}`
User Joined On: `{str(join)}`
User Permissions: `{str(permissions)}`**""")
	await ctx.send(userAvatarUrl)
	await ctx.send("bot made by mondo")


#checks latency
@client.command()
async def PING(ctx):
	if round(client.latency * 1000) <= 50:
		await ctx.send(
		    f'**I Have A `{round(client.latency * 1000)}` Milli Seconds! The Server Is Based Off `{(ctx.message.guild.region)}`! The Ping Is GREAT!**'
		)
	else:
		await ctx.send(
		    f'**I Have A `{round(client.latency * 1000)}` Milli Seconds! The Server Is Based Off `{(ctx.message.guild.region)}`! The Ping is USELESS LIKE YOU**'
		)


#clear channel
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
	await ctx.send("**CLEANED YOUR FUCKING CHANNEL OF  `" + str(amount) +
	               "` Messages YOU FUCKING BUM **")


#check song lyrics
@client.command()
async def lyric(ctx, artist, title):
	r = requests.get('https://api.lyrics.ovh/v1/{}/{}'.format(artist, title))
	if r.status_code == 200:
		l_response = json.loads(r.content)
		try:
			lyric = l_response["lyrics"]
			await ctx.send(f'**`Here are the lyrics:{lyric}`')
		except:
			await ctx.send(
			    f'**`Lyrics not found! or you have a fucking spelling problem you stupid retard`**'
			)


#Kicks people
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
	"""Kicks a User"""
	await member.kick()
	await ctx.message.add_reaction(" ")
	await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
	await ctx.send(f"{ctx.author.name} has kicked {member.display_name}")


#Bans People
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, reason=None):
	"""Bans a user"""
	if reason == None:
		await ctx.send(
		    f"Woah {ctx.author.mention}, Make sure you provide a reason!")
	else:
		messageok = f"You have been banned from {ctx.guild.name} for {reason}"
		await member.send(messageok)
		await member.ban(reason=reason)


#Unbans people
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
	"""Unbans a User"""
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split("#")

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name,
		                                       member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return


@client.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
	await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))


@client.command()
async def slap(ctx,
               members: commands.Greedy[discord.Member],
               *,
               reason='no reason'):
	slapped = ", ".join(x.name for x in members)
	await ctx.send('{} just got slapped for {}'.format(slapped, reason))


@client.command()
async def Punch(ctx,
                members: commands.Greedy[discord.Member],
                *,
                reason='no reason'):
	Punched = ", ".join(x.name for x in members)
	await ctx.send('{} just got punched for {}'.format(Punched, reason))


@client.command()
async def joined(ctx, *, member: discord.Member):
	await ctx.send('{0} joined on {0.joined_at}'.format(member))


@client.command()
async def f(self, ctx):
        """Press F to pay your respects"""
        await ctx.send(Language.get("fun.respects", ctx).format(ctx.author, random.randint(1, 10000)))

        


keep_alive()


TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
