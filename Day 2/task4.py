import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

image = image.astype(int)

total_pixels = 0
black_pixels = 0
white_pixels = 0
high_intensity_pixels = 0

for row in image:
    for pixel in row:
        

        intensity = (pixel[0] + pixel[1] + pixel[2]) / 3

        total_pixels += 1

        if intensity == 0:
            black_pixels += 1

        if intensity == 255:
            white_pixels += 1

        if intensity > 200:
            high_intensity_pixels += 1

# Display results
print("Total Pixels:", total_pixels)
print("Black Pixels:", black_pixels)
print("White Pixels:", white_pixels)
print("Pixels with Intensity > 200:", high_intensity_pixels)