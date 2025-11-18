"""
Custom Faker provider for Schema.org/Recipe properties.
Generates realistic data for recipes and cooking instructions.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgRecipeProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Recipe properties."""
    
    # Recipe-specific data
    RECIPE_CATEGORIES = [
        "Appetizer", "Main Course", "Dessert", "Side Dish", "Breakfast",
        "Lunch", "Dinner", "Snack", "Beverage", "Salad", "Soup",
        "Bread", "Pasta", "Seafood", "Vegetarian", "Vegan"
    ]
    
    CUISINES = [
        "Italian", "French", "Chinese", "Japanese", "Mexican", "Indian",
        "Thai", "American", "Mediterranean", "Greek", "Spanish", "German"
    ]
    
    INGREDIENTS = [
        "Flour", "Sugar", "Salt", "Pepper", "Olive Oil", "Butter",
        "Eggs", "Milk", "Cheese", "Chicken", "Beef", "Fish",
        "Tomatoes", "Onions", "Garlic", "Basil", "Oregano", "Parsley"
    ]
    
    def recipe_name(self):
        """Recipe name."""
        adjectives = ["Delicious", "Classic", "Easy", "Quick", "Traditional", "Gourmet"]
        dishes = ["Pasta", "Soup", "Salad", "Cake", "Bread", "Stew", "Roast", "Pie"]
        return f"{random.choice(adjectives)} {random.choice(dishes)}"
    
    def recipe_description(self):
        """Recipe description."""
        return self.common_description()
    
    def recipe_recipe_category(self):
        """Recipe category."""
        return random.choice(self.RECIPE_CATEGORIES)
    
    def recipe_recipe_cuisine(self):
        """Cuisine type."""
        return random.choice(self.CUISINES)
    
    def recipe_recipe_ingredient(self):
        """Recipe ingredient."""
        return random.choice(self.INGREDIENTS)
    
    def recipe_recipe_instructions(self):
        """Recipe instructions."""
        steps = [
            "Preheat oven to 350°F",
            "Mix dry ingredients in a large bowl",
            "Add wet ingredients and stir until combined",
            "Pour into prepared pan",
            "Bake for 30-40 minutes until golden brown",
            "Let cool before serving"
        ]
        num_steps = random.randint(4, 8)
        return random.sample(steps, min(num_steps, len(steps)))
    
    def recipe_prep_time(self):
        """Preparation time."""
        times = ["PT15M", "PT30M", "PT45M", "PT1H", "PT1H30M"]
        return random.choice(times)
    
    def recipe_cook_time(self):
        """Cooking time."""
        times = ["PT15M", "PT30M", "PT45M", "PT1H", "PT1H30M", "PT2H"]
        return random.choice(times)
    
    def recipe_total_time(self, prep_time=None, cook_time=None):
        """Total time required."""
        if prep_time and cook_time:
            # Simplified - just return a combined time
            times = ["PT30M", "PT45M", "PT1H", "PT1H30M", "PT2H", "PT2H30M"]
            return random.choice(times)
        return random.choice(["PT30M", "PT45M", "PT1H", "PT1H30M", "PT2H"])
    
    def recipe_recipe_yield(self):
        """Number of servings."""
        return random.randint(2, 12)
    
    def recipe_nutrition_calories(self):
        """Calories per serving."""
        return random.randint(100, 800)
    
    def recipe_author(self):
        """Recipe author."""
        return self.fake.name()
    
    def recipe_image_url(self):
        """Recipe image URL."""
        recipe_name = self.recipe_name().lower().replace(" ", "-")
        return f"https://example.com/images/recipes/{recipe_name}.jpg"
    
    def recipe_aggregate_rating(self):
        """Recipe aggregate rating."""
        return round(random.uniform(3.5, 5.0), 1)
    
    def recipe_review_count(self):
        """Number of recipe reviews."""
        return random.randint(5, 200)
    
    def recipe_keywords(self):
        """Recipe keywords."""
        keywords = ["easy", "quick", "healthy", "delicious", "family-friendly"]
        num_keywords = random.randint(2, 4)
        return ", ".join(random.sample(keywords, num_keywords))


def create_recipe_data(num_entities=10, seed=None):
    """
    Generate recipe data using the custom provider.
    
    Args:
        num_entities: Number of recipe entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing recipe data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgRecipeProvider)
    
    recipes = []
    
    for i in range(num_entities):
        prep_time = fake.recipe_prep_time()
        cook_time = fake.recipe_cook_time()
        total_time = fake.recipe_total_time(prep_time, cook_time)
        
        recipe = {
            "@type": "Recipe",
            "name": fake.recipe_name(),
            "description": fake.recipe_description(),
            "recipeCategory": fake.recipe_recipe_category(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            recipe["recipeCuisine"] = fake.recipe_recipe_cuisine()
        
        # Ingredients
        num_ingredients = random.randint(5, 15)
        recipe["recipeIngredient"] = [fake.recipe_recipe_ingredient() for _ in range(num_ingredients)]
        
        # Instructions
        recipe["recipeInstructions"] = fake.recipe_recipe_instructions()
        
        # Time
        recipe["prepTime"] = prep_time
        recipe["cookTime"] = cook_time
        recipe["totalTime"] = total_time
        
        # Yield
        recipe["recipeYield"] = fake.recipe_recipe_yield()
        
        # Nutrition
        if random.random() < 0.6:
            recipe["nutrition"] = {
                "calories": fake.recipe_nutrition_calories()
            }
        
        # Author
        if random.random() < 0.7:
            recipe["author"] = fake.recipe_author()
        
        # Image
        if random.random() < 0.8:
            recipe["image"] = fake.recipe_image_url()
        
        # Ratings
        if random.random() < 0.6:
            rating = fake.recipe_aggregate_rating()
            review_count = fake.recipe_review_count()
            recipe["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        # Keywords
        if random.random() < 0.5:
            recipe["keywords"] = fake.recipe_keywords()
        
        recipes.append(recipe)
    
    return recipes


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Recipe Provider\n")
    print("=" * 80)
    
    recipes = create_recipe_data(num_entities=3, seed=42)
    
    for i, recipe in enumerate(recipes, 1):
        print(f"\nRecipe {i}:")
        print("-" * 80)
        for key, value in recipe.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    print(f"    - {item}")
            else:
                print(f"  {key}: {value}")

