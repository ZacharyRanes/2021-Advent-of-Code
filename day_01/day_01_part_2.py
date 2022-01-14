def main():
    depths_array = []
    depth_increases = 0

    with open('input', 'r', encoding="UTF-8") as depth_file:
        depths_array = depth_file.readlines()

    for i in range(3, len(depths_array)):
        if (int(depths_array[i]) + int(depths_array[i-1]) + int(depths_array[i-2])) > (int(depths_array[i-1]) + int(depths_array[i-2]) + int(depths_array[i-3])):
            depth_increases += 1

    print(depth_increases)


if __name__ == "__main__":
    main()
