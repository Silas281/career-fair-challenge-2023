import csv
import os


class CSVFILEIO:
    # Constructor
    def __init__(self, filename):
        self.filename = filename

    # Read CSV file
    def read_csv(self):
        points = []
        try:
            with open(self.filename) as csv_file:
                csv_reader = list(csv.reader(csv_file, delimiter=','))
                for i in range(1, len(csv_reader)):
                    points.append(
                        (float(csv_reader[i][0]), float(csv_reader[i][1])))
            # close file
            csv_file.close()
            return points
        except FileNotFoundError:
            print("File not found")
            return None

    # Write CSV file

    def write_to_csv(self, filename, points):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['x', 'y'])
            for point in points:
                writer.writerow(point)
        # close file
        f.close()
        print("File written successfully")
