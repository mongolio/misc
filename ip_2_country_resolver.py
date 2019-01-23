import csv
import json
from urllib.request import urlopen

HOME_DIR = "/Users/mongolio/"

TOKEN="d71755d281a65f"

INPUT_FILE = "input_ips.csv"
OUTPUT_FILE = "ip_2_country.csv"

def read_input_file():
    """
    """
    results_list=[]
    ip_addr_data = open(f"{HOME_DIR}{INPUT_FILE}","r", encoding = "utf-8-sig").readlines()
    for line in ip_addr_data:
        result=line.strip()
        results_list.append(result)

    return results_list

def save_output_file(output_dictionary):
    """
    """
    print(output_dictionary)
    with open(f'{HOME_DIR}{OUTPUT_FILE}','w') as  dst_file:
        obj = csv.writer(dst_file)
        obj.writerows(output_dictionary.items())


def resolve_country(current_ip):
    """
    """
    url = f'http://ipinfo.io/{current_ip}?TOKEN=${TOKEN}'
    response = urlopen(url)
    data = json.load(response)
    return data['country']
