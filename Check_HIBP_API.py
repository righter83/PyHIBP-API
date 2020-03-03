import pyhibp
import json
from pyhibp import pwnedpasswords as pw
import time
import sys

with open('config.json') as config_file:
    data = json.load(config_file)

pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
pyhibp.set_api_key(key=data['api-key'])

if len(sys.argv) > 1:
   resp = pyhibp.get_account_breaches(account=sys.argv[1], truncate_response=True)
   if resp:
      print("Account ",sys.argv[1],"was hacked on these sites",resp)
else:
   with open("list.txt") as f:
      list = f.read().splitlines()
      for user in list:
         resp = pyhibp.get_account_breaches(account=user, truncate_response=True)
         time.sleep(1.5)
         if resp:
            print("Account ",user,"was hacked on these sites",resp)


