from flask import Flask, jsonify, render_template

from app.services.blob_client import LocalContentClient
from app.services.cache import MemoryTTLCache
from app.services.content_service import ContentService

def create_app() -> Flask:
    app = Flask(__name__)
    content_client = LocalContentClient(base_dir="data")
    cache = MemoryTTLCache(ttl_seconds=60, maxsize=128)
    content_service = ContentService(content_client, cache)

    @app.route("/healthz")
    def healthz():
        return jsonify({"status": "ok test"}), 200

    @app.route("/readyz")
    def readyz():
        return jsonify({"status": "ready"}), 200

    @app.route("/")
    def index():
        events = content_service.get_items("events.json")["items"]
        news = content_service.get_items("news.yaml")["items"]
        faq = content_service.get_items("faq.json")["items"]
        return render_template("index.html")

    @app.route("/api/events")
    def api_events():
        return jsonify(content_service.get_items("events.json")), 200

    @app.route("/api/news")
    def api_news():
        return jsonify(content_service.get_items("news.yaml")), 200

    @app.route("/api/faq")
    def api_faq():
        return jsonify(content_service.get_items("faq.json")), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
