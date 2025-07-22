import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
import textwrap
import re

# Load the data
file_path = 'captions.txt'
image_folder = 'Images/'

# Read the file
data = pd.read_csv(file_path)

# Clean up the captions immediately after loading

# 1. Remove extra spaces from captions
data['caption'] = data['caption'].str.strip()

# 2. Remove special symbols 
data['caption'] = data['caption'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', x))

# 3. Remove duplicate captions
data = data.drop_duplicates(subset=['caption'])

# 4. Remove rows where the caption is empty
data = data[data['caption'].notna()]

# Display first lines of captions
print("Columns in dataset:", data.columns)
print(data.head())


# Sample 10 random rows
sampled_data = data.sample(10)

# Show the images with their captions
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
axes = axes.flatten()

for i, (index, row) in enumerate(sampled_data.iterrows()):
    
    img_path = os.path.join(image_folder, row['image']) 
    try:
        # Load and display the image
        img = Image.open(img_path)
        axes[i].imshow(img)

        # make text look better with images
        caption = row['caption']
        wrapped_caption = textwrap.fill(caption, width=30)  

        axes[i].set_title(wrapped_caption, fontsize=10, pad=10) 
        axes[i].axis('off')
    except Exception as e:
        # Error checking if files cannot be read
        axes[i].axis('off')
        axes[i].set_title("Image not found")
        print(f"Error loading image {img_path}: {e}")

for j in range(len(sampled_data), len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()

# Print the cleaned data
print(data.head())
