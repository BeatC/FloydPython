__author__ = 'Illia Daynatowicz'

import sys
sys.stderr = open("errors.txt", "w+")
class DMatrix:
    def __init__(self, n):
        self.n = n
        self.stage = 0
        self.matrix = []
        self.path_matrix = []
        for i in range(0, n):
            self.matrix.append([])
            self.path_matrix.append([])
            for j in range(0, n):
                self.matrix[i].append(999)
                self.path_matrix[i].append("{0}-{1}".format(i+1, j+1))

    def next(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if i == j:
                    self.path_matrix[i][j] = "-"
                min_variant = self.matrix[i][self.stage] + self.matrix[self.stage][j]
                if str(self.path_matrix[self.stage][j])[0:2].isdigit():
                    min_path = self.path_matrix[i][self.stage] + str(self.path_matrix[self.stage][j])[2:]
                else:
                    min_path = self.path_matrix[i][self.stage] + str(self.path_matrix[self.stage][j])[1:]
                if self.matrix[i][j]:
                    if min_variant < self.matrix[i][j]:
                        self.matrix[i][j] = min_variant
                        self.path_matrix[i][j] = min_path
        self.stage += 1

    def display(self):
        print("<table><tr><td></td>")
        for i in range(0, self.n):
            print("<th>x<sub>{0}</sub></th>".format(i+1))
        print("</tr>")

        for i in range(0, self.n):
            print("<tr><th>x{0}</th>".format(i+1))
            for j in range(0, self.n):
                if self.matrix[i][j] != 999:
                    print("<td>{0}</td>".format(self.matrix[i][j]), end="")
                else:
                    print("<td>&#x221e;</td>", end="")
            print("</tr>")
        print("</table>")

    def display_path(self):
        print("<table><tr><td></td>")
        for i in range(0, self.n):
            print("<th>x<sub>{0}</sub></th>".format(i+1))
        print("</tr>")

        for i in range(0, self.n):
            print("<tr><th>x{0}</th>".format(i+1))
            for j in range(0, self.n):
                if self.matrix[i][j] != 999:
                    print("<td>{0}</td>".format(self.path_matrix[i][j]), end="")
                else:
                    print("<td>-</td>", end="")
            print("</tr>")
        print("</table>")


    def set_matrix(self, matrix):
        self.matrix = matrix


sys.stdout = open("./index.html", "w+")

my_matrix = DMatrix(13)
matrix = [[0, 3, 3, 3, 5, 999, 999, 999, 999, 999, 999, 999, 999],
          [999, 0, 999, 999, 999, 3, 999, 2, 999, 999, 999, 999, 999],
          [999, 999, 0, 999, 999, 3, 2, 999, 999, 999, 999, 999, 999],
          [999, 999, 999, 0, 999, 1, 999, 2, 999, 999, 999, 999, 999],
          [999, 999, 999, 999, 0, 999, 2, 2, 999, 999, 999, 999, 999],
          [999, 999, 999, 999, 999, 0, 999, 999, 5, 2, 999, 999, 999],
          [999, 999, 999, 999, 999, 999, 0, 999, 1, 999, 1, 2, 999],
          [999, 999, 999, 999, 999, 999, 999, 0, 999, 2, 1, 2, 999],
          [999, 999, 999, 999, 999, 999, 999, 999, 0, 999, 999, 999, 6],
          [999, 999, 999, 999, 999, 999, 999, 999, 999, 0, 999, 999, 3],
          [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0, 999, 3],
          [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0, 2],
          [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0]]
my_matrix.set_matrix(matrix)
print("<html><head><link rel='stylesheet' href='./style.css'></head><body>")
print("<img src='./graph.png'/>")
for i in range(0, 14):
    print("<p>Matrix D<sup>{0}</sup>: </p>".format(i))
    my_matrix.display()
    if i != 0:
        print("<p>Path matrix for D<sup>{0}</sup>: ".format(i))
        my_matrix.display_path()
    my_matrix.next()

print("</body></html>")
