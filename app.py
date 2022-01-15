from flask import Flask, request, url_for
import sqlite3
import json
import requests


app = Flask(__name__)
openWeatherMap_apiKey = "95c8668ed23df614d0e4b79c8684d317" # Used to get weather based on the city of sensors


def getDatabaseConnection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    return connection


@app.route("/")
def index():
    return "Hello API"


@app.route("/registerSensor", methods=("GET", "POST"))
def registerSensor():
    country = request.args.get("countryName")
    city = request.args.get("cityName")

    #if(request.method == "POST"): # Should be for input form
    if not (country):
        return "Country name is required !"
    elif not (city):
        return "City name is required !"
    else:
        connection = getDatabaseConnection()
        try:
            try:
                connection.execute("INSERT INTO sensors (country, city) VALUES (?, ?)", (country, city))
            except sqlite3.OperationalError as e:
                print(e)
                return e
        finally:
            connection.commit()
            connection.close()

        return "New sensor for " + city + " in " + country + " added to database."


@app.route("/getSensor")
def getSensor():
    sensorsID = []
    if(request.args.get("sensorsID") == "all"):
        sensorsID = request.args.get("sensorsID")
    elif("," in request.args.get("sensorsID")):
        sensorsID = request.args.get("sensorsID").split(",")
    else:
        sensorsID = int(request.args.get("sensorsID"))
    
    sensors = []
    connection = getDatabaseConnection()

    try:
        if(type(sensorsID) == str):
            try:
                sensors = connection.execute("SELECT * FROM sensors").fetchall()
            except sqlite3.OperationalError as e:
                print(e)
                return e

        elif(type(sensorsID) == int):
            try:
                sensors = connection.execute("SELECT * FROM sensors WHERE id = ?", (str(sensorsID))).fetchall()
            except sqlite3.OperationalError as e:
                print(e)
                return e
        else:
            for id in sensorsID:
                try:
                    sensors.append(connection.execute("SELECT * FROM sensors WHERE id = ?", (id)).fetchone())
                except sqlite3.OperationalError as e:
                    print(e)
                    return e

    finally:
        connection.close()

    result = {}
    for sensor in sensors:
        print("Sensor from ", sensor["city"], " in ", sensor["country"])

        openWeatherMap_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + openWeatherMap_apiKey + "&q=" + sensor["city"]
        jsonResponse = requests.get(openWeatherMap_url)
        response = jsonResponse.json()

        print("test")

        if(response["cod"] == "404"):
            result = str(sensor["city"]) + ": city not found."
            return result
        else:
            currentTemperature = response["main"]["temp"]
            currentHumidity = response["main"]["humidity"]

            sensorInformation = {}
            sensorInformation["id"] = sensor["id"]
            sensorInformation["country"] = sensor["country"]
            sensorInformation["city"] = sensor["city"]
            sensorInformation["temperature"] = currentTemperature
            sensorInformation["humidity"] = currentHumidity

            result[sensor["id"]] = sensorInformation


    return result