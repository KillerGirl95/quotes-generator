from PIL import Image, ImageDraw, ImageFont

def draw_text_with_wrapping(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        # cond - adding next word exceeds maximum width
        if draw.textbbox((0, 0), current_line + ' ' + word, font=font)[2] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

#loading image
image = Image.open("quo_img.jpg")

# Create a drawing object
draw = ImageDraw.Draw(image)
with open ("quote.txt","r") as text_file:
    text_content= text_file.readline()
font_size = 40
font = ImageFont.truetype("arial.ttf", font_size)

# Maximum wrapping width  
max_width = 400

#  position to center text
image_width, image_height = image.size
text_x = (image_width - max_width) // 2
text_y = 150

# Draw wrapped text 
wrapped_lines = draw_text_with_wrapping(draw, text_content, font, max_width)

for i, line in enumerate(wrapped_lines):
    bbox = draw.textbbox((text_x, text_y + i * font.getmask(line).getbbox()[3]), line, font=font)
    draw.text((text_x, text_y + i * (bbox[3] - bbox[1])), line, font=font, fill=(255, 255, 255))

image.save("final_img.jpg") 
image.show() 
