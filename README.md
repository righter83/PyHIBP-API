# PyHIBP API E-Mail Address List Scanner
With this little script you can check a list of E-Mail Addressess if they have been powned.
The source check is done via the HaveIbeenPowned APIv3

### Requirements
You need an HIBP Api Key: https://haveibeenpwned.com/API/Key

### Installation
First clone the repo:
```
git clone https://github.com/righter83/PyHIBP-API   
```

Copy the config file and put your API Key in the copied file
```
cp config.json.dist config.json
```
### Usage
Create a list.txt File with an E-Mail Address on each line

run the script
```
python3 Check_HIBP_API.py
```

### Results
```
Account  test@example.com was hacked on these sites [{'Name': '000webhost'}, {'Name': '500px'}, {'Name': '8tracks'}]
```

