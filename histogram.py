def histogram(points, bins):
    n = len(points)
    result = []

    i = 0

    for (a, b) in bins:
        count = 0

        while i < n and points[i] < b:
            if points[i] >= a:
                count += 1
            i += 1

        width = b - a
        density = count / (n * width)
        result.append(density)

    return result