# Test Task for Python Developer Position

## Cloning the repository

###### Clone the repository using the command below :
[git clone] (https://github.com/razaullah123/Ropstam.git)

## Project Setup

###### Move into the directory where we have the project files :
cd Ropstam

###### Install virtualenv :
pip install virtualenv

###### Create a virtual environment
python3 -m venv virtual_environment_name

###### Activate the virtual environment :
source virtual_environment_name/bin/activate

###### Install the requirements :
pip install -r requirements.txt


## Running the App
###### To run the App, use:  
python manage.py runserver

## Project API's
###### Sign Up API
(http://127.0.0.1:8000/auth/registration/)

###### Payload  
username  
email  

###### Result
{
    "result": "User Register Successfully",
    "username": "mujeeb"
}