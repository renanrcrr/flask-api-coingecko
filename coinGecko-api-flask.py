from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_crypto_quotes(crypto_names, vs_currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_names)}&vs_currencies={vs_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quotes = []
        for crypto_name in crypto_names:
            if crypto_name in data:
                price = data[crypto_name][vs_currency]
                quotes.append({"crypto_name": crypto_name, "price": price})
        return quotes
    else:
        return None

@app.route('/get_crypto_quotes', methods=['GET'])
def get_multiple_crypto_quotes():
    try:
        crypto_names = request.args.getlist('crypto_name')
        vs_currency = request.args.get('vs_currency', 'usd')

        if not crypto_names:
            return jsonify({"error": "At least one crypto name parameter is required."}), 400

        quotes = get_crypto_quotes(crypto_names, vs_currency)

        if quotes is not None:
            return jsonify(quotes)
        else:
            return jsonify({"error": "Failed to fetch data from CoinGecko."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
