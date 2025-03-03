import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Weather Website URL
URL = "https://www.timeanddate.com/weather/canada/vancouver"

# Function to scrape weather data
def scrape_weather():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract temperature
    temp_element = soup.find("div", class_="h2")
    temp = temp_element.text.strip().replace("°", "").replace("\xa0", "").strip() if temp_element else "N/A"

    # Extract weather condition
    condition_element = soup.select_one("#qlook p")
    condition = condition_element.text.strip() if condition_element else "N/A"

    # Extract humidity from the detailed weather table
    humidity = "N/A"
    weather_table = soup.find("table", class_="table")

    if weather_table:
        for row in weather_table.find_all("tr"):
            key_element = row.find("th")
            value_element = row.find("td")

            if key_element and value_element:
                key = key_element.text.strip()
                value = value_element.text.strip()

                if "Humidity" in key:
                    humidity = value.replace("%", "").strip()
    temp_cleaned = ''.join(filter(str.isdigit, temp)) 
    # Store in dictionary
    weather_data = {
        "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         # Keeps only numbers

        "Temperature_C": int(temp_cleaned) if temp_cleaned else None,
        "Weather_Condition": condition,
        "Humidity": int(humidity) if humidity != "N/A" else None,
    }

    return weather_data

# Function to store data in SQLite
def save_to_db(weather_data):
    conn = sqlite3.connect("weather_analysis.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        Timestamp TEXT,
        Temperature_C INTEGER,
        Weather_Condition TEXT,
        Humidity INTEGER
    )
    """)

    # Insert data
    cursor.execute("""
    INSERT INTO weather (Timestamp, Temperature_C, Weather_Condition, Humidity)
    VALUES (?, ?, ?, ?)
    """, (weather_data["Timestamp"], weather_data["Temperature_C"], weather_data["Weather_Condition"], weather_data["Humidity"]))

    conn.commit()
    conn.close()

# Function to suggest clothing based on weather
def clothing_advice(condition, temp):
    advice = "Wear comfortable clothes."
    if "rain" in condition.lower() or "sprinkle" in condition.lower():
        advice = "🌧️ Take an umbrella or raincoat!"
    elif "snow" in condition.lower():
        advice = "❄️ Wear boots and warm layers!"
    elif "cloudy" in condition.lower():
        advice = "☁️ Wear a light jacket."
    elif "sunny" in condition.lower():
        advice = "☀️ Wear sunglasses and light clothing."
    
    if temp and temp < 5:
        advice += " 🧣 It's quite cold, wear a warm coat!"
    elif temp and temp > 25:
        advice += " 🕶️ It's hot outside, wear sunscreen!"
    
    return advice

# Function to visualize temperature and humidity trends


# Fetch, store, and visualize data
weather_data = scrape_weather()

if weather_data:
    save_to_db(weather_data)
    print(f"✅ Data Saved Successfully!\n📅 {weather_data['Timestamp']}\n🌡️ {weather_data['Temperature_C']}°C\n🌥️ {weather_data['Weather_Condition']}\n💧 {weather_data['Humidity']}%")
    print(f"👕 Advice: {clothing_advice(weather_data['Weather_Condition'], weather_data['Temperature_C'])}")
   
else:
    print("❌ Failed to fetch weather data.")
