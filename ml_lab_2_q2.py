def matrix_multiply(A, B):
    # Check if matrices are multipliable
    if len(A[0]) != len(B):
        return "Error: Matrices are not multipliable"
    
    # Initialize result matrix with appropriate dimensions
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def main():
    # Input matrices A and B
    A = [[1, 2, 3],
         [4, 5, 6]]
    
    B = [[7, 8],
         [9, 10],
         [11, 12]]

    # Multiply matrices and print result
    result = matrix_multiply(A, B)
    print("Product AB:")
    if isinstance(result, str):
        print(result)
    else:
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
