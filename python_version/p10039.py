def result():
    inputs = []

    for i in range(5):
        inputs.append(int(input()))

    for i in range(5):
        if inputs[i] < 40:
            inputs[i] = 40

    avg = 0
    for i in inputs:
        avg += i

    print(avg//5)