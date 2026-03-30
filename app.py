import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetcher import fetch_stock_news, fetch_stock_price
from sentiment_analyzer import analyze_sentiment

st.set_page_config(page_title="AI Financial Analyst", layout="wide")

st.title("📈 AI Financial News & Market Analyst")

# Sidebar
with st.sidebar:
    st.header("Search")
    ticker = st.text_input("Enter Ticker (e.g., RELIANCE.NS, TSLA)", value="RELIANCE.NS")
    analyze_btn = st.button("Analyze Market", type="primary")

if analyze_btn:
    # --- 1. Fetch Price Data ---
    price_data = fetch_stock_price(ticker)
    
    if price_data:
        st.subheader(f"📊 {ticker} Live Metrics")
        m1, m2, m3, m4 = st.columns(4)
        
        m1.metric("Current Price", f"₹{price_data['Close']}")
        m2.metric("Open", f"₹{price_data['Open']}")
        m3.metric("High/Low", f"₹{price_data['High']} / ₹{price_data['Low']}")
        
        # Determine color for the change metric
        delta_val = f"{price_data['Pct_Change']}%"
        m4.metric("Day Change", delta_val, delta=f"{price_data['Change']}", delta_color="normal")
    
    st.divider()

    # --- 2. Fetch News & Analysis ---
    with st.spinner("Analyzing news sentiment..."):
        df_news = fetch_stock_news(ticker)
        
        col1, col2 = st.columns([2, 1])

        if not df_news.empty:
            with col1:
                st.subheader("Latest Headlines")
                st.dataframe(df_news, use_container_width=True, hide_index=True)

            with col2:
                st.subheader("AI Verdict")
                titles = df_news['Title'].tolist()[:5]
                analysis = analyze_sentiment(titles)
                
                # Visual logic for the verdict box
                if "Bullish" in analysis: st.success(analysis)
                elif "Bearish" in analysis: st.error(analysis)
                else: st.warning(analysis)
                
                # Sentiment Chart
                sentiment_label = "Bullish" if "Bullish" in analysis else "Bearish" if "Bearish" in analysis else "Neutral"
                chart_df = pd.DataFrame({
                    "Sentiment": ["Positive", "Neutral", "Negative"],
                    "Score": [70, 20, 10] if sentiment_label == "Bullish" else [10, 20, 70] if sentiment_label == "Bearish" else [33, 33, 34]
                })
                fig = px.pie(chart_df, values='Score', names='Sentiment', hole=0.5,
                             color='Sentiment', color_discrete_map={'Positive':'#00cc96', 'Neutral':'#636efa', 'Negative':'#ef553b'})
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("💡 No news headlines found for this ticker today, but you can see the price movement above!")

st.divider()
st.caption("Developed by Sanket | Data Analyst Intern | Data Source: Yahoo Finance & Groq Llama 3.3")