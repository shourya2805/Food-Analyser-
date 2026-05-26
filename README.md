# Food-Analyser-
# 🍽️ Food Nutrient Analyzer

An AI-powered web application that analyzes the nutritional content of food in real time using your camera and Google's Gemini AI. Simply capture a photo of your food and get an instant, detailed nutritional breakdown — including calories, macros, vitamins, and a health insight.

---

## 🚀 Demo

1. Open the app in your browser
2. Click **Start Camera**
3. Point at your food and click **Capture & Analyze**
4. Get a full nutritional breakdown instantly

---

## 🧠 How It Works

```
Browser Webcam
      ↓
Captures image (JPEG)
      ↓
Sends to Flask backend (/analyze)
      ↓
Flask decodes base64 image → PIL Image
      ↓
Sends image + prompt to Gemini AI API
      ↓
Gemini analyzes food visually
      ↓
Returns nutritional analysis
      ↓
Flask sends result back to browser
      ↓
UI displays structured results card
```

---

## 📁 Project Structure

```
FoodAnalyser/
├── app.py           # Flask backend — handles routing, image processing, Gemini API calls
├── index.html       # Frontend UI — camera capture, results display
├── .env             # Environment variables (API key) — never commit this
├── .gitignore       # Ignores .env, venv, __pycache__, etc.
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## ⚙️ Tech Stack

### Backend
| Library | Version | Purpose |
|---|---|---|
| `flask` | latest | Web framework — serves the UI and handles API routes |
| `google-genai` | latest | Google Gemini AI client — sends image and prompt, receives analysis |
| `Pillow` | latest | Image processing — converts bytes to PIL Image, handles color formats |
| `python-dotenv` | latest | Loads API key securely from `.env` file |
| `opencv-python` | latest | Camera access and image capture (used in original CLI version) |

### Frontend
| Technology | Purpose |
|---|---|
| HTML5 | Structure and layout |
| CSS3 | Styling and responsive design |
| JavaScript (Vanilla) | Camera access via `getUserMedia`, fetch API calls, DOM updates |
| Tabler Icons | UI icons |

### AI
| Service | Model | Purpose |
|---|---|---|
| Google Gemini API | `gemini-2.5-flash` | Food recognition and nutritional analysis from image |

---

## 🔍 What Gemini Analyzes

The AI performs a 5-step analysis on every captured food image:

1. **Visual Analysis** — colors, texture, cooking state, visible ingredients
2. **Food Identification** — exact dish name, cuisine type, confidence level
3. **Portion Estimation** — weight in grams, portion size description
4. **Nutritional Breakdown** — calories, protein, carbs, fat, fiber, sugar, sodium, vitamins
5. **Health Insight** — healthy / moderate / indulgent rating with key benefit or warning

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Food-Analyser.git
cd Food-Analyser
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
Get your free API key at [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 5. Run the app
```bash
python3 app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 📦 requirements.txt

```
flask
google-genai
Pillow
python-dotenv
opencv-python
```

Generate it automatically with:
```bash
pip freeze > requirements.txt
```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key from AI Studio |

Never hardcode your API key in the source code. Always use `.env`.

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the frontend UI (`index.html`) |
| `POST` | `/analyze` | Accepts base64 image, returns nutritional analysis JSON |

### `/analyze` Request Body
```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQ..."
}
```

### `/analyze` Response
```json
{
  "result": "STEP 1 - VISUAL ANALYSIS:\n..."
}
```

---

## 🗂️ .gitignore

```
.env
venv/
__pycache__/
*.pyc
captured_food.jpg
.DS_Store
```

---

## ⚠️ Known Limitations

- Requires a valid Gemini API key with available quota
- Free tier has daily request limits — upgrade at [https://ai.google.dev](https://ai.google.dev) for higher limits
- Camera access requires browser permissions
- Best results with good lighting and a clear shot of the food
- Nutritional values are **AI estimates** — not a substitute for professional dietary advice

---

## 🙌 Acknowledgements

- [Google Gemini API](https://ai.google.dev) — AI-powered food analysis
- [Flask](https://flask.palletsprojects.com) — lightweight Python web framework
- [OpenCV](https://opencv.org) — computer vision library
- [Pillow](https://python-pillow.org) — Python image processing
- [Tabler Icons](https://tabler-icons.io) — open source UI icons

---

