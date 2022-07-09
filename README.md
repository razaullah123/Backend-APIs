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
password  **Sent to the user email**
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
(http://127.0.0.1:8000/vehicles/category/)
###### Method  
POST
###### Payload
title
token
###### Result
{
    "title": "Bus"
}

###### API for Updating a Category
(http://127.0.0.1:8000/vehicles/category/1/)
###### Method  
PATCH
###### Payload
title
token
###### Result
{
    "title": "Cars"
}

###### API for Getting all Categories
(http://127.0.0.1:8000/vehicles/category/)
###### Method  
GET
###### Result
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Bus"
        },
        {
            "title": "Sedan"
        },
        {
            "title": "SUV"
        }
    ]
}

###### API for Getting all Categories
(http://127.0.0.1:8000/vehicles/category/1/)  
###### Method  
DELETE  
###### Payload
token
**Note: Before deleting a category we should delete the cars in that category because the category field is a foreign key in the Car model and on_delete is Protected**
###### Result
Category with the mentioned id will be deleted from the database

###### API for Creating a Car
###### Method  
POST
###### Payload
color  
model  
register_num  
category 
token
###### Result
{  
    "color": "Blue",  
    "model": 2005,  
    "register_num": 1988,  
    "category": 2,  
    "register_cars": 3  
}  
###### API for Getting all registered Cars
(http://127.0.0.1:8000/vehicles/car/)
###### Method 
GET
###### Payload
Token 
###### Result
{
    "count": 3,  
    "next": null,  
    "previous": null,  
    "results": [  
        {  
            "color": "Black",  
            "model": 2007,  
            "register_num": 1988,  
            "category": 2,  
            "register_cars": 3  
        },  
        {  
            "color": "Blue",  
            "model": 2005,  
            "register_num": 1988,  
            "category": 2,  
            "register_cars": 3  
        },  
        {  
            "color": "white",  
            "model": 2006,  
            "register_num": 1988,  
            "category": 2,  
            "register_cars": 3  
        }  
    ]  
}  

###### API for Getting a Single Car Record
(http://127.0.0.1:8000/vehicles/car/2)
###### Method 
GET
###### Payload
Token 
###### Result
{  
    "color": "Black",  
    "model": 2007,  
    "register_num": 1988,  
    "category": 2,  
    "register_cars": 2  
}  

###### API for Updating a Registered Car
(http://127.0.0.1:8000/vehicles/car/1/)
###### Method
PUT
###### Payload
color
model
token
###### Result
{
    "color": "purple",
    "model": 2010,
    "register_num": 1314,
    "category": 2,
    "register_cars": 3
}
###### API for Deleting a Car
(http://127.0.0.1:8000/vehicles/car/1/)
###### Method
DELETE
###### Payload
token
###### Result
Car with the mentioned id will be deleted from the database