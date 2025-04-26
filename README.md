# 🖼️ Image Hosting API

A lightweight, fast, and scalable image hosting API built with **FastAPI**, deployed on **Render**.

This API allows you to upload images and provides a publicly accessible URL for each uploaded image.

---

## 🚀 Live Demo

- **Base URL**: [https://futuregen.onrender.com](https://futuregen.onrender.com)
- **Upload Endpoint**: [https://futuregen.onrender.com/upload](https://futuregen.onrender.com/upload)

---

## 📦 Features

- Upload images (`.jpg`, `.jpeg`, `.png`) via POST requests
- Returns publicly accessible image URL
- Built with FastAPI
- Hosted on Render with HTTPS
- Dynamic configuration via `config.json`
- Monitored using UptimeRobot to prevent cold starts
- Professional folder structure and logging

---

## 🛠️ Project Structure

```
image_hosting_api/
├── app/
│   ├── main.py          # FastAPI app with upload and root routes
│   ├── config.py        # Configuration loader
│   ├── logger.py        # Logging setup
│   ├── utils.py         # Helper utilities
├── uploads/             # Uploaded images stored here
│   └── .gitkeep
├── test/
│   └── upload_image.py  # Testing script for uploads
├── config.json          # Configuration settings
├── requirements.txt     # Project dependencies
└── runtime.txt          # Python runtime version for Render
```

---

## 📋 API Endpoints

### `POST /upload`
Upload an image file and receive a public URL.

- **Form field**: `file`
- **Supported formats**: `.jpg`, `.jpeg`, `.png`
- **Response**:
  ```json
  {
    "url": "https://futuregen.onrender.com/images/<uploaded_filename>"
  }
  ```

---

## 🧪 Local Testing

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image_hosting_api.git
   cd image_hosting_api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

4. Upload an image:
   ```bash
   python test/upload_image.py path/to/your/image.jpg
   ```

---

## ⚙️ Configuration

Modify `config.json` to adjust settings:

```json
{
  "server": {
    "host": "0.0.0.0",
    "port": 8000
  },
  "upload_dir": "uploads",
  "logging": {
    "level": "INFO",
    "file": "app.log"
  },
  "base_url": "https://futuregen.onrender.com"
}
```

---

## 🛡️ Notes

- Free Render plans may experience cold starts; UptimeRobot pings prevent downtime.
- Uploaded images remain publicly accessible unless manually deleted.
- Future improvements could include authentication, image expiration, or quota limits.

---

## ✨ Credits

Built and deployed by **Mayur** 🚀  
Guided and supported by Sam (ChatGPT AI).

---

## 📜 License

This project is licensed under the MIT License.