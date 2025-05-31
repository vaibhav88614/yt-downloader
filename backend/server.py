from flask import Flask, request, send_file, jsonify
import os
import uuid
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')
    quality = data.get('quality', 'best')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        video_id = str(uuid.uuid4())
        output_path = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.%(ext)s")

        quality_map = {
            "360p": "bestvideo[height<=360]+bestaudio/best[height<=360]",
            "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "best": "bestvideo+bestaudio/best",
            "worst": "worstvideo+worstaudio/worst"
        }

        format_string = quality_map.get(quality, "bestvideo+bestaudio/best")

        ydl_opts = {
            'outtmpl': output_path,
            'format': format_string,
            'merge_output_format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
