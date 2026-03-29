import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from data_fetcher import fetch_stock_news
from sentiment_analyzer import analyze_sentiment

# 1. Page Configuration
st.set_page_config(page_title="AI Financial News Analyst", layout="wide", page_icon="📈")

# Custom CSS to make it look modern
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 AI Financial News Analyst")
st.caption("Real-time sentiment analysis powered by Llama 3.3 & Yahoo Finance")

# 2. Sidebar Settings
with st.sidebar:
    st.header("Control Panel")
    ticker = st.selectbox("Select Ticker", ["RELIANCE.NS", "HDFCBANK.NS", "ICICIBC.NS", "AAPL", "TSLA", "NVDA"])
    analyze_btn = st.button("Generate Analysis", type="primary")
    
    st.divider()
    # Weekend Check
    is_weekend = datetime.datetime.now().weekday() >= 5
    if is_weekend:
        st.info("🗓️ Markets are currently closed. Showing latest available news.")

# 3. Main Logic
if analyze_btn:
    with st.spinner(f"🔍 Analyzing {ticker}..."):
        # Fetch Data
        df = fetch_stock_news(ticker)
        
        if df.empty:
            st.error(f"No news data found for {ticker}. Please try another symbol.")
        else:
            # Layout: Top Row for Charts
            col_chart1, col_chart2 = st.columns([1, 1])
            
            # AI Analysis First to get Sentiment for Charts
            titles = df['Title'].tolist()[:5]
            analysis_text = analyze_sentiment(titles)
            
            # Determine sentiment for visualization
            sentiment = "Neutral"
            if "Bullish" in analysis_text: sentiment = "Bullish"
            elif "Bearish" in analysis_text: sentiment = "Bearish"

            with col_chart1:
                st.subheader("Market Sentiment")
                # Dynamic Pie Chart based on AI verdict
                colors = {'Positive': '#00cc96', 'Neutral': '#636efa', 'Negative': '#ef553b'}
                val_map = {"Bullish": [75, 15, 10], "Bearish": [10, 15, 75], "Neutral": [30, 40, 30]}
                
                chart_df = pd.DataFrame({
                    "Category": ["Positive", "Neutral", "Negative"],
                    "Score": val_map[sentiment]
                })
                fig = px.pie(chart_df, values='Score', names='Category', hole=0.4,
                             color='Category', color_discrete_map=colors)
                fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
                st.plotly_chart(fig, use_container_width=True)

            with col_chart2:
                st.subheader("AI Analyst Verdict")
                if sentiment == "Bullish":
                    st.success(analysis_text)
                elif sentiment == "Bearish":
                    st.error(analysis_text)
                else:
                    st.warning(analysis_text)

            st.divider()

            # 4. News Table (Cleaned)
            st.subheader("📰 Latest Headlines")
            # Cleaning: Ensure no "None" is displayed in the UI
            df_display = df[['Title', 'Publisher', 'Time']].copy()
            df_display = df_display.fillna("Not Available")
            
            st.dataframe(df_display, use_container_width=True, hide_index=True)

# Footer
st.divider()
st.caption(f"Developed by Sanket | Data Analyst Intern | {datetime.datetime.now().strftime('%Y-%m-%d')}")