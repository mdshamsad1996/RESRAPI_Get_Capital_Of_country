 ####  Instruction 
 Run API using below locatlhost url
 
        http://localhost:8080/getcapital/<string:country_name>
        
Run API using below ngrok url

        http://bb08993a.ngrok.io/getcapital/<string:country_name>
            or
        https://bb08993a.ngrok.io/getcapital/<string:country_name>


        
Make sure python (preferred python3.7) is added to path.

    python --version
        or		
    python3.7 --version
 
 
 Install virtualenv using pip.

         pip install virtualenv 
 
First create a virtual environment for the project.

    virtualenv -p python3.7 venv or virtualenv venv
         . venv/bin/activate (Linux)
         . venv/Scripts/activate (windows)
         
## Install dependencies

        pip install -r requirements.txt
    
This will install all the dependencies (pylint, pycodestyle, flask) mentioned in the requirements file.

#### To run app using below command
         python src/get_capital_of_country.py
    

##### Run unit Test case of app using below command
             python -m unittest tests/test_get_capital_of_country.py

#### Run Linters (To fix linters error)

    Run using pylint linter command
        pylint src (for src folder)
        pylint tests (for tests folder)
        
    Run using pycodestyle linter command
         pycodestyle src (for src folder)
         pycodestyle tests (for tests folder)
         ##### Generate url using ngrok

open ngrok.exe as administrator and type below command

        ngrk htttp portnumber(8080)
        
        
### Overview
 It is a REST API using Flask Python framework. The API take a country name and return it’s capital. The API have also basic error handling (e.g. Invalid country name), follow PEP8 coding conventions and also take care of unittest case
 
