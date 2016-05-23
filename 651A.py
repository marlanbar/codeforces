a1, a2 = map(int, raw_input().split())


timeList = {}


def totalTime(a1, a2):
    print totalTimeAUX(a1, a2, 0, 0)


def totalTimeAUX(a1, a2, charger, time):
    global timeList
    if a1 <= 0 or a2 <= 0 or (a1 == 1 and a2 == 1):
        return time
    else:
        if (a1, a2, charger) in timeList:
            return timeList[a1, a2, charger]
        else:
            if charger == 0:
                timeList[a1, a2, 1] = totalTimeAUX(a1, a2, 1, time)
                timeList[a1, a2, 2] = totalTimeAUX(a1, a2, 2, time)
                return max(timeList[a1, a2, 1], timeList[a1, a2, 2])
            elif charger == 1:
                timeList[a1 + 1, a2 - 2, 1] = totalTimeAUX(a1 + 1, a2 - 2, 1, time + 1)
                timeList[a1 + 1, a2 - 2, 2] = totalTimeAUX(a1 + 1, a2 - 2, 2, time + 1)
                return max(timeList[a1 + 1, a2 - 2, 1], timeList[a1 + 1, a2 - 2, 2])
            else:
                timeList[a1 - 2, a2 + 1, 1] = totalTimeAUX(a1 - 2, a2 + 1, 1, time + 1)
                timeList[a1 - 2, a2 + 1, 2] = totalTimeAUX(a1 - 2, a2 + 1, 2, time + 1)
                return max(timeList[a1 - 2, a2 + 1, 1], timeList[a1 - 2, a2 + 1, 2])

totalTime(a1, a2)
