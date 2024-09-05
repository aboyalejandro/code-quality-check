def calculate_area_of_rectangle(width, height):
    return width * height


def calculate_area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius


def print_area(shape, area):
    print(f"The area of the {shape} is: {area}")


def main():
    rectangle_width = 5
    rectangle_height = 10
    circle_radius = 7

    rectangle_area = calculate_area_of_rectangle(rectangle_width, rectangle_height)
    circle_area = calculate_area_of_circle(circle_radius)

    print_area("rectangle", rectangle_area)
    print_area("circle", circle_area)


if __name__ == "__main__":
    main()
