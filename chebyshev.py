def chebyshev_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Ils doivent avoir la même longueur")
    return max(map(lambda a_b: abs(a_b[0] - a_b[1]), zip(v1, v2)))
