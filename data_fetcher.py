import yfinance as yf
import pandas as pd

def fetch_stock_price(ticker_symbol):
    """
    Fetches the open, close, high, and low for today vs yesterday.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        # Fetch 5 days to ensure we have enough data for a 'Change' calculation
        hist = stock.history(period="5d")
        
        if hist.empty:
            return None

        latest_day = hist.iloc[-1]
        prev_day = hist.iloc[-2] if len(hist) > 1 else latest_day

        return {
            "Open": round(latest_day['Open'], 2),
            "High": round(latest_day['High'], 2),
            "Low": round(latest_day['Low'], 2),
            "Close": round(latest_day['Close'], 2),
            "Change": round(latest_day['Close'] - prev_day['Close'], 2),
            "Pct_Change": round(((latest_day['Close'] - prev_day['Close']) / prev_day['Close']) * 100, 2)
        }
    except Exception as e:
        print(f"--- DEBUG PRICE ERROR: {e} ---")
        return None

def fetch_stock_news(ticker_symbol):
    """
    Fetches the latest news headlines.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        news_list = stock.news
        
        if not news_list:
            return pd.DataFrame()

        processed_news = []
        for item in news_list:
            processed_news.append({
                "Title": item.get('title') or "Headline Unavailable",
                "Publisher": item.get('publisher') or "Source Unknown",
                "Time": pd.to_datetime(item.get('providerPublishTime'), unit='s') if item.get('providerPublishTime') else "N/A",
            })
            
        return pd.DataFrame(processed_news)
    except Exception as e:
        print(f"--- DEBUG NEWS ERROR: {e} ---")
        return pd.DataFrame()