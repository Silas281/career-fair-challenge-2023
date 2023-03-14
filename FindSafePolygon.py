import math  # for math.atan2
import ReadWrite  # for ReadWrite.CSVFILEIO
import ReadFrCmd  # for ReadFrCmd.ReadCMD


class FindSafePolygon:

    def __init__(self):
        # Read file name from command line
        self.filename = ReadFrCmd.ReadCMD().read_cmd()
        # Read points from CSV file

        self.unsafe_points = ReadWrite.CSVFILEIO(self.filename).read_csv()
        self.n = len(self.unsafe_points)

    def distance(self, p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    def polar_angle(self, p1, p2):
        if p1[1] == p2[1]:
            return -math.pi
        dy = p1[1]-p2[1]
        dx = p1[0]-p2[0]
        return math.atan2(dy, dx)

    def orientation(self, p1, p2, p3):
        dy1 = p2[1]-p1[1]
        dx1 = p2[0]-p1[0]
        dy2 = p3[1]-p2[1]
        dx2 = p3[0]-p2[0]
        return (dx1*dy2 - dy1*dx2) <= 0

    def find_safe_polygon(self):
        p0 = min(self.unsafe_points, key=lambda p: (p[1], p[0]))
        self.unsafe_points.sort(key=lambda p: (
            self.polar_angle(p0, p), self.distance(p0, p)))
        stack = []
        for i in range(self.n):
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], self.unsafe_points[i]):
                stack.pop()
            stack.append(self.unsafe_points[i])
        return stack

    def write_safe_polygon_to_csv(self):
        ReadWrite.CSVFILEIO(self.filename).write_to_csv(
            "polygonOut.csv", self.find_safe_polygon())


if __name__ == "__main__":

    findSafeP = FindSafePolygon()

    safe_p = findSafeP.find_safe_polygon()
    print(safe_p)
    # Write safe polygon to CSV file
    findSafeP.write_safe_polygon_to_csv()
