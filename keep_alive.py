from flask import Flask, render_template
from threading import Thread

app = Flask('')

from flask import Flask, render_template, request, redirect
import youtube_dl
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("main.html")

@app.route('/download', methods=["POST", "GET"])
def download():
    if request.method == "POST":
        url = request.form["url"]
        if url == '':
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        else:
            pass
        # print("Someone just tried to download", url)
        with youtube_dl.YoutubeDL() as ydl:
            url = ydl.extract_info(url, download=False)
            print(url)
            try:
                download_link = url["entries"][-1]["formats"][-1]["url"]
            except:
                download_link = url["formats"][-1]["url"]
            return redirect(download_link+"&dl=1")

if __name__ == '__main__':
	app.run(debug=True)

def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
