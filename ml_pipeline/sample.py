import pandas as pd
'''
class_names = ['apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 'beet_salad',
                'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito', 'bruschetta', 'caesar_salad',
                'cannoli', 'caprese_salad', 'carrot_cake', 'ceviche', 'cheesecake', 'cheese_plate', 'chicken_curry',
                'chicken_quesadilla', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder',
                'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 'deviled_eggs', 'donuts',
                'dumplings', 'edamame', 'eggs_benedict', 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips',
                'foie_gras', 'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice',
                'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon',
                'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 'hot_dog', 'huevos_rancheros', 'hummus',
                'ice_cream', 'lasagna', 'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons',
                'miso_soup', 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 'paella',
                'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib',
                'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi',
                'scallops', 'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 'spaghetti_carbonara',
                'spring_rolls', 'steak', 'strawberry_shortcake', 'sushi', 'tacos', 'takoyaki', 'tiramisu',
                'tuna_tartare', 'waffles']  # Replace with actual class names

nutritional_data = {
    'Label': class_names,
    'Calories': [300, 500, 400, 250, 200, 150, 350, 300, 450, 600, 200, 250, 300, 150, 400, 200, 500, 350, 400, 500, 600, 
                 300, 500, 350, 400, 550, 600, 250, 300, 400, 350, 300, 450, 400, 300, 350, 250, 500, 300, 350, 400, 300, 
                 250, 300, 250, 300, 400, 500, 250, 350, 400, 300, 200, 150, 300, 200, 300, 500, 400, 250, 350, 200, 300, 
                 400, 350, 500, 600, 300, 350, 450, 200, 300, 250, 300, 200, 400, 500, 350, 400, 200, 500, 600, 250, 300, 
                 500, 450, 350, 500, 450, 300, 350, 300, 350, 200, 250, 400, 300,200, 250, 400, 300,],
    'Nutrients': ['Vitamin A, C', 'Protein, Iron', 'Sugar, Carbs', 'Protein, Vitamin B12', 'Protein', 'Fiber, Vitamin K', 
                  'Sugar', 'Protein, Carbs', 'Sugar, Carbs', 'Protein, Carbs', 'Vitamins, Carbs', 'Vitamin A, C', 'Sugar, Calcium', 
                  'Vitamin A, C', 'Carbs, Fiber', 'Protein, Vitamin C', 'Calcium', 'Calcium, Protein', 'Protein', 'Protein', 
                  'Sugar', 'Sugar', 'Carbs, Sugar', 'Protein', 'Fat, Protein', 'Sugar, Carbs', 'Fat, Protein', 'Protein', 'Fiber', 
                  'Vitamin A', 'Carbs', 'Fiber', 'Vitamin A, C', 'Protein', 'Carbs, Fiber', 'Vitamin C', 'Calcium', 'Vitamin C', 
                  'Protein', 'Vitamin B', 'Carbs', 'Vitamin C', 'Vitamin A', 'Protein', 'Protein', 'Vitamin B', 'Carbs', 'Vitamin A, C', 
                  'Fiber', 'Calcium', 'Protein', 'Vitamin A', 'Vitamin C', 'Protein', 'Fiber', 'Carbs', 'Vitamin B', 'Vitamin C', 
                  'Carbs', 'Vitamin B', 'Protein', 'Vitamin B', 'Vitamin C', 'Protein', 'Carbs', 'Fiber', 'Protein', 'Vitamins', 
                  'Carbs', 'Protein', 'Fiber', 'Protein, Carbs', 'Vitamin C', 'Protein, Carbs', 'Fiber', 'Protein', 'Vitamin B12', 
                  'Fiber', 'Vitamin A, C', 'Vitamin A', 'Protein', 'Protein, Carbs', 'Vitamin B', 'Vitamin C', 'Fat, Protein', 
                  'Carbs, Protein', 'Calcium, Vitamin C', 'Fiber, Carbs', 'Vitamin A', 'Fiber', 'Protein', 'Vitamin B, Fiber', 
                  'Sugar, Calcium', 'Protein', 'Fiber', 'Carbs, Sugar', 'Protein', 'Vitamins', 'Protein, Calcium','Protein, Calcium','Calcium'],
    'Carbohydrates (g)': [45, 20, 55, 10, 5, 20, 40, 50, 60, 70, 30, 40, 45, 25, 55, 10, 65, 55, 50, 60, 80, 40, 70, 45, 50, 
                          60, 70, 25, 30, 45, 35, 50, 60, 55, 40, 50, 20, 70, 35, 50, 55, 35, 20, 30, 20, 45, 50, 60, 30, 40, 
                          50, 40, 25, 15, 35, 20, 35, 60, 45, 30, 50, 20, 35, 45, 55, 60, 30, 35, 55, 20, 40, 30, 35, 30, 60, 
                          55, 40, 60, 40, 65, 30, 35, 40, 50, 55, 50, 45, 35, 60, 50, 30, 50, 60, 35, 40, 30, 40,35, 40, 30, 40,],
    'Fats (g)': [15, 30, 25, 10, 15, 10, 20, 25, 30, 35, 10, 15, 20, 15, 25, 10, 30, 20, 25, 30, 35, 15, 30, 20, 25, 30, 
                 35, 15, 20, 25, 20, 25, 30, 20, 15, 20, 10, 35, 20, 25, 30, 20, 15, 25, 20, 15, 30, 35, 20, 25, 30, 20, 15, 
                 10, 20, 15, 25, 35, 20, 15, 25, 10, 20, 25, 30, 20, 25, 35, 15, 20, 25, 10, 20, 30, 25, 35, 25, 20, 30, 20, 
                 35, 25, 30, 25, 15, 20, 20, 35, 25, 20, 15, 25, 20, 15, 30, 25, 15, 25, 20,25, 20]
}

nutritional_df = pd.DataFrame(nutritional_data)
print(nutritional_df)
'''
a= ['apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 'beet_salad',
                'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito', 'bruschetta', 'caesar_salad',
                'cannoli', 'caprese_salad', 'carrot_cake', 'ceviche', 'cheesecake', 'cheese_plate', 'chicken_curry',
                'chicken_quesadilla', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder',
                'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 'deviled_eggs', 'donuts',
                'dumplings', 'edamame', 'eggs_benedict', 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips',
                'foie_gras', 'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice',
                'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon',
                'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 'hot_dog', 'huevos_rancheros', 'hummus',
                'ice_cream', 'lasagna', 'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons',
                'miso_soup', 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 'paella',
                'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib',
                'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi',
                'scallops', 'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 'spaghetti_carbonara',
                'spring_rolls', 'steak', 'strawberry_shortcake', 'sushi', 'tacos', 'takoyaki', 'tiramisu',
                'tuna_tartare', 'waffles']  
print(len(a))