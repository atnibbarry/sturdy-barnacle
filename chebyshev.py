def chebyshev_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Les vecteurs doivent avoir la même longueur")
    return max([abs(a - b) for a, b in zip(v1, v2)])
