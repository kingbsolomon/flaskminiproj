from flask import Flask, render_template, jsonify
import data

app = Flask(__name__)


@app.route("/")
def render_music_table():
    return render_template('table.html', data=data.music)


@app.route("/json")
def render_music_table_json():
    return jsonify(data.music)


@app.route("/songform")
def add_song_form():
    return render_template('song.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)


