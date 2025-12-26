from vec3 import Vec3

image_width = 400
image_height = 200

def write_color(f, color):    #this function is to write the colors on the ppm file 
    r = int(255.999 * color.x)
    g = int(255.999 * color.y)
    b = int(255.999 * color.z)
    f.write(f"{r} {g} {b}\n")

with open("output.ppm", "w") as f:
    f.write("P3\n")
    f.write(f"{image_width} {image_height}\n")
    f.write("255\n")

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            color = Vec3(
                i / (image_width - 1),
                j / (image_height - 1),
                0.25
            )
            write_color(f, color)
