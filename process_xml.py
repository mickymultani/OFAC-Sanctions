import requests
import subprocess
import os

def download_xml_and_run_script():
    url = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml'
    response = requests.get(url)
    
    # Define the path where you want to download the XML file
    xml_file_path = os.path.join(os.getcwd(), 'sdn_advanced.xml')

    with open(xml_file_path, 'w') as file:
        file.write(response.text)

    # Call your script here
    subprocess.call(["python", "process_xml.py", "-sdn", xml_file_path, "--output-path", os.getcwd()])

download_xml_and_run_script()
