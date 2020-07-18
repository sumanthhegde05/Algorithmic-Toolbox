import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    refils = 0
    initial=0
    for elem in range (0,len(stops)):
        if stops[elem]-initial <= tank:
            continue
        else:
            initial = stops[elem-1]
            if stops[elem]-initial > tank:
                return -1
            refils+=1
    return refils

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
