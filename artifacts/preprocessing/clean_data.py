import pandas as pd
import re
import os
import spacy
from datetime import datetime
from sklearn.model_selection import train_test_split

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove special characters and punctuation (keep some for spacy parsing if needed, but let's follow the simple plan)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespaces
    text = " ".join(text.split())
    return text

def preprocess_data(input_path, output_path):
    print(f"Reading data from {input_path}...")
    # Read CSV with semicolon separator
    df = pd.read_csv(input_path, sep=';')
    
    if 'Ulasan' not in df.columns:
        print("Error: 'Ulasan' column not found in CSV.")
        return

    # Load Spacy model once
    print("Loading Spacy model...")
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Spacy model 'en_core_web_sm' not found. Please run 'python -m spacy download en_core_web_sm'")
        return

    print("Cleaning and lemmatizing text...")
    
    # Define aspects and keywords
    aspect_keywords = {
        'suara': ['suara', 'sound', 'jernih', 'treble', 'vocal'],
        'bass': ['bass', 'ngebass'],
        'pengiriman': ['kirim', 'pengiriman', 'sampai', 'cepat', 'kurir', 'ongkir'],
        'packing': ['packing', 'kemasan', 'bungkus', 'bubble'],
        'harga': ['harga', 'worth', 'murah', 'terjangkau']
    }

    sentiment_keywords = {
        'positive': ['bagus', 'mantap', 'oke', 'ok', 'puas', 'jernih', 'cepat', 'aman', 'awet', 'recomended', 'worth', 'sip'],
        'negative': ['kurang', 'lama', 'kecewa', 'penyok', 'cacat', 'mati', 'rusak', 'lelet', 'jelek']
    }

    def extract_absa_samples(row):
        raw_text = str(row['Ulasan'])
        cleaned_text = clean_text(raw_text)
        
        # Process with Spacy for lemmatization
        doc = nlp(cleaned_text)
        lemmatized_text = " ".join([token.lemma_ for token in doc])
        
        samples = []
        
        # Simple rule-based extraction
        for aspect, keywords in aspect_keywords.items():
            if any(k in lemmatized_text for k in keywords):
                sentiment = 'neutral'
                if any(pos in lemmatized_text for pos in sentiment_keywords['positive']):
                    sentiment = 'positive'
                if any(neg in lemmatized_text for neg in sentiment_keywords['negative']):
                    sentiment = 'negative'
                
                samples.append({
                    'ulasan': lemmatized_text,
                    'aspect': aspect,
                    'sentiment': sentiment
                })
        return samples

    # Flatten the ABSA samples
    all_samples = []
    for _, row in df.iterrows():
        all_samples.extend(extract_absa_samples(row))
    
    absa_df = pd.DataFrame(all_samples)
    absa_df_train, absa_df_test = train_test_split(absa_df, test_size=0.2, random_state=42)

    # Save to clean directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    absa_df.to_csv(output_path + '.csv', index=False)
    absa_df_train.to_csv(output_path + '_train.csv', index=False)
    absa_df_test.to_csv(output_path + '_test.csv', index=False)
    print(f"Processed ABSA data saved to {output_path}")

if __name__ == "__main__":
    # Define paths based on planning
    raw_dir = os.path.join("data", "raw")
    clean_dir = os.path.join("data", "clean")
    
    # Use the specific file found in data/raw
    input_file = "data_scrape_2026-05-08.csv"
    input_path = os.path.join(raw_dir, input_file)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = f"scraped-data_2026-05-08_cleaned_{date_str}"
    output_path = os.path.join(clean_dir, output_file)
    
    if os.path.exists(input_path):
        preprocess_data(input_path, output_path)
    else:
        print(f"Input file {input_path} not found.")
