import logging
from pathlib import Path
from funcy import log_durations
from flask import render_template, Flask, send_from_directory

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        Path(__file__).parent.joinpath("templates"), "favicon.png", mimetype="image/png"
    )


@app.route("/", methods=["GET"])
@log_durations(app.logger.debug)
def index():
    return render_template("index.html", page_name="", project_name="goldendoodle")


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info("Starting goldendoodle server.")
else:
    app.run(debug=True)
