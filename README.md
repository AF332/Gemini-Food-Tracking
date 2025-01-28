# Gemini LLM Food Image Analysis

## Project Overview
This project utilizes **Google's Gemini LLM** along with the **USDA Food Data API** to analyze food images and extract nutritional information. By uploading an image of a meal, the script identifies food items using **Gemini 1.5 Flash** and fetches corresponding **calories, protein, carbohydrates, and fat** data from the USDA API.

This project is useful for **food tracking, meal planning, and nutrition analysis**, making it a great tool for fitness enthusiasts, dieticians, and researchers.

---

## Features
- **AI-powered food detection**: Uses **Gemini LLM** to identify food items in an image.
- **Automated nutrition analysis**: Fetches macronutrient breakdown (calories, protein, carbs, fat) using **USDA Food Data API**.
- **Summarized Meal Report**: Displays total caloric and macronutrient content of the detected meal.
- **Scalable & Extendable**: Can be integrated into fitness tracking apps, diet planners, or meal logging systems.

---

## Technologies Used
- **Python**: Core programming language.
- **Google Gemini API**: AI model for analyzing food images.
- **USDA Food Data API**: Source for retrieving nutritional values.
- **Pillow (PIL)**: Image processing for handling uploaded meal images.
- **Requests**: For making API calls.

---

## Installation & Setup
### Prerequisites
Ensure you have Python (>=3.7) installed along with the required libraries:
```sh
pip install google-generativeai requests pillow
```

### API Setup
1. **Google Gemini API**: Obtain an API key from [Google AI](https://ai.google.dev/) and set it up.
2. **USDA API**: Register on [USDA Food Data Central](https://fdc.nal.usda.gov/) and generate an API key.

Replace the placeholder API keys in `Gemini.py` with your own:
```python
GOOGLE_API_KEY = 'your-google-api-key'
USDA_API_KEY = 'your-usda-api-key'
```

### Running the Script
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/food-analysis-gemini.git
   cd food-analysis-gemini
   ```
2. **Run the Script**:
   ```sh
   python Gemini.py
   ```
3. **Upload a Meal Image**: Replace the image path in `Gemini.py` with your own meal image file:
   ```python
   image_path = "your_image.jpeg"
   analyse_meal(image_path)
   ```
4. **View the Nutrition Report**: The script will display a **detailed breakdown** of calories, protein, carbs, and fat.

---

## Example Output
```sh
🔹 **Meal Nutrition Summary** 🔹
Chicken: 165 kcal | 31g Protein | 0g Carbs | 3.6g Fat
Rice: 130 kcal | 2.7g Protein | 28g Carbs | 0.3g Fat
Broccoli: 55 kcal | 3.7g Protein | 11g Carbs | 0.6g Fat

✅ **Total Meal Calories:** 350 kcal
✅ **Total Protein:** 37.4g
✅ **Total Carbs:** 39g
✅ **Total Fat:** 4.5g
```

---

## Challenges Faced
- Handling **image variations** (e.g., different lighting conditions and angles).
- **Matching food names** detected by Gemini to USDA’s food database.
- Optimizing API calls for **faster processing**.

---

## Future Enhancements
- **Improve food recognition accuracy** using fine-tuned models.
- **Add support for multiple food databases**.
- **Build a web interface** for uploading images and visualizing nutrition reports.
- **Develop a mobile app integration** for real-time meal tracking.

---

## Acknowledgements
- **Google AI** for providing Gemini LLM.
- **USDA Food Data Central** for reliable nutrition data.
- **Open-source community** for continuous support and learning.

