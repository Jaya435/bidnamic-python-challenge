<img src="logo.png" alt="drawing" width="500"/>

# Python Software Engineering Challenge

This Repository contains a python project that can insert several CSV files into a PostgreSQL
database, calculates the Return on Ad Spending, and display the data and a couple of custom queries
on an API.

## Getting Started

These instructions will let you get a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live
system.

### Prerequisites

You will need to run this programme using Python3. You can follow a guide here to install Python3
on your local machine https://installpython3.com/. Once Python3 is installed, you can run this
programme from within a virtual environment.

#### You will need a PostgreSQL server for testing and deployment, this can be done in two ways:

- With docker installed:
```
docker run -p 5432:5432 -e POSTGRES_USER=raos -e POSTGRES_DB=raos -e
POSTGRES_PASSWORD=mysecretpassword --name raos-db -d postgres
```
- With PostgreSQL installed:
```
psql -U postgres -p 5432 -h localhost
CREATE USER raos WITH PASSWORD mysecretpassword CREATEDB;
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository onto your local machine
```
https://github.com/Jaya435/bidnamic-python-challenge.git
```
Create your Python 3 virtual environment and install all requirements
```
make install
```
to activate the venv use:
```
make activate
```

To run a development web server
```
make runserver
```

To perform code formatting
```
make blake
```
To perform code linting
```
make flake8
```

Other make commands to aid development are available on the commandline.


## Running the tests

The automated tests can be run using the below command:
```
make test
```

## Using the Web Server
Once you have run:
```
make runserver
```
The API endpoints can be viewed at:
```
http://localhost:8000/api/
```
Two view the top ten ROAS by structure_value:
```
http://localhost:8000/api/structure-value/ellesse/
```
Two view the top ten ROAS by alias:
```
http://localhost:8000/api/alias/Shift - Shopping - GB - net1 - HIGH - april-washington-virginia-alanine - 8ac32f611b0940a39fa5e822184089d3/
```


## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
