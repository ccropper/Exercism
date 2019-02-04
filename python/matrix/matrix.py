import numpy

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        for row in matrix_string.strip().split("\n"):
            self.matrix.append(row.split(" "))
        self.matrix = [[int(num) for num in row] for row in self.matrix]
      
    def row(self, index):
        return [num for num in self.matrix[index-1]]

    def column(self, index):
        return [row[index-1] for row in self.matrix]