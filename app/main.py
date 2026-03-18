from flask import Flask, jsonify, render_template

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/healthz")
    def healthz():
        return jsonify({"status": "ok test"}), 200

    @app.route("/readyz")
    def readyz():
        return jsonify({"status": "ready"}), 200

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api/events")
    def api_events():
        return jsonify({"items": []}), 200

    @app.route("/api/news")
    def api_news():
        return jsonify({"items": []}), 200

    @app.route("/api/faq")
    def api_faq():
        return jsonify({"items": []}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
