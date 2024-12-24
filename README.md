# Food Vision Pro 🍔🍏

Food Vision Pro is a deep learning-based food classification model built using **EfficientNet** architecture. The app allows users to upload food images, predict the food type, and track its nutritional information. The model is trained on the **Food101** dataset and offers a complete food classification experience.

## Key Features 🚀

- **Image Classification**: Predict the type of food in an image using a pre-trained EfficientNet model.
- **Nutritional Information**: Fetch nutritional data of the predicted food item using the Nutritionix API.
- **Visualization**: View the model's architecture, including convolution and pooling operations, and radar charts for nutrition data.

## Table of Contents 📚

- [Introduction](#introduction)
- [CNN and EfficientNet Architecture](#cnn-and-efficientnet-architecture)
- [Transfer Learning](#transfer-learning)
- [Food101 Dataset](#food101-dataset)
- [Model Training and Fine-tuning](#model-training-and-fine-tuning)
- [App Features and Functionality](#app-features-and-functionality)
- [How to Run the Project](#how-to-run-the-project)
- [License](#license)

## Introduction 🎯

Food Vision Pro uses deep learning techniques to classify food items in images and provide nutritional insights. The app integrates **Convolutional Neural Networks (CNNs)** and the state-of-the-art **EfficientNet architecture** to achieve high accuracy with fewer parameters. The goal is to provide a seamless food classification experience for users by combining image recognition and nutritional analysis.

## CNN and EfficientNet Architecture 🧠

### Convolutional Neural Networks (CNNs) 🌀

CNNs are a class of deep learning models designed to automatically learn features from images through convolutional layers. The CNN architecture consists of:

- **Convolutional Layers**: Apply filters (kernels) over the input image to extract feature maps representing various patterns like edges, textures, and shapes.
- **Pooling Layers**: Reduce the spatial dimensions (height and width) of feature maps using techniques like max pooling to improve computational efficiency and prevent overfitting.
- **Fully Connected Layers**: Flatten the feature maps and pass them through dense layers for classification.

CNNs excel in image recognition tasks because they capture spatial hierarchies in images, enabling them to understand complex patterns.

### EfficientNet Architecture 🚀

EfficientNet is an advanced CNN architecture known for its superior performance and efficiency. It uses **compound scaling**, which scales the depth, width, and resolution of the network simultaneously to optimize accuracy and efficiency.

Key advantages of EfficientNet:
- **Compound Scaling**: EfficientNet scales the network's depth, width, and resolution, improving performance with fewer parameters.
- **Lightweight**: EfficientNet models are computationally efficient and faster to train, making them ideal for deployment.
- **High Accuracy**: EfficientNet outperforms traditional models like ResNet and VGG on various image classification tasks.

The **EfficientNet-B0** model is used in this project, which is optimized for a 224x224 input image size, making it suitable for food classification.

## Transfer Learning ⚡

In this project, **transfer learning** is utilized, where a pre-trained EfficientNet model is fine-tuned on the Food101 dataset. Transfer learning allows the model to leverage the knowledge learned from a large dataset like ImageNet and adapt it to the specific task of food classification. This reduces the amount of training data and time needed to achieve good performance.

The pre-trained EfficientNet model is fine-tuned using the Food101 dataset, which contains images from 101 food categories, and the model is adapted to classify food types with high accuracy.

## Food101 Dataset 🍽️

The **Food101** dataset is a large-scale food image dataset containing 101 categories of food, with 101,000 images in total. Each class has 1,000 images, and the dataset is split into training and test sets.

The Food101 dataset includes various food items like:

- Apple pie
- Beef carpaccio
- Caesar salad
- Chicken curry
- Cheesecake
- Donuts
- Pizza
- Sushi
- Waffles

This diverse set of food categories helps the model generalize well for food image classification tasks.

## Model Training and Fine-tuning 🏋️‍♂️

- The model was pre-trained on the **ImageNet** dataset.
- **Transfer learning** was applied to fine-tune the model on the Food101 dataset.
- Data augmentation techniques, like random rotations, flipping, and zooming, were applied to the training images to improve generalization.
- **Mixed precision training** was used to speed up training while maintaining accuracy.

The fine-tuned model was then deployed using **TensorFlow** and integrated into the app for real-time predictions.

## App Features and Functionality 🖥️

The app includes the following features:

- **Image Upload**: Users can upload food images to the app.
- **Prediction**: The model predicts the food type based on the uploaded image.
- **Nutritional Information**: Nutritional data is fetched from the **Nutritionix API** and displayed to the user.
- **Visualizations**: The app provides various visualizations, including:
  - Convolution operations with filters.
  - Max pooling operations to show how image features are downsampled.
  - A radar chart to visualize nutritional information.
- **Prediction Probabilities**: The app shows a bar chart with the top 10 predicted food classes and their corresponding probabilities.

## How to Run the Project 🚀

### Prerequisites

1. **Nutritionix API Access**:  
   In order to fetch nutritional information, you need an API key and an app ID from Nutritionix. You can get your credentials by registering on their platform:

   - Visit the [Nutritionix Developer Portal](https://developer.nutritionix.com/)
   - Sign up and generate an **API Key** and **App ID**.

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

### Running the App

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/food-vision-pro.git
   cd food-vision-pro

2. Update the app with your Nutritionix API credentials (API Key and App ID) in the config.py or relevant section of the code.

3. Run the Streamlit app:
   ```bash
   streamlit run app.py

4. Visit the local URL (usually http://localhost:8501) to start using the app

### License ⚖️
his project is licensed under the MIT License - see the LICENSE file for details.

### Key Updates:
1. **Nutritionix API Access**: Instructions for getting the API key and App ID from Nutritionix.
2. **Running the App**: Added a section to configure the API credentials before running the app.
   
This ensures that the users know how to set up the Nutritionix API and run the app successfully.

