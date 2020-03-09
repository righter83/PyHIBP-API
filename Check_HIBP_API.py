import pyhibp
import json
from pyhibp import pwnedpasswords as pw
import time
import sys

# List of Breaches with included passwords (this is only a small amount of pages which are used by my users)
pws = ['Adobe', 'LinkedIn', 'Dubsmash', 'Netlog', 'OnlinerSpambot', 'MyFitnessPal' 'Lastfm', 'MyHeritage', 'DVDShopCH', 'Evite', 'Dropbox', '8fit', 'ArmorGames', 'BTCE', 'Canva', 'CafePress', 'ShareThis', 'Coinmama', 'Trillian']

# read config file
with open('config.json') as config_file:
    data = json.load(config_file)
onlyPw=data['onlyPw']

# configure HIBP Agent
pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
pyhibp.set_api_key(key=data['api-key'])

# check only one account
if len(sys.argv) > 1:
   resp = pyhibp.get_account_breaches(account=sys.argv[1], truncate_response=True)
   if resp:
      print("Account ",sys.argv[1],"was hacked on these sites",resp)
# check a whole list
else:
   with open("list.txt") as f:
      list = f.read().splitlines()
      for user in list:
         resp = pyhibp.get_account_breaches(account=user, truncate_response=True)
         time.sleep(1.5)
         search=json.dumps(resp)
         # show only breaches with password
         if onlyPw:
            if any(x in search for x in pws):
               print("Account ",user.strip(),"password leaked by these site hacks",resp)
         # show all breaches
         else:
            if resp:
               print("Account ",user.strip(),"informations leaked by these site hacks",resp)


