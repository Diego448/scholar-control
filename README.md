# Initial project setup
## Prerquisites
You need to have the following programs installed to setup your development environment
* Python 3.8
* Flask
* Eve
* MongoDB
* Python IDE
* git

## Additional software and tools
* Visual Studio Code
* MongoDB Compass
* Postman
* Google Chrome

## Getting the source code
Clone this repo using the command git clone into your machine
`$ git clone https://github.com/Diego448/scholar-control.git`

## Preparing your local environment
Navigate to the project folder and create a new virtual environment using python 3 tools
`python3 -m venv .`
or
`python -m venv .`

Activate your newly created virtual environment
`Scripts\activate` or `bin/activate.sh`

After creating the new virtualenvironment install the required frameworks and modules using pip
`python3 -m pip -r requirements.txt`
or
`python -m pip -r requirements.txt`

## Starting the servers
To start both frontend and backend servers use the following commands
### Eve
`python3 restapi/restapp.py`
or 
`python restapi\restapp.py`

### Flask
`source setup.sh`
or
`start.bat`