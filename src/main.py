import numpy as np

if __name__ == "__main__"
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
             a.append(int(input()))
        matrix.append(a)


    b = np.array(a)

    print(np.linalg.inv(b))
