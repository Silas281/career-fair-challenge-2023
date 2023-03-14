
import ReadFrCmd  # read file name from command line
import ReadWrite  # read and write CSV file


class FindSafePoint:
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

    def find_all_triangles(self):
        # find all traingles
        traingles = []
        for i in range(self.n):
            for j in range(i+1, self.n):
                for k in range(j+1, self.n):
                    points = [self.points[i], self.points[j], self.points[k]]
                    # print(points)
                    # if self.is_valid_triangle(points):
                    area = self.area(points)
                    if area > 0:
                        traingles.append(points)
        return traingles

    def find_traingles_person_in(self, person, traingles):
        # find traingles with person in
        traingles_person_in = []
        for traingle in traingles:
            main_traingle_area = self.area(traingle)
            triangle1 = [traingle[0], traingle[1], person]
            triangle2 = [traingle[0], traingle[2], person]
            triangle3 = [traingle[1], traingle[2], person]
            triangle1_area = self.area(triangle1)
            triangle2_area = self.area(triangle2)
            triangle3_area = self.area(triangle3)
            if triangle1_area + triangle2_area + triangle3_area == main_traingle_area:
                traingles_person_in.append(traingle)
        return traingles_person_in

    def find_single_safe_traingle(self, traingles_person_in):
        # find traingle with person in and no other point in
        for traingle in traingles_person_in:
            # check if any other point in
            other_point_in = False
            for point in self.points:
                if point not in traingle:
                    d1 = self.distance(traingle[0], point)
                    d2 = self.distance(traingle[1], point)
                    d3 = self.distance(traingle[2], point)
                    if d1 + d2 + d3 <= 2 * max(d1, d2, d3):
                        other_point_in = True
                        break
            if not other_point_in:
                return traingle
        return None

    def write_safe_traingle(self):
        # all traingles]
        traingles = self.find_all_triangles()
        traingles_person_in = self.find_traingles_person_in(
            self.points[0], traingles)
        safe_traingle = self.find_single_safe_traingle(traingles_person_in)
        # find safe traingle

        ReadWrite.CSVFILEIO(self.filename).write_to_csv(
            "SafePointOut.csv", safe_traingle)


if __name__ == "__main__":
    # Find safe point and write to CSV file
    FindS = FindSafePoint()

    FindS.write_safe_traingle()
