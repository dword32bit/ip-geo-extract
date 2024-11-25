import subprocess
import os
import requests
import re

link = input("Input link address : ")

def get_ip(link):
    process = subprocess.Popen(
        ['wget', link, '-O', 'video.mp4'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    _, stderr = process.communicate()
    stderr = stderr.decode('utf-8')

    ip_addresses = []
    for line in stderr.split('\n'):
        if 'Resolving' in line:
            ip_addresses = re.findall(r'\d+\.\d+\.\d+\.\d+', line)

    if ip_addresses:
        print('IP Addresses:')
        for ip in ip_addresses:
            print(ip)
    else:
        print('No IP addresses found')

    filename = 'get'
    i = 1
    while os.path.exists(filename):
        filename = f'get{i}'
        i += 1
    os.rename('get', filename)
    print(f'File saved as {filename}')

    for ip in ip_addresses:
        get_geo(ip)

def get_geo(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        print("\nGeolocation Information:")
        print(f"IP: {ip}")
        print(f"Country: {data.get('country', 'Unknown')}")
        print(f"Region: {data.get('regionName', 'Unknown')}")
        print(f"City: {data.get('city', 'Unknown')}")
        print(f"Latitude: {data.get('lat', 'Unknown')}")
        print(f"Longitude: {data.get('lon', 'Unknown')}")
        print(f"ISP: {data.get('isp', 'Unknown')}")
        print(f"Organization: {data.get('org', 'Unknown')}")
    except requests.exceptions.RequestException as e:
        print("Error retrieving geolocation information:", e)

get_ip(link)
