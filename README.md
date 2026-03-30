# 📈 AI Financial News & Market Analyst

An AI-driven intelligence dashboard that provides a 360-degree view of stock market health. By combining **Live Price Metrics** (Structured Data) with **LLM Sentiment Analysis** (Unstructured Data), this tool helps investors quantify market "mood" during periods of high volatility.

---

## 🚀 Core Features

* **Live Market Metrics:** Real-time tracking of Today's Open, High, Low, and Current Price using `yfinance`.
* **Dynamic Change Indicators:** Instant visualization of price movement with color-coded "Day Change" metrics (Green/Red).
* **AI-Powered Sentiment:** Leverages **Llama 3.3 70B** (via Groq) to analyze the latest headlines and provide a professional financial verdict.
* **Dual-Signal Dashboard:** Displays both numerical price action and textual news sentiment side-by-side.
* **Security Focused:** Implements environment variable management (`.env`) to ensure API credentials remain private.

---

## 🛠️ Technical Stack

* **Frontend:** Streamlit (Python-based Web Framework)
* **AI/NLP:** Groq API (Model: `llama-3.3-70b-versatile`)
* **Data Sources:** Yahoo Finance (via `yfinance`)
* **Processing:** Pandas & NumPy
* **Visualization:** Plotly Express
* **Version Control:** Git & GitHub

---

## ⚙️ How to Run Locally

1. **Clone the Project:**
   ```bash
   git clone [https://github.com/sanket0359/AI-Financial-Analyst.git](https://github.com/sanket0359/AI-Financial-Analyst.git)
   cd AI-Financial-Analyst
