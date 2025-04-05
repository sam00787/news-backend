from flask import Flask, request, jsonify
import feedparser

app = Flask(__name__)

# Example RSS Feeds (Add more as needed)
RSS_FEEDS = {
    'world': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'technology': 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
    'sports': 'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml',
    'health': 'https://rss.nytimes.com/services/xml/rss/nyt/Health.xml',
}


@app.route('/news/')
def get_news():
    category = request.args.get('category', 'world')
    search = request.args.get('search', '')

    feed_url = RSS_FEEDS.get(category, RSS_FEEDS['world'])
    feed = feedparser.parse(feed_url)

    results = []
    for entry in feed.entries:
        if search.lower() in entry.title.lower() or search.lower() in entry.summary.lower():
            summary = summarize(entry.summary)
            results.append({
                'title': entry.title,
                'summary': summary
            })

    return jsonify(results)


def summarize(text):
    sentences = text.split('. ')
    summary = '. '.join(sentences[:5]) + '...'
    return summary


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

