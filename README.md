# PyHIBP API E-Mail Address List or single account Scanner
With this little script you can check a single or a list of E-Mail Addressess if they have been powned.
The source check is done via the HaveIbeenPowned APIv3

### Requirements
You need an HIBP Api Key: https://haveibeenpwned.com/API/Key

Install the pyhipb Library
```
pip3 install pyhibp
```

### Installation
First clone the repo:
```
git clone https://github.com/righter83/PyHIBP-API
```

Copy the config file and put your API Key in the copied file
```
cp config.json.dist config.json
```

if you wanna print only Breaches with passwords set onlyPw to true in config.json
This is a static array list in the script

### Usage
run the script for a single address
```
python3 Check_HIBP_API.py user@example.com
```

run the script for a list of addresses which are stored in list.txt
```
python3 Check_HIBP_API.py
```


### Results
```
Account test@example.com was hacked on these sites [{'Name': '000webhost'}, {'Name': '500px'}, {'Name': '8tracks'}]
```

