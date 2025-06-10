import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110' # Đánh dấu kết thúc thông điệp

    # Iterate through pixels to hide message
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel(((col, row)))) # Get pixel as a list (R, G, B, [A])

            # Iterate through R, G, B (and A if present) channels
            for color_channel in range(3): # Assuming RGB image, if RGBA, needs adjustment to 4
                if data_index < len(binary_message):
                    # Change the least significant bit (LSB) of the color channel
                    # Get current LSB: pixel[color_channel] % 2
                    # Replace LSB with the bit from binary_message
                    # pixel[color_channel] >> 1 : shift right to remove current LSB
                    # << 1: shift left to make space for new LSB
                    # | int(binary_message[data_index], 2): OR with new LSB bit
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            img.putpixel(((col, row), tuple(pixel)))

            # Check if all bits of the message have been hidden
            if data_index >= len(binary_message):
                break # Exit inner and outer loops if message is fully hidden
        if data_index >= len(binary_message): # Check again to break outer loop
            break