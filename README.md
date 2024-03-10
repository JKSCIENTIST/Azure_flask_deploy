This is a Flask web application which is been hosted using Azure Web App!

The process is simple,

Step 1:
=> Develop your flask code in your local machine and test it.
=> Push the code into git .

Step 2:
=> Create an Azure account if you don't have one!
=> Click on create a resource
=> Search for "Web App"

Step 3:
=> Select the Web App
=> Click "Create"

Step 4:
=> Give all the details about your app.
=> Give a good name for the Resource group which is like a folder which manages your resources!
=> After providing the details you want, Go to Review+Create and Create a Web App

Step 5:
=> Go to deployment center and connect the Web App with your github repo.
=> Now Deploy the changes and restart the app

Step 6:
=> It will create a Yaml file with configurations, which contains pip install -r requirements.txt
=> Now we have two methods,

1. Create a requirements.txt file and give the requirements of the flask environment. (OR)
2. Take away that pip install -r requirements.txt from the yaml file and add pip install flask instead so that the virtual environment created will be capable of running the flask app without any issues.

=> It is advisable to go for the first method if you have many requirements to be installed. If not second one is more than enough.

Step 7:
=> Commit the changes and restart the Web App from the Azure Console.
=> Go to Overview and click the Default Domain name which will redirect you to the Hosted Web App.
=> The Web App takes about 3 - 4 min to build the app.
=> Check the logs for status of the build.
=> If it says Successful, then you are good to go and the output is displayed on the Web App.
=> If it says Failed, then check your code for any errors (Step 1 is to test it locally), Check the Yaml file, Check the github repo for any changes to be done, check the website on other browsers.


![image](https://github.com/JKSCIENTIST/Azure_flask_deploy/assets/136571338/951505c1-e488-4ce5-b19e-6857dcabf4fd)

Successfully Deployed a Flask Web App using Azure Web App!!
