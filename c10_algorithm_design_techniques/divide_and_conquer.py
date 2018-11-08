
inf = float('inf')


class ClosestPoint:
    def __init__(self, points):
        self.points = points
        self.xset = sorted(self.points, key=lambda x: x[0])
        self.yset = sorted(self.points, key=lambda x: x[1])

    def distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

    def closest(self, points=None, yset=None):
        if points is None:
            points = list(self.xset)
        if yset is None:
            yset = list(self.yset)
        if not points or len(points) == 1:
            return inf
        if len(points) == 2:
            return self.distance(points[0], points[1])
        center_ind = len(points) // 2
        left_part = points[:center_ind]
        right_part = points[center_ind:]
        center = (left_part[-1][0] + right_part[0][0]) / 2
        left_yset = []
        right_yset = []
        for x in yset:
            if x[0] <= center:
                left_yset.append(x)
            else:
                right_yset.append(x)
        left_min = self.closest(left_part, left_yset)
        right_min = self.closest(right_part, right_yset)
        width = min(left_min, right_min)
        new_points = []
        for point in yset:
            if center - width <= point[0] <= center + width:
                new_points.append(point)
        yset = new_points
        if len(yset) < 2:
            return width
        for x in yset[:-1]:
            for y in yset[1:]:
                if y == x:
                    continue
                if y[1] - x[1] > width:
                    break
                dis = self.distance(x, y)
                if dis < width:
                    width = dis
        return width


if __name__ == '__main__':
    points = [
        (1, 2),
        (1, 1),
        (2, -1),
        (0, 0),
        (1, 0),
        (1, 4),
    ]
    p = ClosestPoint(points)
    print(p.closest())

