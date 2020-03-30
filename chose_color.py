import numpy as np
def choose_color():
    clrs = []
    n = np.random.randint(4,900)
    #np.random.RandomState(seed = n)
    for i in range(n):
        rv = np.random.exponential()
        if rv < 0.15:
            clrs.append("red")
        elif rv < 0.30:
            clrs.append("skyblue")
        elif rv < 0.50:
            clrs.append("yellow")
        elif rv < 0.70:
            clrs.append("black")
        else:
            clrs.append("white")
    np.random.shuffle(clrs)
    color = np.random.choice(clrs)
    return color

