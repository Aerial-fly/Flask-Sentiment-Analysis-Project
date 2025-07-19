# local_model.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import streamlit as st

# Menggunakan cache agar model tidak dilatih berulang kali
@st.cache_resource
def get_model():
    print("--- Melatih model (ini hanya akan jalan sekali saat server start) ---")
    
    data = {
        'teks': [
            # Positif
            'produk ini sangat bagus dan berkualitas', 'saya sangat senang dengan pelayanannya',
            'pengiriman cepat dan barang aman', 'rasanya enak sekali, saya suka',
            'aplikasi ini sangat membantu pekerjaan saya', 'kualitasnya memuaskan',
            'desainnya bagus banget', 'saya puas dengan hasilnya',
            'harganya murah tapi kualitasnya oke', 'pokoknya mantap',
            'kamu sangat pintar dan solutif', 'penjelasannya mudah dimengerti',
            'keren banget fiturnya', 'saya akan merekomendasikan ini',
            'pelayanannya ramah dan cepat',
            # Negatif
            'saya kecewa dengan produknya', 'pelayanan sangat buruk dan tidak ramah',
            'pengiriman sangat lambat, saya tidak suka', 'barang yang datang rusak dan tidak sesuai',
            'aplikasi ini sering error dan lambat', 'kualitasnya buruk sekali',
            'harganya mahal tapi jelek', 'sangat tidak memuaskan',
            'saya tidak akan beli lagi di sini', 'mengecewakan',
            'penjelasannya bikin bingung', 'responnya tidak membantu sama sekali',
            'kamu pemalas dan tidak niat kerja', 'jelek banget, jangan dibeli',
            'saya rugi beli ini'
        ],
        'sentimen': [
            'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif', 'positif',
            'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif', 'negatif'
        ]
    }
 
    df = pd.DataFrame(data)
    X = df['teks']
    y = df['sentimen']

    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X, y)
    
    return model