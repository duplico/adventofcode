import fileinput

from shapely.geometry import LineString, MultiLineString, MultiPoint
from shapely.ops import unary_union, linemerge

def main():
    lines = []
    intersections = 0
    for line in fileinput.input():
        p1, p2 = line.split(' -> ')

        p1 = tuple(map(lambda a: int(a), p1.split(',')))
        p2 = tuple(map(lambda a: int(a), p2.split(',')))

        line = LineString([p1, p2])
        
        # Only consider horizontal or vertical lines:
        if p1[0] == p2[0] or p1[1] == p2[1]:
            lines.append(line)


    # 0,9 - 5,9 : 0,9 - 2,9
    # 7,0 - 7,4 : 9,4 - 3,4
    # 3,4 - 1,4 : 9,4 - 3,4

    intersection_list = []

    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if lines[i].intersects(lines[j]):
                isect = lines[i].intersection(lines[j])
                # print(f"It appears {lines[i]} intersects {lines[j]} x {isect.length+1}, with:")
                # print(f"  {isect}")
                intersection_list.append(isect)
    intersections_union = unary_union(intersection_list)
    
    print(intersections_union)

    points = MultiPoint([geom_item for geom_item in intersections_union.geoms if geom_item.geometryType() == 'Point'])
    print(points)

    lines = MultiLineString([geom_item for geom_item in intersections_union.geoms if geom_item.geometryType() == 'LineString'])

    for line in lines.geoms:
        print(line, line.intersects(points))

    print(linemerge(lines).length)
    exit()

    for geom_item in intersections_union.geoms:
        intersections += geom_item.length
        if geom_item.geometryType() == 'Point':
            intersections += 1
        elif geom_item.geometryType() == 'LineString':
            intersections += geom_item.length + 1
        else:
            raise ValueError("Got a bad geometry type.")

    print(intersections)

    # print(intersections_union.geoms[0].geometryType())
    # print(dir(intersections_union.geoms[0]))


if __name__ == '__main__':
    main()
