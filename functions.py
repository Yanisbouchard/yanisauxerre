def several_zeros():
    return [0] * 10

if __name__ == '__main__':
    print(several_zeros())  
   
def several_zeros_custom(nb_zeros=10):  
    return [0] * nb_zeros

if __name__ == '__main__':
    print(several_zeros_custom())      
    print(several_zeros_custom(5))     

       
def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

if __name__ == '__main__':
    result = matrix(2, 3)
    print(result)         
    print(result[1][2])   
class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]  
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        return self._matrix[row][col]

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return self._matrix == other._matrix

if __name__ == '__main__':
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1.get_value(1, 2))  
    print(m1 == m2)           


def my_sort(my_list):
    sorted_list = my_list.copy()
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]  
    return sorted_list

if __name__ == '__main__':
    my_list = [4, 2, 7, 1, 3]
    print(my_sort(my_list))  
