import numpy

class Matrix(object):
    def __init__(self, matrix_string):
        self.stripped_matrix = matrix_string.strip().split("\n")
        self.matrix = []
        for row_num in range(len(self.stripped_matrix)):
            self.matrix.append(self.stripped_matrix[row_num].split(" "))            

    def row(self, index):
        row = self.matrix[index-1]
        int_row = []
        for num in row:
            int_row.append(int(num))
        return int_row

    def column(self, index):
        column = [] 
        for row in self.matrix:
            column.append(row[index-1])
        int_column = []
        for num in column:
            int_column.append(int(num))
        return int_column