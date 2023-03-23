from flask import Flask, render_template, request, session, url_for, redirect, send_file
from pytube import YouTube
from io import BytesIO

    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fac55e7c9d00f473c7ac20bc'

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            y = YouTube(session['link'])
            y.check_availability()
            return render_template('download.html', yt=y)
        except:
            return render_template('error.html')
    return render_template('home.html')

@app.route('/download', methods=['GET','POST'])
def download():
    if request.method == "POST":
        buffer = BytesIO()
        y = YouTube(session['link'])
        itag = request.form.get('itag')
        video = y.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=y.title, mimetype='video/mp4')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
