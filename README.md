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

###### Method  
POST

###### Payload  
username  
email  

###### Result
{
    "result": "User Register Successfully",
    "username": "mujeeb"
}  
**After Successful registration an email will be sent to the user mentioned email with a randomly generated password**
###### Sign In API
( http://127.0.0.1:8000/auth/sign-in/)

###### Method  
POST

###### Payload
username  
email  
password  
###### Result
{
    "result": "User login Successfully",  
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJhemFAeW9wbWFpbC5jb20iLCJ1c2VybmFtZSI6InJhemF1bGxhaCIsImlhdCI6MTY1NzMwNzgwNH0.dGOcISYWPIMskh0nhTigRtrJsawoaPwabFWo0m9Tgik",  
    "users":  [  
        {
            "id": 1,  
            "username": "razaullah",  
            "email": "raza@yopmail.com"  
        }  
    ]
}

###### API for Creating a Category
###### Method  
POST
###### Payload
title
###### Result
{
    "title": "Bus"
}