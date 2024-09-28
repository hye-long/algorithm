def solution(a, b, c, d):
    from collections import Counter
    
    dice = [a, b, c, d]
    counter = Counter(dice)
    
    if len(counter) == 1:
        p = a
        return 1111 * p
    
    elif len(counter) == 2:
        values = list(counter.values())
        keys = list(counter.keys())
        
        if 3 in values:
            # 세 주사위가 같은 숫자인 경우
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            # 두 주사위씩 같은 숫자인 경우
            p, q = keys
            return (p + q) * abs(p - q)
    elif len(counter) == 3:
        # 두 주사위만 같은 숫자인 경우
        keys = list(counter.keys())
        values = list(counter.values())
        p = keys[values.index(2)]
        q = keys[values.index(1)]
        r = keys[values.index(1, values.index(1) + 1)]
        return q * r
    else:
        # 네 주사위가 모두 다른 숫자인 경우
        return min(dice)

