import collections

def minSteps(s: str, t: str) -> int:
    count_s=collections.Counter(s)
    result=0

    for item in t:
        if count_s[item] >0:
            count_s[item]-=1

        else:
            result+=1
    return result

