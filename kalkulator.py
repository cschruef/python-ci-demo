def addiere(a, b):
    return a + b


def teile(a, b):
    if b == 0:
        raise ValueError("Teilen durch null geht nicht")
    return a / b