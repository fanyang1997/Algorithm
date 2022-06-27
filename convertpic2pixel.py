from PIL import Image
import matplotlib.pyplot as plt

# img = Image.open('/home/pi/Desktop/test.jpg')
# img.show()


def photo2pixelart(image, i_size, o_size):
    """
    image: path to image file
    i_size: size of the small image eg:(8,8)
    o_size: output size eg:(10000,10000)
    """
    # read file
    img = Image.open(image)

    # convert to small image
    small_img = img.resize(i_size, Image.BILINEAR)

    # resize to output size
    res = small_img.resize(img.size, Image.NEAREST)

    # Save output image
    # filename = f'mario_{i_size[0]}x{i_size[1]}.png'
    # res.save(filename)

    # Display images side by side
    plt.figure(figsize=(16, 10))
    # original image
    plt.subplot(1, 2, 1)
    plt.title('Original image', size=18)
    plt.imshow(img)  # display image
    plt.axis('off')  # hide axis
    # pixel art
    plt.subplot(1, 2, 2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    img = Image.open('./007bnLd7ly1gtfee96q2aj31hc0u0qv5.jpeg')
    photo2pixelart("./007bnLd7ly1gtfee96q2aj31hc0u0qv5.jpeg",
                   i_size=(200, 200),
                   o_size=img.size)
