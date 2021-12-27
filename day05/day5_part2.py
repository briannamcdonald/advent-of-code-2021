def organize_data(lines):
    max_x = 0
    max_y = 0
    line_segments = []

    # store all of the line segments
    for line in lines:
        points = line.split(" -> ")
        point1 = points[0].split(",")
        point2 = points[1].split(",")
        x1 = int(point1[0].strip())
        y1 = int(point1[1].strip())
        x2 = int(point2[0].strip())
        y2 = int(point2[1].strip())
        line_segments.append([(x1, y1), (x2, y2)])

        # keep track of the maximum row and column values
        if x1 > max_x: max_x = x1
        if y1 > max_y: max_y = y1
        if x2 > max_x: max_x = x2
        if y2 > max_y: max_y = y2
    
    return line_segments, max_x, max_y


def main():
    data = open("day05/input.txt", "r")
    lines = [line for line in data]
    line_segments, max_x, max_y = organize_data(lines)

    # initialize diagram
    diagram = []
    for y in range(max_y + 1):
        diagram.append([])
        for x in range(max_x + 1):
            diagram[y].append(0)
    
    # fill out diagram
    for segment in line_segments:
        (x1, y1), (x2, y2) = segment
        if x1 == x2:
            larger_y = max([y1, y2])
            smaller_y = min([y1, y2])
            for y in range(smaller_y, larger_y + 1):
                diagram[y][x1] += 1
        elif y1 == y2:
            larger_x = max([x1, x2])
            smaller_x = min([x1, x2])
            for x in range(smaller_x, larger_x + 1):
                diagram[y1][x] += 1
        else:
            while x1 != x2 and y1 != y2:
                diagram[y1][x1] += 1
                
                if x1 > x2: 
                    x1 -= 1
                else: 
                    x1 += 1

                if y1 > y2: 
                    y1 -= 1
                else: 
                    y1 += 1
            diagram[y2][x2] += 1
    
    # count the values in the diagram that are >= 2
    counter = 0
    for row in diagram:
        for val in row:
            if val >= 2: counter += 1
    
    print(counter)


if __name__ == "__main__":
    main()