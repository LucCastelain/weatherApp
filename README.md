# <h1> Weather app <h1>
<h2>Files in the repository</h2>

* app.py : basically the app file. It contains all the endpoint needed to add sensors to database and to query information from them. It creates the server using flask.
* createDatabase.sql : SQL file to create a file database.db containing a table sensor. It adds 1 default sensor in the table.
* initDatabase.py : this file can e executed with python to create the database if not already created. It executes the code inside the createDatabase.sql file.
* database.db : the database file.

<h2>database</h2>
The database was made using SQLite. It allows the data to persist and it was easier to have only one database file inside the repository of the project.
The database has only one table named "sensors". This table contains 3 columns :

* id : PRIMARY KEY AUTOINCREMENT
* country : VARCHAR(255), big enough to have any country name but not as big as TEXT type
* city : VARCHAR(255)

No arbitrary data for sensors are stored.

<h2>How it works</h2>
You do not have to use initDatabase.py file as the database file is already in the repository.

It is easier to execute the app on a Linux, Unbuntu, MacOS or any similar system but Windows.
First you need to run the virtual environment. To do so, open a terminal/shell inside the repository of the project and run the command : 
<pre>
    $ source env/bin/activate
</pre>
Then run the command :
<pre>
    $ flask run
</pre>
The server is running in localhost, as for this exercice I did not think it was useful to really make it run online.
If the server is still not running. You may need to install flask with pip once the virtual environment is run ($ pip install flask). And then also install the requests module :
<pre>
    $ pip install requests
</pre>
Then you may need to indicate to flask where is the app. Run the following commands inside the terminal :
<pre>
    $ export FLASK_APP = app
    $ export FLASK_ENV = development
</pre>

Once the server is running, you will have 2 usable endpoints:
* /registerSensor : this endpoint allows user to save a new sensor to the database. It takes to parameters, "countryName" and "cityName", which are both strings.
So, if you want to save a new sensor in the database, this endpoint will look like this : http://127.0.0.1:5000/registerSensor?countryName=Ireland&cityName=Galway . The id of the added sensor is automatically incremented based on the last added sensor.
* /getSensor : this endpoint allows user to query sensor(s)' data. It takes one parameter, "sensorsID". This parameter can be a string named "all" to query all sensors' data. It can also be a number to query the data from one sensor. Or it can be numbers separated by coma to query data from multiple sensors. For examples, this endpoint can looks like this :
http://127.0.0.1:5000/getSensor?sensorsID=1
http://127.0.0.1:5000/getSensor?sensorsID=1,2
http://127.0.0.1:5000/getSensor?sensorsID=all

Once sensors information are queried. I used OpenWeatherMap service, which provide weather data based on the location (here the city of the sensor).
As I did not know if the user had to choose the metrics, only two metrics are queried thanks to the sensor information.
I did not get the date range, therefore I only get the metrics of the current date, not an average of the chosen date range.

The app is a REST API as asked and do not have any UI. Following the rules of the exercise, I did not use any HTML, but I could have.