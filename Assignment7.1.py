print("Hello Darkness my old Friend :))")
def multiplication_table(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            result = i * j
            print(f"{i} x {j} = {result}\t", end="")
        print()  # Move to the next line after printing a row

# Get input from the user
rows = int(input("Enter the number of rows (n): "))
columns = int(input("Enter the number of columns (m): "))
multiplication_table(rows, columns)
