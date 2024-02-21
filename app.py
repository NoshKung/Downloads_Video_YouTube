from flask import Flask, render_template, request, redirect, url_for, flash
from pytube import YouTube
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

download_path = './Downloads'
if not os.path.exists(download_path):
    os.makedirs(download_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    quality = request.form['quality']

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4", resolution=quality).first()
        
        stream.download(download_path)
        flash('ดาวน์โหลดเสร็จสมบูรณ์!')
    except Exception as e:
        flash(f'เกิดข้อผิดพลาด: {str(e)}')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
