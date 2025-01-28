import google.generativeai as genai
import requests
import PIL.Image
import io

# API keys
GOOGLE_API_KEY = 'your-google-api-key' # Replace with your own google API.
USDA_API_KEY =  'your-usda-api-key' # Replace with your own USDA API.
USDA_SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Function to analyse meal image using Gemini
def analyse_food_image(image_path):
    """Uses Gemini 1.5 flash to analyse a meal image and return identified food items."""
    model = genai.GenerativeModel("gemini-1.5-flash")

    img_part = PIL.Image.open(image_path)
    
    text_prompt = "Identify all food items in this image."

    response = model.generate_content([img_part, text_prompt])

    return response.text # Returns detected food items

# Function to fetch nutrition data from USDA API
def get_nutrition_info(food_name):
    """Fetches calories, protein, carbs, and fat for a given food item from USDA API."""
    params = {"query": food_name, "api_key": USDA_API_KEY}

    response = requests.get(USDA_SEARCH_URL, params=params)
    data = response.json()

    if "foods" in data and len(data["foods"]) > 0:
        food_data = data["foods"][0]  # Take the first search result
        food_nutrients = {nutrient["nutrientName"]: nutrient["value"] for nutrient in food_data["foodNutrients"]}

        return {
            "food": food_name,
            "calories": food_nutrients.get("Energy", 0),  # kcal
            "protein": food_nutrients.get("Protein", 0),  # g
            "carbs": food_nutrients.get("Carbohydrate, by difference", 0),  # g
            "fat": food_nutrients.get("Total lipid (fat)", 0)  # g
        }

    return None

# Upload image, get food items & calculate nutrition
def analyse_meal(image_path):
    """ Processes an image to analyse food items and return nutrition facts using USDA API. """
    food_items = analyse_food_image(image_path).split(", ")  # Split detected items

    meal_nutrition = []
    total_calories, total_protein, total_carbs, total_fat = 0, 0, 0, 0

    for food in food_items:
        nutrition = get_nutrition_info(food)
        if nutrition:
            meal_nutrition.append(nutrition)
            total_calories += nutrition["calories"]
            total_protein += nutrition["protein"]
            total_carbs += nutrition["carbs"]
            total_fat += nutrition["fat"]

    # Output Nutrition Summary
    print("\n🔹 **Meal Nutrition Summary** 🔹")
    for item in meal_nutrition:
        print(f"{item['food']}: {item['calories']} kcal | {item['protein']}g Protein | {item['carbs']}g Carbs | {item['fat']}g Fat")

    print(f"\n✅ **Total Meal Calories:** {total_calories} kcal")
    print(f"✅ **Total Protein:** {total_protein}g")
    print(f"✅ **Total Carbs:** {total_carbs}g")
    print(f"✅ **Total Fat:** {total_fat}g")

# Test it with an image
image_path = "test1.jpeg"  # Replace with your meal image file path
analyse_meal(image_path)