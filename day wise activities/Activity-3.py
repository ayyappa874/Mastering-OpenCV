import cv2
import numpy as np
import matplotlib.pyplot as plt

# Get uploaded image name
image_name = list(uploaded.keys())[0]

# Read image
image = cv2.imread(image_name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create empty mask
region = np.zeros(gray.shape, np.uint8)

# Seed point (Change if needed)
seed_x = gray.shape[0] // 2
seed_y = gray.shape[1] // 2

# Threshold difference
threshold = 15

# Get seed intensity
seed_value = gray[seed_x, seed_y]

# Stack for region growing
stack = [(seed_x, seed_y)]
region[seed_x, seed_y] = 255

# Region Growing
while stack:
    x, y = stack.pop()

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:

            nx, ny = x + dx, y + dy

            if (0 <= nx < gray.shape[0] and 
                0 <= ny < gray.shape[1] and 
                region[nx, ny] == 0):

                if abs(int(gray[nx, ny]) - int(seed_value)) < threshold:
                    region[nx, ny] = 255
                    stack.append((nx, ny))

# Display Results
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Region Traced")
plt.imshow(region, cmap='gray')
plt.axis("off")

plt.show()
