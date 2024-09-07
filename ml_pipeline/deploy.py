import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import pandas as pd
from PIL import Image

# Load your pre-trained model
model = tf.keras.models.load_model('../model/food_vision_v2.keras')  # Replace with your model path

# Define class names (replace with your actual class names)
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

def preprocess_image(img):
    """Preprocess the image for the model."""
    img = img.resize((224, 224))  # Adjust the target size based on your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)  # Adjust for your model
    return img_array

def predict_image(img_array):
    """Predict the class of the image using the model."""
    predictions = model.predict(img_array)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    return predicted_class_idx, class_names[predicted_class_idx], predictions[0]

# Streamlit app
st.title('Food Vision Application')
st.write("Upload an image of food to get a prediction!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    # Preprocess and predict
    img_array = preprocess_image(img)
    predicted_class_idx, predicted_class_name, predictions = predict_image(img_array)
    
    # Display the prediction
    st.write(f"**Predicted class index:** {predicted_class_idx}")
    st.write(f"**Predicted class name:** {predicted_class_name}")

    # Convert predictions to DataFrame for bar chart
    df_probabilities = pd.DataFrame(predictions, index=class_names, columns=['Probability'])
    df_probabilities = df_probabilities.sort_values(by='Probability', ascending=False)

    # Display bar chart
    st.write("### Prediction Probabilities")
    st.bar_chart(df_probabilities, width=600, height=300, use_container_width=True)

    # Display a message based on the prediction
    st.success(f"The model predicts this image as: {predicted_class_name}")
