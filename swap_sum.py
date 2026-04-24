def swap_sum(A, B):
    sumA = sum(A)
    sumB = sum(B)

    diff = sumB - sumA - 10

    # must be even, otherwise impossible
    if diff % 2 != 0:
        return None

    target = diff // 2

    i, j = 0, 0

    while i < len(A) and j < len(B):
        current = B[j] - A[i]

        if current == target:
            return (i, j)
        elif current < target:
            j += 1
        else:
            i += 1

    return None