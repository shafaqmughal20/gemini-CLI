from flask import Flask, render_template
import feedparser

app = Flask(__name__)

def get_cricket_scores():
    """Fetches and parses cricket scores from the RSS feed."""
    feed_url = "https://static.cricinfo.com/rss/livescores.xml"
    feed = feedparser.parse(feed_url)
    return feed.entries

@app.route("/")
def index():
    """Renders the index page with live cricket scores."""
    scores = get_cricket_scores()
    return render_template("index.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
