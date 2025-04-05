from flask import Flask, jsonify, request
from flask_cors import CORS  # <-- Add this import

app = Flask(__name__)

# Allow CORS for all origins (you can specify domains here)
CORS(app)

@app.route("/news/")
def get_news():
    category = request.args.get('category')
    search = request.args.get('search')

    # Example data, replace with actual fetching logic
    news_data = [
        {"title": f"{search} News 1", "summary": "Summary of news 1"},
        {"title": f"{search} News 2", "summary": "Summary of news 2"},
    ]
    
    return jsonify(news_data)

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

