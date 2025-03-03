def solution(N, stages):
    answer = []

    size = len(stages)
    d = {}
    for i in range(1, N + 1):
        if (stages.count(i) == 0):
            d[i] = 0
            continue

        d[i] = stages.count(i) / size
        size -= stages.count(i)

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in d:
        answer.append(i[0])

    return answer