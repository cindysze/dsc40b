def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')

    for x, c in zip(data, colors):
        if c == 'blue':
            max_blue = max(max_blue, x)
        else:  # red
            min_red = min(min_red, x)

    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):

    loss = 0

    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):

    pairs = sorted(zip(data, colors))
    sorted_data = [x for x, _ in pairs]

    candidates = [sorted_data[0] - 1]

    for i in range(len(sorted_data) - 1):
        candidates.append(
            (sorted_data[i] + sorted_data[i + 1]) / 2
        )

    best_theta = candidates[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in candidates:
        loss = compute_ell(data, colors, theta)

        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta


def minimize_ell_sorted(data, colors):

    blue_gt_theta = colors.count('blue')
    red_le_theta = 0

    best_loss = blue_gt_theta
    best_theta = data[0] - 1

    for i in range(len(data)):

        if colors[i] == 'blue':
            blue_gt_theta -= 1
        else:  # red
            red_le_theta += 1

        current_loss = red_le_theta + blue_gt_theta

        if i < len(data) - 1:
            current_theta = (data[i] + data[i + 1]) / 2
        else:
            current_theta = data[i] + 1

        if current_loss < best_loss:
            best_loss = current_loss
            best_theta = current_theta

    return best_theta


if __name__ == "__main__":
    data = [1, 2, 3, 4]
    colors = ['blue', 'red', 'blue', 'red']

    theta = minimize_ell(data, colors)

    print("theta =", theta)
    print("loss =", compute_ell(data, colors, theta))