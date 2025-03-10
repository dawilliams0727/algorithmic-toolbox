from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    # sort segments by end points
    segments.sort(key = lambda x: x.end)
# iterate through segments and find overlaps
    overlaps = set()
    overlap_freq = {}
    intersected = {k: False for k in segments} #keep track of which segments have been interesected with
    while False in intersected.values():
        # because sorted by ends, each segment needs to check if its start overlaps with preceding segments ends
        for i in range(len(segments)):
            # must check current segment i against all prior segments
            for j in range(i):
               # print(f"checking {segments[i]} for overlap with {segments[j]}")
            # this segment end must be greater than that segments start
                if segments[i].start <= segments[j].end:
                    # overlap starts at furthest right of the two segments starts, and the preceding segments end)
                    overlap = Segment(max(segments[j].start, segments[i].start), segments[j].end)
                    #print(f"\tfound overlap {overlap}")
                    overlaps.add(overlap)
                    if overlap not in overlap_freq:
                        overlap_freq[overlap] = set([segments[i], segments[j]])
                    else:
                        overlap_freq[overlap].update([segments[i], segments[j]])
            
            # check segment against found overlaps
            for o in overlaps:
                if segments[i].start <= o.start <=segments[i].end or segments[i].start <= o.end <=segments[i].end:
                    #print(f"adding {segments[i]} to existing overlap {o}")
                    overlap_freq[o].update([segments[i]])
            #print(f"\n\n{overlap_freq}\n\n")

    # sort overlaps by number of segments containing overlap
        ordered_overlaps = sorted(list(overlaps), key = lambda x: len(overlap_freq[x]), reverse=False)

        # pick highest frequency overlap and mark the associated segments as intersected
    
        most_overlap = ordered_overlaps.pop()
        points.append(most_overlap.end)
        #print(f"Highest Overlap: {most_overlap}")
        #print(segments)
        for segment in overlap_freq[most_overlap]:
            #print(segment)
            intersected[segment] = True

        for segment in filter(lambda x: intersected[x] == False, intersected):
            points.append(segment.end)
            intersected[segment] = True

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
