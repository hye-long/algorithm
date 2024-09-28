def solution(numLog):
    control = ""
    for i in range(1, len(numLog)):
        c = numLog[i] - numLog[i-1]
        if c == 1:
            control += 'w'
        elif c == -1:
            control += 's'
        elif c == 10:
            control += 'd'
        elif c == -10:
            control += 'a'
    return control
