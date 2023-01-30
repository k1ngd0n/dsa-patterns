def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    current_idx = 2
    while current_idx < len(arr):
        last_unique = next_non_duplicate - 1
        if arr[last_unique] != arr[current_idx]:
            arr[next_non_duplicate] = arr[current_idx]
            next_non_duplicate += 1
        current_idx += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
