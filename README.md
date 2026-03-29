# 📈 AI Financial News Analyst
An AI-powered dashboard that fetches real-time stock news and uses **Llama 3.3** (via Groq) to perform sentiment analysis.

## 🚀 Features
- **Real-time Data:** Fetches news directly from Yahoo Finance.
- **AI Insights:** Provides a Bullish/Bearish verdict with confidence scores.
- **Interactive Visuals:** Dynamic pie charts and metrics using Streamlit and Plotly.
- **Weekend Aware:** Intelligent handling of market-closed hours.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Model:** Llama-3.3-70b-versatile (Groq API)
- **Frontend:** Streamlit
- **Data Viz:** Plotly & Pandas

## ⚙️ Installation
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/AI-Financial-Analyst.git`
2. Install requirements: `pip install -r requirements.txt`
3. Add your Groq API key to a `.env` file.
4. Run: `streamlit run app.py`