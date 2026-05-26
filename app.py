from flask import Flask, request, jsonify, send_from_directory
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv
import io
import base64
import os

load_dotenv()

app = Flask(__name__, static_folder='.')

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_food(pil_image):
    """Send image to Gemini and get nutritional info — your original logic"""
    buffer = io.BytesIO()
    pil_image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()

    prompt = """You are an expert nutritionist and food recognition AI with advanced visual analysis capabilities.

STEP 1 - VISUAL ANALYSIS:
Carefully observe the following visual properties:
- Colors present (be specific: golden-brown, bright red, pale white, etc.)
- Texture (crispy, soft, creamy, raw, cooked, grilled, fried, etc.)
- Ripeness/cooking state (for fruits: ripe/unripe based on color; for cooked food: raw/cooked/overdone)
- Visible ingredients or components
- Approximate quantity and portion size

STEP 2 - FOOD IDENTIFICATION:
Based on your visual analysis:
- Name the exact food/dish (be specific: "Ripe Yellow Mango" not just "Mango", "Grilled Chicken Breast" not just "Chicken")
- If it's a mixed dish, list all visible components
- Mention cuisine type if identifiable (Indian, Italian, Chinese, etc.)
- State your confidence level: High / Medium / Low

STEP 3 - PORTION ESTIMATION:
- Estimate weight in grams
- Describe portion size (small/medium/large or in cups/pieces)

STEP 4 - NUTRITIONAL BREAKDOWN (per serving):
Provide estimated values for:
  - Calories (kcal)
  - Protein (g)
  - Carbohydrates (g)
  - Fat (g)
  - Fiber (g)
  - Sugar (g)
  - Sodium (mg)
  - Vitamins (mention top 2-3 if identifiable)

STEP 5 - HEALTH INSIGHT:
- One line on whether this food is healthy, moderate, or indulgent
- Any key health benefit or warning (e.g. high sugar, good protein source, etc.)

IMPORTANT RULES:
- Base ALL answers strictly on what you visually observe — color, texture, appearance
- Never assume or default to generic answers
- If multiple food items are visible, analyze each separately and give a combined total
- If you cannot identify something clearly, say "Uncertain - possibly X" with Low confidence"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            prompt
        ]
    )
    return response.text


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    try:
        # Decode base64 image from browser
        image_data = data['image'].split(',')[1] if ',' in data['image'] else data['image']
        image_bytes = base64.b64decode(image_data)

        # Convert to PIL Image
        pil_image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        # Save captured image (same as your original code)
        pil_image.save('captured_food.jpg')
        print("💾 Image saved as 'captured_food.jpg'")

        # Run your original analysis
        print("🤖 Analyzing nutritional content...")
        result = analyze_food(pil_image)
        print("\n" + "=" * 40)
        print("📊 NUTRITIONAL ANALYSIS RESULTS")
        print("=" * 40)
        print(result)
        print("=" * 40)

        return jsonify({'result': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("🍽️  Food Nutrient Analyzer")
    print("=" * 40)
    print("🌐 Open http://localhost:5000 in your browser")
    print("=" * 40)
    app.run(debug=True, port=5000)
