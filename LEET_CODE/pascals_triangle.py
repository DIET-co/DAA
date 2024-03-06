def print_pascals_triangle(height):
    coefficients = [1]
    for row_num in range(height):
        row = " ".join(map(str, coefficients))
        print(row.center(len(row) + 2 * row_num))

        # Compute next row
        previous = coefficients[:]
        for k in range(row_num):
            coefficients[k + 1] = previous[k] + previous[k + 1]
        coefficients.append(1)

# Get input from user
height = int(input("Enter the height of the Pascal's triangle: "))
print_pascals_triangle(height)

##time complexity O(N^2).
##space complexity O(N^2).