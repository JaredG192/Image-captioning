# 🖼️ Image Captioning AI

This project is a deep learning-based image captioning model developed as part of a machine learning course. It automatically generates descriptive captions for input images using a combination of Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs).

---

## 📁 Project Structure

- `caption.txt` – Text file containing 5 captions for each image  
- `Image_Captioning.py` – Python script containing the complete model pipeline: preprocessing, training, and caption generation  
- `Image_Captioning.ipynb` – Jupyter Notebook version for exploratory experiments, visualizations, and model evaluation  
- `sample_images/` – A small set of example images for testing and demonstration  

---

## 🧪 Objectives

- Train a model that can generate natural language descriptions for unseen images  
- Preprocess image and text data for deep learning  
- Build a CNN-LSTM architecture to encode image features and decode them into captions  
- Evaluate model quality using BLEU scores and qualitative output  

---

## 🛠️ Methods and Tools

**Languages & Libraries:**
- Python  
- TensorFlow / Keras  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- NLTK, Pillow  

**Techniques:**
- Data Cleaning & Tokenization  
- Feature Extraction using Pretrained CNNs (e.g., InceptionV3)  
- Text Vectorization and Sequence Padding  
- RNN Decoder with LSTM  
- Evaluation using BLEU Score  

---

## 📊 Key Features and Components

- **Image Preprocessing** – Images are resized and encoded using a pretrained CNN  
- **Text Preprocessing** – Captions are cleaned, tokenized, and converted to sequences  
- **Vocabulary Creation** – Tokenizer created for all unique words in the captions  
- **Model Architecture** – Combines CNN encoder + LSTM decoder with attention mechanism (if included)  
- **Caption Generation** – Greedy or beam search strategies used to predict the best caption  

---

## 📈 Results Summary

- The model was trained on the **Flickr8k** dataset  
- Achieved reasonable performance on test images with semantically correct and grammatically sound captions  
- BLEU scores were used to evaluate the quality of generated captions compared to human-written ones  

---

## 📂 Dataset

The dataset consists of 8,000 images, each with 5 human-annotated captions.

📥 Due to GitHub file size limits, the dataset is not included in this repository.
👉 [Flickr8k Image Captioning Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)



---

## 👨‍💻 Authors

**Jared Gonzalez**, 
**A Sai Prasanth Reddy**, 
**Tejaswi Chigurupati**


California State University, San Bernardino  
Bachelor in Science, Computer Science,  
Minor in Data Science  

---

## 📃 License

This project is for academic purposes and is shared under the MIT License.




