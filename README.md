# moip-tech-challenge
An web application that provides an API for payment to customers and a checkout for who don't want to integrate with the API.

## Getting Started
These instructions will get you a version of the project up and running on your local machine.

### Prerequisites

* MongoDB
* Python

### Installing
First you'll have to install the MongoDB Community Server, v3.6.5 or more

And then you'll have to install the Python v3.5 or more

### Running

#### Database

First, execute your MongoDB Server that by default must be on the folder: 
> Program Files/MongoDB/Server/x.x/bin/mongod.exe

Then you'll have to start a new database executing:
> Program Files/MongoDB/Server/x.x/bin/mongo.exe

And running the code on the terminal:
> use challenge

That's it for the database.

#### Application
  
After cloning the project, on the terminal go to the folder and run:

> pip install virtualenv

Then, run to create a virtual environment with the python libraries:

> virtualenv venv --distribute

After that, execute:

> venv\Scripts\activate

so you can install the application requirements, using:

> pip install -r requirements.txt

At the end just run

> python src/run.py

and your application should be up and running.

### Testing

To run the unit tests, you'll just need to run:

> python -m unittest


### Documentation

The API Documentation can be seen here:

https://documenter.getpostman.com/view/1879456/RWEfNfNN