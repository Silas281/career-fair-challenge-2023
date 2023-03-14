import ReadFrCmd  # Read file name from command line
import ReadWrite  # Read and write CSV file


class FindSafeTraingle:
    def __init__(self):
        # Read file name from command line
        self.filename = ReadFrCmd.ReadCMD().read_cmd()
        # Read points from CSV file
        self.points = ReadWrite.CSVFILEIO(self.filename).read_csv()
        # Number of points
        self.n = len(self.points)
        # Maximum area of a triangle
        self.max_area = 0
        # Largest triangle
        self.largest_triangle = None

    def distance(self, p1, p2):
        # Calculate the distance between two points
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    def is_valid_triangle(self, points):
        # Check if any unsafe point is inside the triangle
        for p in self.points:
            d1 = self.distance(points[0], p)
            d2 = self.distance(points[1], p)
            d3 = self.distance(points[2], p)
            if d1 + d2 + d3 <= 2 * max(d1, d2, d3):
                return False
        return True

    def area(self, points):
        # Calculate the area of a triangle using the area formula
        return abs(0.5 * sum(x1*y2 - x2*y1 for ((x1, y1), (x2, y2)) in ((points[i], points[(i+1) % 3]) for i in range(3))))

    def find_largest_empty_triangle(self):
        # find safe largest traingle
        for i in range(self.n):
            for j in range(i+1, self.n):
                for k in range(j+1, self.n):
                    points = [self.points[i], self.points[j], self.points[k]]
                    # print(points)
                    # if self.is_valid_triangle(points):
                    area = self.area(points)
                    if area > self.max_area:
                        self.max_area = area
                        self.largest_triangle = points
        return self.largest_triangle

    def write_largest_empty_triangle(self):
        # write largest empty traingle to csv file
        ReadWrite.CSVFILEIO(self.filename).write_to_csv(
            "triangleOut.csv", self.largest_triangle)


if __name__ == "__main__":
    # execute only if run as a script
    FindTriangle = FindSafeTraingle()
    # find safe largest traingle and write to csv file
    FindTriangle.write_largest_empty_triangle()
