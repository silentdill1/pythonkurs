from random import randint
import numpy as np


class Matrix(object):

    def rand(self):
        matrix = self.matrix
        if self.columns == 0:
            for variable_index in range(matrix.shape[0]):
                matrix[variable_index] = randint(0, 100) / 100
        else:
            for row_index in range(matrix.shape[0]):
                for column_index in range(matrix.shape[1]):
                    matrix[row_index][column_index] = randint(0, 100) / 100

    def __init__(self, rows, columns=0):
        self.rows = rows
        self.columns = columns
        if columns != 0:
            self.matrix = np.empty((rows, columns))
        else:
            self.matrix = np.empty(rows)
        self.rand()

    def identity(self):
        matrix = self.matrix
        if matrix.shape[0] != matrix.shape[1]:
            raise Exception('Matrix has to be a square matrix.')
        else:
            for diag_index in range(matrix.shape[0]):
                matrix[diag_index][diag_index] = 1

    @staticmethod
    def __dot_product(matrix1, matrix2):
        dot_product = 0
        for vector_index in range(matrix1.shape[0]):
            dot_product += matrix1[vector_index] * matrix2[vector_index]
        return dot_product

    @staticmethod
    def transpose(matrix):
        t_matrix = np.empty((matrix.shape[1], matrix.shape[0]))
        for i in range(t_matrix.shape[0]):
            for j in range(t_matrix.shape[1]):
                t_matrix[i][j] = matrix[j][i]
        return t_matrix

    def __add__(self, matrix):
        matrix1 = self.matrix
        matrix2 = matrix.matrix
        if matrix1.shape != matrix2.shape:
            raise Exception('Matrices need to have same dimensions.')
        else:
            r_matrix_object = Matrix(matrix1.shape[0], matrix1.shape[1])
            r_matrix = np.empty(matrix1.shape)
            for row_index in range(matrix1.shape[0]):
                for column_index in range(matrix1.shape[1]):
                    r_matrix[row_index][column_index] = matrix1[row_index][column_index] + \
                                                        matrix2[row_index][column_index]
            r_matrix_object.matrix = r_matrix
            return r_matrix_object

    def __mul__(self, matrix):
        matrix1 = self.matrix
        matrix2 = matrix.matrix
        if (len(matrix1.shape) == 1) and (len(matrix2.shape) == 1) and (matrix1.shape == matrix2.shape):
            dot_product = Matrix.__dot_product(matrix1, matrix2)
            return dot_product
        elif matrix1.shape[1] != matrix2.shape[0]:
            raise Exception('Matrices cannot be multiplied, wrong dimensions')
        else:
            r_matrix_object = Matrix(matrix1.shape[0], matrix2.shape[1])
            r_matrix = np.empty((matrix1.shape[0], matrix2.shape[1]))
            for i in range(r_matrix.shape[0]):
                for j in range(r_matrix.shape[1]):
                    r_matrix[i][j] = Matrix.__dot_product(matrix1[i], Matrix.transpose(matrix2)[j])
            r_matrix_object.matrix = r_matrix
            return r_matrix_object

    def __sub__(self, matrix):
        matrix1 = self.matrix
        matrix2 = matrix.matrix
        if matrix1.shape != matrix2.shape:
            raise Exception('Matrix need to have same dimensions.')
        else:
            r_matrix_object = Matrix(matrix1.shape[0], matrix1.shape[1])
            r_matrix = np.empty(matrix1.shape)
            for row_index in range(matrix1.shape[0]):
                for column_index in range(matrix1.shape[1]):
                    r_matrix[row_index][column_index] = matrix1[row_index][column_index] - \
                                                        matrix2[row_index][column_index]
            r_matrix_object.matrix = r_matrix
            return r_matrix_object

    def __str__(self):
        matrix = self.matrix
        string = ''
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                string += (str(matrix[i][j]) + '\t')
            string += '\n'
        return string


if __name__ == "__main__":
    m = Matrix(2, 3)
    print(m.__str__())

