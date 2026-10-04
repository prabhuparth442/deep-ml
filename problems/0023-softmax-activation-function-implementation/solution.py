import math

def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    l = [math.exp(x-m) for x in scores]
    s = sum(l)
    scores = [x/s for x in l]
    return scores