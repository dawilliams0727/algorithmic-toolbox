from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def points_cover(starts, ends, points):
    # create segments
    segments = list(zip(starts,ends))
    # maybe sort segments by start points?
    segments.sort(key = lambda x: [x][0])
    count = [0] * len(points)
    def recursive(segments, points):
        # if there are no segments, there can be no points intersecting
        if len(segments) == 0:
            return
        if len(segments) == 1:
            # if there is one segment, check all points against it
            start = segments[0][0]
            end = segments[0][1]
            for index, point in enumerate(points):
                if start <= point <= end:
                    count[index] += 1
            return
        # split segments and points into halves and recurse
        s,p = len(segments) // 2, len(points) // 2
        left, right =(segments[:s], points[:]), (segments[s:], points[:])
        # check each point for containment in each segment of smaller group
        recursive(*left), recursive(*right)
    
    recursive(segments, points)    
    return count

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)