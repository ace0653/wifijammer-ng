This project uses the wifijammer.py script from 5 years ago as a template for something newer, more stable and robust, and using AI-assisted coding to correct and improve upon the original in many ways. 
The newer wifijammer.py project has several goals in mind:
1) To produce a simpler, updated Python script for automating the process of deauth-ing users of the 2.4Gz Wifi spectrum, across all channels, with greater interactivity and options to better suit the user.
2) Add a fun, interactive menu interface!
3) Make the code simpler, possibly shorter overall, and easier to read than Hash's original.
4) Utilize various LLMs that specialize in logic and coding to assist and teach how this program works as a Proof-Of-Concept, refine the project, and help debug and improve upon the code along the way.


# wifijammer
Disconnect Nearby Access Points and Stations by forging and Transmitting Deauthentication Frames. Built on top of scapy and utilizes channel hopping and forging frames from a single interface. Works with **python 3**.


## Usage:
```
python3 [scriptname] [argument...]
python3 wifijammer-ng.py --help
```
## Installation:
Install Scapy: 
```
$ pip3 install scapy
```
## Usage:
```
python3 [scriptname] [argument...]
python3 wifijammer-ng.py --help
```

### Disclaimer
This tool is only intended for testing purposes and should be used where there is allowance of having de-authentication tests. The user should have prior consent for testing against the target. The author will not be held responsible regarding any case of misuse. 

### Author
I'll add this later.
