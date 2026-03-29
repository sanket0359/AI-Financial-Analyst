import os
from groq import Groq
from dotenv import load_dotenv

# 1. Load the API key from the .env file
load_dotenv()

# 2. Get the key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# 3. Initialize the Groq client
client = Groq(api_key=api_key)

def analyze_sentiment(news_titles):
    """
    Analyzes stock news headlines and returns a formatted financial verdict.
    """
    # Filter out empty or None titles
    clean_titles = [str(t) for t in news_titles if t is not None]
    
    if not clean_titles:
        return "No valid news titles found to analyze."

    combined_titles = "\n- ".join(clean_titles)
    
    # Using Llama 3.3 70B for high-quality financial reasoning
    prompt = f"""
    You are a professional financial analyst. Analyze the following news headlines and provide:
    1. VERDICT: (Bullish, Bearish, or Neutral)
    2. EXPLANATION: (A 2-sentence summary of the market mood)
    3. CONFIDENCE: (A score from 1-10)

    Headlines:
    {combined_titles}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3, # Low temperature for consistent analysis
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error in AI Analysis: {e}"