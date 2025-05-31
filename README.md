# 🌍 Universal Video Downloader  
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Chrome Extension](https://img.shields.io/badge/Extension-Popup%20UI-blue)](https://chrome.google.com/webstore)  
[![Built with Python](https://img.shields.io/badge/Built%20with-Flask%20%2B%20yt--dlp-yellow)](https://github.com/yt-dlp/yt-dlp)

---

## 📸 Demo

> 📌 Paste video URL → Choose quality → Click download

![Popup Screenshot](./screenshots/popup-demo.png)
<!-- Add your screenshot in a `screenshots` folder -->

---

## 🚀 Features

✅ Download videos from:
- **YouTube**, **Instagram Reels**, **Twitter**, **Facebook**, **Vimeo**, and more  
✅ Choose quality: `1080p`, `720p`, `360p`, `best`, or `worst`  
✅ Fully client-side popup UI — no site injection  
✅ Python Flask backend using `yt-dlp`  
✅ Free deployment on [Render](https://render.com)  
✅ Designed for speed, simplicity, and cross-platform support

---

## 🧱 Project Structure

```bash
universal-video-downloader/
│
├── backend/                 # Python Flask API with yt-dlp
│   ├── server.py
│   ├── requirements.txt
│   └── render.yaml
│
└── chrome-extension/       # Chrome extension popup interface
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    └── icon.png
```

---

## 🌐 Deploy Backend (1-click Setup)

1. Upload `/backend` to a **GitHub repo**
2. Create a new Web Service at [Render.com](https://render.com)
3. Connect your GitHub repo
4. Set:
   - 🛠 **Build Command**: *(leave blank)*  
   - ▶️ **Start Command**: `python server.py`
5. Copy the live backend URL (e.g., `https://video-downloader-api.onrender.com`)

---

## 🧩 Load Chrome Extension

1. Open Chrome → Go to `chrome://extensions`
2. Enable **Developer Mode**
3. Click **Load Unpacked** → Select the `/chrome-extension` folder
4. Replace the backend URL in `popup.js` with your Render URL

---

## 🛠 Built With

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Chrome Extensions API (MV3)](https://developer.chrome.com/docs/extensions/mv3/)
- [Render Cloud Hosting](https://render.com)

---

## ⚠️ Disclaimer

> This project is intended for **educational & personal use**.  
> Downloading copyrighted content may violate the terms of service of hosting platforms.

---

## 📬 Contact & Contribute

Pull requests and stars are always welcome.  
For improvements, bug reports, or feature requests — feel free to open an issue.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔖 Project Description (for GitHub About Section)

**Universal Video Downloader** is a Chrome extension with a Flask + `yt-dlp` backend that lets you download videos from YouTube, Instagram Reels, Twitter, Facebook, Vimeo, and more — with selectable quality and a clean popup UI. Built for personal use, fast performance, and privacy-first downloading. Deployed easily with Render.
