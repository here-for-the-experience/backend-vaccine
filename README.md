# Backend for Verifying and Generating Vaccines for Users

A Fastapi backend for Verifying whether an user has taken then vaccine by an admin and creating vaccination certificate for them.

## Features
+ Unpacks Requests, extracts and verifies OAuth parameters from headers.
+ Supports GET and POST request.
+ Written in Python, with minimal dependencies.
+ Talks to database for generating vaccination certificate and sends it to the client.

## Non-Features
+ There is no feature of booking a date for vaccination.
+ Vaccination certificate will be the same for everyone.
+ Do not allow users to choose which vaccine they want to take.

## Building

At first Clone the repository using : 
```
git clone 'url'
```

Vaccination Backend can be built and run in two ways :
1. using your own machine, or 
2. Using Docker

### If you have docker installed in your machine, you can run :
```
docker build -t image-name --build-arg  URL="DATABASE URL" --build-arg SECRET_TOKEN="SECRET TOKEN FOR JWT"  .
```
As soon as the building finishes, you can run :
```
docker run image-name:tag-name 
```
And the application should start running.


### Otherwise, you can install the dependencies at first using 
```
pip install -r requirements.txt
export URL="DATABASE URL"
export SECRET_TOKEN="SECRET TOKEN FOR JWT"
uvicorn app.main:app --reload
```


And the application should start running.

#### If you make some changes in the tables, you should run :
```
alembic revision --autogenerate -m "Revision Version"
alembic upgrade head
```
![image](https://github.com/here-for-the-experience/backend-vaccine/assets/77661612/c4bcbdde-aa35-4aac-b031-f0a30ccc5d35)

## Understanding the Implementation 
  + The **/create/** route defines the endpoint for creating a new vaccine. Frontend will send a request in this api with a token and using that token we will create a vaccination table for that user with a random vaccine name from the **vaccine** table.
  + The **/myvaccine** route gives back the vaccination certification to the user to download.
  + The **/allvaccines** route can be only accessed by the admin. He can see all the pending vaccines using this route.
  + The **/approve** route can be only accessed by the admin also. He can approve a vaccination using this route.
  + The **schemas** module defines the schemas for Vaccine, Vaccination, Approve and Token to generate vaccine and validate requests.
  + We have used **alembic** to manage our database schema in a version-controlled way. This means that you can track changes to your schema over time, and easily roll back to a previous version if necessary.

## Usage

Sqlalchemy model to define the Vaccination table is given below :
```
class Vaccination(Base) :
    __tablename__ = "vaccination_table"
    id = Column(Integer,primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    vaccine_id = Column(Integer, nullable=False, default=1)
    vaccination_date = Column(Date, nullable = False)
    verified = Column(Boolean, nullable=False, default=False)
    certificate_url = Column(String, nullable=True, default = None)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
```
Sqlalchemy model to generate a Vaccine table with names is given below :

```
class Vaccine(Base) :
    __tablename__ = "vaccine_table"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable = False)
```

## Running Tests 
 Run :
```
pytest
```

## Reporting Problems 
You can send us a mail at :
+ iam.reduan@gmail.com
+ Raufun.nazin13@gmail.com
+ shakil.csedu@gmail.com

## Contributors 
+ Alve Reduan
+ Fahim Shakil
