import yfinance as yf
import pandas as pd

def fetch_stock_news(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        news_list = stock.news
        
        if not news_list:
            return pd.DataFrame()

        processed_news = []
        for item in news_list:
            # .get() with a default value prevents "None"
            processed_news.append({
                "Title": item.get('title') or "Headline Unavailable",
                "Publisher": item.get('publisher') or "Source Unknown",
                "Time": pd.to_datetime(item.get('providerPublishTime'), unit='s') if item.get('providerPublishTime') else "N/A",
                "Link": item.get('link') or "#"
            })
            
        return pd.DataFrame(processed_news)
    except Exception:
        return pd.DataFrame()