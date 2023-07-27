**OFAC Sanctions Data Processing**
This repository contains a GitHub Actions workflow that automatically downloads and processes the OFAC special designated nationals XML file (sdn_advanced.xml) from the U.S. Department of the Treasury website. The processed data is stored in a text file in the "Sanctioned Addresses" directory and it contains all the ETH addresses sanctioned by OFAC.

Workflow
The workflow is scheduled to run every day at midnight UTC and each time a push is made to the repository. The steps of the workflow are as follows:

Setup Python: The workflow sets up a Python environment using the latest version of Python.

Download XML file: The workflow downloads the sdn_advanced.xml file from the U.S. Department of the Treasury website.

Process XML file: The workflow runs a Python script to process the XML file. The script extracts sanctioned digital currency addresses for Ethereum (ETH) and outputs them to a text file.

Commit and push changes: The workflow commits the generated text file and pushes the changes to the repository.

Python Script
The Python script (process_xml.py) used in this workflow parses the XML file and extracts sanctioned digital currency addresses for a specified asset (in this case, Ethereum). The script can be modified to extract addresses for other assets as well.
