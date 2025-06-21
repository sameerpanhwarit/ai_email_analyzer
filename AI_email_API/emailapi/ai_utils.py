import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the Hugging Face API Key from environment
HF_API_KEY = os.getenv("API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"} if HF_API_KEY else {}

def hf_summarize(text):
    API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
    
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    
    if response.status_code != 200:
        print("❌ Summary API failed:", response.status_code)
        print("🔍 Response:", response.text)
        return "Summary unavailable"

    try:
        result = response.json()
        return result[0]['summary_text']
    except Exception as e:
        print("❌ JSON decode error in summarizer:", e)
        print("🔍 Raw response:", response.text)
        return "Summary parse error"

def hf_sentiment(text):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    
    if response.status_code != 200:
        print("❌ Sentiment API failed:", response.status_code)
        print("🔍 Response:", response.text)
        return "Unknown"

    try:
        result = response.json()
        return result[0]['label'].capitalize()
    except Exception as e:
        print("❌ JSON decode error in sentiment:", e)
        print("🔍 Raw response:", response.text)
        return "Parse error"

def analyze_email(text):
    print("📥 Incoming text:", text)

    # Only summarize if text is long
    if len(text.split()) > 30:
        summary = hf_summarize(text)
    else:
        summary = text

    sentiment = hf_sentiment(text)

    # Very basic rule-based urgency check
    urgency = "High" if any(word in text.lower() for word in ["urgent", "asap", "immediately", "important"]) else "Low"

    print("✅ Analysis result:", {
        "summary": summary,
        "sentiment": sentiment,
        "urgency": urgency
    })

    return summary, sentiment, urgency
