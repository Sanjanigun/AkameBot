import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.fl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Sedang Memulai...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Cieeee Nungguin, Tertipu Kamu Bangsat!`")
	# I did it for two hours :D just ctrl+c - crtl+v






