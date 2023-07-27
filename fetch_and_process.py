import requests
import subprocess
import os

def download_xml_and_run_script():
    url = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml'
    response = requests.get(url)
    with open('sdn_advanced.xml', 'w') as file:
        file.write(response.text)

    # Get the current working directory
    cwd = os.getcwd()

    # Call your script here
    subprocess.call(["python", "process_xml.py", "--output-path", cwd, "sdn_advanced.xml"])

download_xml_and_run_script()
