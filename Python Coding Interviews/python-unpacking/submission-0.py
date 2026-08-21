from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    # return sum(triplet)
    value_1, value_2, value_3 = triplet
    # value_1, value_2, value_3 = triplet[0], triplet[1], triplet[2]
    val = 0
    #   I would personally do a for loop
    for num in triplet:
        val += num # triplet.get("num")
    if val != 0:
        return val
    # if val is not None:

    
    return value_1 + value_2 + value_3

    


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    value_1, value_2, value_3 = box_dimensions
    # value_1, value_2, value_3 = triplet[0], triplet[1], triplet[2]
    val = 0
    #   I would personally do a for loop
    for num in box_dimensions:
        val = val * num # triplet.get("num")
    if val != 0:
        return val
    # if val is not None:

    
    return value_1 * value_2 * value_3  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
