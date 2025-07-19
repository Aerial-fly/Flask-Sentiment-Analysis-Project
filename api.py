# api.py
from flask import Flask, request, jsonify, render_template 
from local_model import get_model

app = Flask(__name__)

print("Memuat model")
model = get_model()
print("Model sudah dimuat")

@app.route("/")
def halaman_utama():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    if not data or 'teks' not in data:
        return jsonify({"error": "Input tidak valid."}), 400

    teks_input = data['teks']
    prediksi = model.predict([teks_input])
    hasil_prediksi = prediksi[0]
    
    return jsonify({
        "input_teks": teks_input,
        "sentimen": hasil_prediksi
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)