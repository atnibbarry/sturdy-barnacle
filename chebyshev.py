def chebyshev_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Il faut que les vecteurs ont la même longueur!!!")
    max_diff = 0
    for a, b in zip(v1, v2):
        diff = abs(a - b)
        if diff > max_diff:
            max_diff = diff
    return max_diff
