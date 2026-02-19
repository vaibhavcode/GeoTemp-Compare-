import pandas as pd
import matplotlib.pyplot as plt
import requests

#this programme imports geocodes of two places from user and compare temprature
city1 = str(input("Enter the name of the first city"))
lat1 = float(input("Enter the latitude of the first city"))
long1 = float(input("Enter the longitude of the first city"))
city2 = str(input("Enter the name of the second city"))
lat2 = float(input("Enter the latitude of the second city"))
long2 = float(input("Enter the longitude of the second city"))

url1 =  f"https://api.open-meteo.com/v1/forecast?latitude={lat1}&longitude={long1}&current=temperature_2m"
url2 =  f"https://api.open-meteo.com/v1/forecast?latitude={lat2}&longitude={long2}&current=temperature_2m"
data1 = requests.get(url1).json()
data2 = requests.get(url2).json()
temp1 = data1["current"]["temperature_2m"]
temp2 = data2["current"]["temperature_2m"]
elev1 = data1["elevation"]
elev2 = data2["elevation"]  

df = pd.DataFrame({
        "City": [city1, city2],
        "Temperature (°C)": [temp1, temp2],
        "Elevation (m)": [elev1, elev2]
    })

def tab():
    print("The temperature and elevation comparison in tabular form:",df)
def visele():
    plt.figure()
    plt.bar(df["City"], df["Elevation (m)"])
    plt.xlabel("City")
    plt.ylabel("Elevation (meters)")
    plt.title("Elevation Comparison")
    plt.show()
def vistemp():
    plt.figure()
    plt.bar(df["City"], df["Temperature (°C)"])
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.title("Current Temperature Comparison")
    plt.show()
print("IF YOU WANT TO SEE THE COMPARISON IN TABULAR FORM ENTER 1\n")
print("IF YOU WANT TO SEE COMPARISON GRAPH OF CITY VS ELEVATION ENTER 2\n")
print("IF YOU WANT TO SEE COMPARISON GRAPH OF CITY VS TEMPERATURE ENTER 3\n")
print("ENTER 4 TO EXIT")
ch = int(input("Please enter your choice : "))
if ch==1:
      tab()
if ch==2:
      visele()
if ch==3:
      vistemp()
if ch==4:
      exit()



