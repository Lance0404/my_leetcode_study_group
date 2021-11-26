def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    """
    large pkg: 5
    small pkg: 1
    """
    min_num = 0
    while items:
        # print(items, available_large_packages, available_small_packages)
        if items > 5 and not available_large_packages and available_small_packages < 5:
            break
        if items > 0 and (not available_small_packages):
            break

        if items > 5 and available_large_packages:
            items -= 5
            available_large_packages -= 1
            min_num += 1
        elif items > 0 and available_small_packages:
            items -= 1
            available_small_packages -= 1
            min_num += 1

    if items:
        return -1
    else:
        return min_num

    
print(minimal_number_of_packages(16, 2, 10))
# 8 (2 l, 6 s)