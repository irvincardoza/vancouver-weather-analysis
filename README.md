# 🌦️ Vancouver Weather Data Scraper & Analysis

## 📌 Overview
This Python project scrapes real-time weather data for Vancouver, stores it in an SQLite database, and provides visualization and clothing advice based on weather conditions.

## 🚀 Features
- Scrapes **current temperature, humidity, and weather conditions** from [Time and Date](https://www.timeanddate.com/weather/canada/vancouver).
- Stores **historical weather data** in an SQLite database (`weather_analysis.db`).
- Provides **clothing advice** based on weather conditions.
- Ensures **data integrity** by cleaning and formatting scraped values.

## 🛠️ Tech Stack
- **Python** (Data processing & API requests)
- **BeautifulSoup** (Web scraping)
- **SQLite3** (Database storage)
- **Pandas** (Data analysis)
- **Matplotlib** (Data visualization)

## 📊 Example Output
```
✅ Data Saved Successfully!
📅 2025-03-03 14:10:56
🌡️ 9°C
🌥️ Sprinkles. Cloudy.
💧 94%
👕 Advice: ☁️ Wear a light jacket. 🧣 It's quite cold, wear a warm coat!
```

## 🏆 Key Functionalities
- **🌐 Web Scraping**: Fetches real-time weather data.
- **🗄️ Data Storage**: Saves weather data in SQLite.
- **📊 Data Visualization** (Future Work): Plots historical trends.
- **🧥 Clothing Advice**: Suggests weather-appropriate outfits.

## 📜 License
MIT License - Free to use, modify, and distribute.
