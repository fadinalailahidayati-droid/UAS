from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MENU = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 25000},
    {"id": 2, "nama": "Mie Goreng", "harga": 22000},
    {"id": 3, "nama": "Ayam Bakar", "harga": 35000},
    {"id": 4, "nama": "Es Teh", "harga": 5000},
    {"id": 5, "nama": "Jus Jeruk", "harga": 12000}
]

@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(MENU)

@app.route('/api/total', methods=['POST'])
def hitung_total():
    pesanan = request.json.get('pesanan', [])
    total = 0
    for item in pesanan:
        menu_item = next((m for m in MENU if m["id"] == item["id"]), None)
        if menu_item:
            total += menu_item["harga"] * item["jumlah"]
    return jsonify({"total": total})

if __name__ == "__main__":
    print("🚀 SERVER RESTAURAN SIAP! http://localhost:5000")
    app.run(debug=True, port=5000)
