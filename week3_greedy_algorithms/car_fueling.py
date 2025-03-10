from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    # check if distance between any two stops is larger than tank, if so return -1
    if len(stops) == 0:
        if distance <= tank:
            return 0
        else: 
            return -1
    if distance - stops[-1] > tank:
        return -1
    for i in range(1, len(stops)):
        if stops[i] - stops[i-1] > tank:
            return -1
    # initialize refills to 0
    # until destination is reached...
    # if distance < tank, return refills
    # if not, choose the furthest reachable stop
    # increment refills
    return distance // tank


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
