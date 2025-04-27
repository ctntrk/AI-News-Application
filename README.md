# AI News Aggregator Pro

AI News Aggregator Pro is a Python-based web application built with Streamlit. The app collects real-time news related to Artificial Intelligence (AI) from multiple trusted sources and displays them in a user-friendly format. Users can search for specific keywords, filter news by time range (e.g., the last 7 days), and select from various sources to customize the content they want to read.

## AI News Aggregator Pro Demo Introduction Video

https://github.com/user-attachments/assets/5e67dfdc-a83b-4e7c-aeb2-afc03e135fa2

---

## Demo
You can try out the application and see it in action by visiting the link below:
 
[**AI News Application Demo**](https://ai-news-application.streamlit.app/)


⚠️ Note: Streamlit Cloud deploy may put the app to sleep if it’s not being actively used or if there’s low traffic. 💤

---


## Features

- **Real-Time AI News**: Aggregates AI-related news from multiple trusted sources.
- **Search Functionality**: Search news articles by keywords.
- **Date Filtering**: Filter news from the last 1 to 30 days.
- **Source-Based Filtering**: Choose which sources to pull news from.
- **Statistics**: View the number of articles from each selected source.
- **Mobile-Friendly Design**: Responsive layout for a great user experience across devices.

---

## Technologies Used

- **Python**: Programming language used to build the app.
- **Streamlit**: Web framework for creating the UI.
- **Feedparser**: Parses and handles RSS feeds.
- **BeautifulSoup**: Cleans HTML content for easy reading.
- **Datetime**: Handles and filters news based on dates.
---
## Data Sources

The app fetches news from the following AI-related sources:

- **TechCrunch**
- **MIT Technology Review**
- **Science Daily**
- **DeepMind Blog**
- **Berkeley AI Research (BAIR) Blog**

---
## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need to install the following Python libraries:

```bash
pip install streamlit feedparser beautifulsoup4
```

### Running the App

To run the app, use the following command in your terminal:

```bash
streamlit run app.py
```

This will start the app on `http://localhost:8501`.

---
## How It Works

1. **Fetching and Caching News**: The app fetches news from selected RSS feeds and caches it for 1 hour to improve performance.
2. **Keyword Search**: Users can enter a keyword to filter news articles by title or summary.
3. **Date Filtering**: The app allows filtering of news articles by a time range (1–30 days).
4. **Source Selection**: Users can choose which sources to fetch news from.
5. **Statistics**: The app shows the total number of articles from each selected source.
6. **Responsive Layout**: The app is designed to be mobile-friendly and adapts to different screen sizes.
---
## Artificial Intelligence News App Web Interface
![Alt text](https://github.com/ctntrk/AI-News-Application/blob/main/Artificial_Intelligence_News_App%20Web_Interface.jpg)
---
## News Info
![Alt text](https://github.com/ctntrk/AI-News-Application/blob/main/News_Info.jpg)

---

## License

This project is licensed under the MIT License.
