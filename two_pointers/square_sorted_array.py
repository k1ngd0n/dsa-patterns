def square_sorted_array(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highest_square_idx = n - 1
    left, right = 0, n - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1
        highest_square_idx -= 1

    return squares


def main():
    print("Squares: " + str(square_sorted_array([-2, -1, 0, 2, 3])))
    print("Squares: " + str(square_sorted_array([-3, -1, 0, 1, 2])))


main()
