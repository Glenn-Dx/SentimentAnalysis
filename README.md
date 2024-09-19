# Sentiment Analysis on News Data for Stock Price Prediction

## Project Overview

This project aims to analyze the relationship between the sentiment of news articles and the actual stock price movement at specific moments in time. The project uses **web scraping** techniques to gather news data and **sentiment analysis** algorithms to determine the sentiment (positive, neutral, or negative) of these articles. The accuracy of the sentiment analysis model is evaluated by comparing its predictions with actual stock price movements, establishing whether there is a significant relationship between sentiment and stock price changes.

## Features

- **Web Scraping for News Data**: The project scrapes news articles related to specific stocks from various news websites.
- **Sentiment Analysis**: Sentiment of each news article is evaluated using NLP (Natural Language Processing) techniques.
- **Stock Price Data**: Historical stock prices for the same period as the news articles are fetched for comparison.
- **Sentiment-Price Correlation**: The sentiment score of the news articles is correlated with the stock price movement.
- **Model Accuracy**: The accuracy of sentiment analysis predictions is measured against real-world stock price data.

## Project Components

1. **Web Scraping**
   - Use of tools like **BeautifulSoup** and **Selenium** to scrape real-time or historical news articles from relevant financial websites.
   
2. **Sentiment Analysis**
   - **VADER** and **DistilBERT** are used to analyze the sentiment of the scraped articles.
   - Articles are categorized into three sentiment classes: positive, neutral, or negative.
   
3. **Stock Price Data**
   - Use of APIs like **Yahoo Finance** to retrieve historical stock price data.

4. **Sentiment-Stock Price Relationship**
   - A correlation matrix to quantify the relationship between sentiment and stock price changes.
   - Graphs and visualizations to display sentiment trends versus stock price movements.

5. **Accuracy Measurement**
   - Accuracy metrics are calculated to evaluate how well sentiment analysis predicts stock price direction (increase or decrease).

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your machine. Additionally, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Required Libraries

The following Python libraries are used in this project:

- `beautifulsoup4`
- `scrapy` or `selenium`
- `requests`
- `pandas`
- `numpy`
- `matplotlib`
- `yfinance` (or any stock price data API)
- `nltk`, `TextBlob`, or `VADER` for sentiment analysis

## Usage

This project is designed to analyze news sentiment and its potential impact on stock prices. It can be used to:

- Investigate whether news sentiment has a measurable effect on stock prices.
- Create trading strategies based on news sentiment.
- Monitor news outlets for sentiment bias regarding particular companies or stocks.

## Results

The project outputs various visualizations and metrics, such as:

- A graph comparing sentiment trends with stock price movements.
- Correlation matrices to evaluate the accuracy of the sentiment predictions.
- Correlation coefficients between sentiment scores and stock price movements.
