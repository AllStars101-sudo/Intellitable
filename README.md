# Intellitable
Intellitable is a Django web app that uses Machine Learning to predict future exam marks of students and also uses Data Analysis using Pandas to analyse students' marks.

The basics:
To run this app make sure to run it as part of your current directory by running 'cd' or similar in your terminal (please download the entire folder and enter the path in terminal). 
For example, '~/Downloads/Intellitable'.

Pre-requisites to ensure before running app server:
Install the following modules in terminal with python on your path:
1. pip install django
2. pip install numpy==1.19.3
3. pip install pandas
4. pip install sklearn
5. pip install requests

For safety, run 'python manage.py makemigrations' and 'python manage.py migrate' to ensure no errors.
Next, type in 'python manage.py runserver' and wait for it to finish system checks.
Now open your browser and type in 'http://127.0.0.1:8000' or 'localhost:8000' to display the contents of the app.

Note: the above commands *must* be written only after ensuring that the Intellitable folder is on your terminal path. To terminate the app, just hit cmd+c or ctrl+c.
Thank you for using Intellitable.
