import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

image = image.astype(int)

total = 0
count = 0
min_value = 255
max_value = 0

for row in image:
    for pixel in row:
        for value in pixel:
            
            total += value
            count += 1

            if value < min_value:
                min_value = value

            if value > max_value:
                max_value = value

mean = total / count

print("Mean Pixel Intensity:", mean)
print("Minimum Pixel Value:", min_value)
print("Maximum Pixel Value:", max_value)
