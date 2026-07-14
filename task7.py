import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

height = image.shape[0]
width = image.shape[1]

if len(image.shape) == 3:
    channels = image.shape[2]
else:
    channels = 1

bit_depth = image.dtype.itemsize * 8

memory_bytes = height * width * channels * (bit_depth / 8)

memory_MB = memory_bytes / (1024 * 1024)

print("Height:", height)
print("Width:", width)
print("Number of Channels:", channels)
print("Bit Depth:", bit_depth, "bits")
print("Memory Size in Bytes:", int(memory_bytes))
print("Memory Size in MB:", memory_MB)