import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import pandas as pd
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import io
import sys

# Visualizing Convolution Operation
def plot_convolution_operation(img, kernel):
    # Perform convolution using the kernel (filter)
    img_gray = np.mean(img, axis=2)  # Convert to grayscale
    kernel_size = kernel.shape[0]
    output = np.zeros_like(img_gray)
    height, width = img_gray.shape

    for i in range(height - kernel_size + 1):
        for j in range(width - kernel_size + 1):
            region = img_gray[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(region * kernel)

    # Plotting the original image and the filtered output
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(output, cmap='gray')
    axes[1].set_title("After Convolution")
    axes[1].axis('off')

    st.pyplot(fig)

# Visualizing Pooling Operation (Max Pooling)
def plot_pooling_operation(img):
    img_gray = np.mean(img, axis=2)  # Convert to grayscale
    pool_size = 2
    stride = 2
    height, width = img_gray.shape

    # Apply max pooling operation
    pooled_img = np.zeros((height // pool_size, width // pool_size))
    for i in range(0, height, pool_size):
        for j in range(0, width, pool_size):
            region = img_gray[i:i+pool_size, j:j+pool_size]
            pooled_img[i // pool_size, j // pool_size] = np.max(region)

    # Plotting the original image and the pooled image
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(pooled_img, cmap='gray')
    axes[1].set_title("After Max Pooling")
    axes[1].axis('off')

    st.pyplot(fig)

def plot_efficientnet_b0_with_labels():
    fig, ax = plt.subplots(figsize=(10, 12))  # Increased figure size to fit everything
    
    # Define the layers and their descriptions
    layers = [
        ("Input", "224x224 Image", (0.5, 0.9)), 
        ("Conv1", "Initial Convolution", (0.5, 0.75)),
        ("Block1", "Depthwise Separable Convs", (0.5, 0.6)),
        ("Block2", "Depthwise Separable Convs", (0.5, 0.45)),
        ("Block3", "Depthwise Separable Convs", (0.5, 0.3)),
        ("Block4", "Final Depthwise Separable Convs", (0.5, 0.15)),
        ("Fully Connected", "Dense Layer for Classification", (0.5, 0.05)),
        ("Output", "Final Classification Output", (0.5, -0.1))  # Adjusted the position for Output
    ]
    
    # Draw each layer box and add labels with descriptions
    for layer, description, position in layers:
        ax.add_patch(patches.Rectangle((0.25, position[1] - 0.05), 0.5, 0.1, linewidth=2, edgecolor='black', facecolor='lightblue'))
        ax.text(0.5, position[1], f"{layer}\n({description})", ha='center', va='center', fontsize=10)
    
    # Draw downward arrows between layers
    for i in range(len(layers) - 1):
        ax.annotate('', xy=(0.5, layers[i + 1][2][1] + 0.05), xytext=(0.5, layers[i][2][1] - 0.05),
                    arrowprops=dict(arrowstyle='->', lw=1.5))
    
    # Add title
    ax.text(0.5, 1.05, 'EfficientNet-B0 Architecture (224x224 Image)', fontsize=16, ha='center', va='center')
    
    # Hide axes
    ax.set_axis_off()
    
    # Render plot in Streamlit
    st.pyplot(fig)

# Load example image for visualizations
def load_image(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))
    img_array = np.array(img)
    return img_array

# Visualizing Convolution Operation
def plot_convolution_operation(img, kernel):
    # Perform convolution using the kernel (filter)
    img_gray = np.mean(img, axis=2)  # Convert to grayscale
    kernel_size = kernel.shape[0]
    output = np.zeros_like(img_gray)
    height, width = img_gray.shape

    for i in range(height - kernel_size + 1):
        for j in range(width - kernel_size + 1):
            region = img_gray[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(region * kernel)

    # Plotting the original image and the filtered output
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(output, cmap='gray')
    axes[1].set_title("After Convolution")
    axes[1].axis('off')

    st.pyplot(fig)

# Visualizing Pooling Operation (Max Pooling)
def plot_pooling_operation(img):
    img_gray = np.mean(img, axis=2)  # Convert to grayscale
    pool_size = 2
    stride = 2
    height, width = img_gray.shape

    # Apply max pooling operation
    pooled_img = np.zeros((height // pool_size, width // pool_size))
    for i in range(0, height, pool_size):
        for j in range(0, width, pool_size):
            region = img_gray[i:i+pool_size, j:j+pool_size]
            pooled_img[i // pool_size, j // pool_size] = np.max(region)

    # Plotting the original image and the pooled image
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(pooled_img, cmap='gray')
    axes[1].set_title("After Max Pooling")
    axes[1].axis('off')

    st.pyplot(fig)

# Visualizing EfficientNet Block
def plot_efficientnet_block():
    # Just an illustration of an EfficientNet block with depthwise separable convolution.
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.text(0.5, 0.8, 'EfficientNet Block', fontsize=20, ha='center')
    ax.text(0.5, 0.6, 'Depthwise Separable Convolution', fontsize=14, ha='center')
    ax.text(0.5, 0.4, 'Standard Convolution + Depthwise Separable Convolution', fontsize=12, ha='center')
    ax.text(0.5, 0.2, 'Bottleneck Layers', fontsize=12, ha='center')
    ax.set_axis_off()
    st.pyplot(fig)

# Load your pre-trained model
path_model=os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),'model'),'Food_vision_v2.keras')
model = tf.keras.models.load_model(path_model)

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
                'tuna_tartare', 'waffles']

# Nutritionix API credentials
API_KEY = 'ca3ad7a9bdd515e90017912bfd055b42'  # Replace with your API key
APP_ID = 'ec342b7f'  # Replace with your app ID

# Preprocessing and helper functions
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)
    return img_array

def predict_image(img_array):
    predictions = model.predict(img_array)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    return predicted_class_idx, class_names[predicted_class_idx], predictions[0]

def fetch_nutrition_info(food_name):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {'x-app-id': APP_ID, 'x-app-key': API_KEY}
    response = requests.post(url, headers=headers, json={"query": food_name})
    data = response.json()
    return data['foods'][0] if 'foods' in data and data['foods'] else None

# Radar Chart Function
def plot_radar_chart(labels, values):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    st.pyplot(fig)

# App Design
st.set_page_config(
    page_title="Food Vision Pro",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
sidebar_option = st.sidebar.radio("Select an Option", ["🎯Prediction", "📊Model Architecture", "🍏About"])

# Page Content Based on Sidebar Selection
if sidebar_option == "🎯Prediction":
    st.title("🍔 Food Vision Pro")
    st.write("Predict food from images and track your nutritional progress!")

    # Image Upload in Sidebar
    uploaded_file = st.sidebar.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        img_array = preprocess_image(img)

        st.image(img, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Predicting... Please wait."):
            predicted_class_idx, predicted_class_name, predictions = predict_image(img_array)

        st.success(f"Predicted Class: **{predicted_class_name.capitalize()}**")

        nutrition_data = fetch_nutrition_info(predicted_class_name)

        if nutrition_data:
            st.header("Nutritional Information and Goals")
            # Create two columns
            col1, col2 = st.columns(2)

            # Nutritional Information
            with col1:
                st.subheader("Nutritional Information")
                calories = nutrition_data.get('nf_calories', 0)
                protein = nutrition_data.get('nf_protein', 0)
                fat = nutrition_data.get('nf_total_fat', 0)
                carbs = nutrition_data.get('nf_total_carbohydrate', 0)
                fiber = nutrition_data.get('nf_dietary_fiber', 0)
                sodium = nutrition_data.get('nf_sodium', 0)
                st.write(f"Calories: {calories} kcal")
                st.write(f"Protein: {protein} g")
                st.write(f"Fat: {fat} g")
                st.write(f"Carbs: {carbs} g")
                st.write(f"Fiber: {fiber} g")
                st.write(f"Sodium: {sodium} mg")

            # Daily Nutritional Goals Progress
            with col2:
                st.subheader("Daily Nutritional Goals Progress")
                daily_goals = {
                    'Calories': 2000,
                    'Protein': 50,
                    'Fat': 70,
                    'Carbs': 310,
                    'Fiber': 25,
                    'Sodium': 2300
                }
                labels = ['Calories', 'Protein', 'Fat', 'Carbs', 'Fiber', 'Sodium']
                values = [calories, protein, fat, carbs, fiber, sodium]
                for label, value in zip(labels, values):
                    progress = min(value / daily_goals[label], 1.0)
                    st.progress(progress)
                    st.write(f"{label}: {value}/{daily_goals[label]}")

            # Visualizations
            st.header("Augmented Visualizations")
            st.subheader("Radar Chart")
            plot_radar_chart(labels, values)

        else:
            st.warning(f"No nutritional information available for {predicted_class_name.capitalize()}.")

        # Prediction Probabilities
        st.header("Prediction Probabilities")
        df_probabilities = pd.DataFrame(predictions, index=class_names, columns=['Probability'])
        df_probabilities = df_probabilities.sort_values(by='Probability', ascending=False)
        st.bar_chart(df_probabilities.head(10))

    else:
        st.info("Upload an image to get started.")

elif sidebar_option == "📊Model Architecture":

    # Explanation of CNNs and EfficientNet
    st.write("### How Convolutional Neural Networks (CNNs) Work")
    st.write("""
    Convolutional Neural Networks (CNNs) are a class of deep learning models that have proven to be very effective for image classification tasks. CNNs use a special architecture designed to automatically learn features from images through convolutional layers.

    - `Convolutional Layers`: These layers apply convolutional filters (also called kernels) that slide over the input image. The filter performs a mathematical operation to produce a feature map that represents certain features such as edges, textures, and patterns in the image.
    - `Pooling Layers`: These layers reduce the spatial dimensions (height and width) of the feature map, making the model computationally efficient and less likely to overfit. Max pooling is the most common technique used, which takes the maximum value from a region of the feature map.
    - `Fully Connected Layers`: After several convolutional and pooling layers, the model flattens the feature maps and passes them through fully connected layers for classification.

    CNNs excel in image recognition tasks because they can capture spatial hierarchies in images.
    """)

    # Visualizing Convolution Operation
    st.write("#### Convolution Operation 🌀")
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])  # Simple edge detection filter
    path_img=os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),'ml_pipeline'),'sample_image.jpeg')
    img = load_image(path_img)  # Provide a sample food image path for convolution visualization
    plot_convolution_operation(img, kernel)

    # Visualizing Pooling Operation
    st.write("#### Max Pooling Operation 🔽")
    plot_pooling_operation(img)

    st.write("### EfficientNet: A State-of-the-Art CNN Architecture 🚀")
    st.write("""
    EfficientNet is an advanced CNN architecture that achieves state-of-the-art performance while being more efficient than traditional architectures like ResNet or VGG. It uses a compound scaling method that scales the depth, width, and resolution of the network in a balanced manner to optimize both accuracy and efficiency.

    **Why EfficientNet is Better**:
    - `Compound Scaling`: EfficientNet scales the network's depth, width, and resolution simultaneously, which allows it to achieve high accuracy with fewer parameters.
    - `Lightweight Model`: EfficientNet models are more lightweight compared to other CNNs like ResNet, which makes them faster to train and deploy without compromising performance.
    - `High Accuracy`: EfficientNet has been shown to outperform many other architectures on various image classification benchmarks.

    This makes EfficientNet an ideal choice for our food classification model.
    """)

    # Visualizing EfficientNet Block
    st.write("#### EfficientNet Block 🔧")
    plot_efficientnet_b0_with_labels()

    st.write("### Dataset: Food101 🍔")
    st.write("""
    The Food101 dataset is a large-scale dataset containing 101 different categories of food, with 101,000 images in total. Each class contains 1,000 images, and the dataset is split into training and test sets.

    This dataset is well-suited for food classification tasks due to its variety and large number of samples per category, which helps the model generalize well.

    ### Data Augmentation and Mixed Precision Training ⚡
    - `Data Augmentation`: To improve generalization and prevent overfitting, various data augmentation techniques (such as random rotations, flipping, and zooming) are applied to the training images.
    - `Mixed Precision Training`: Mixed precision training is a technique that uses lower-precision arithmetic (like FP16) to reduce memory usage and increase the training speed while maintaining model accuracy. It helps in accelerating training on GPUs without sacrificing the performance of the model.
    """)

elif sidebar_option == "🍏About":
    st.title("About 🍏")
    st.write("""
    Food Vision Pro uses deep learning to classify food images 🍔 and provide nutritional information 🍎. The model is built using **EfficientNet** and trained on the **Food101** dataset.
    """)
