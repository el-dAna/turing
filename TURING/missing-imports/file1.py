import numpy as np
from scipy import stats

def process_strings_and_array(List):
    # Check if the input list has exactly 5 strings
    assert isinstance(List, list), "Input must be a list"
    assert len(List) >= 5, "List must contain at least 5 elements"
    assert all(isinstance(x, str) for x in List[:-1]), "All elements except the last must be strings"
    assert isinstance(List[-1], np.ndarray), "The last element must be a numpy array"
    assert all(isinstance(x, np.int64) and x != 0 for x in List[-1]), "Array elements must be non-zero integers of type np.int64"
    assert sum(List[-1]) == 50, "Sum of array elements must be 50"
    assert np.mean(List[-1]) > 45, "Average of array elements must be greater than 45"
    try:
        assert stats.mode(List[-1])[0][0] == 23, "Mode of array elements must be 23"
    except IndexError:
        print("IndexError: The array does not have a mode. Perhaps it has multiple modes or is empty.")
    assert all(len(x) <= 5 for x in List[:-1]), "Length of each string must be at most 5"

    # Turn 3
    assert all(any(c in 'aeiou' for c in s) for s in string_list), "All string elements must have at least one vowel"
    assert all(s.islower() for s in string_list), "All string elements must be lower case"
    assert List[-1].ndim == 1, "The array element must be one-dimensional"
    assert len(np.unique(List[-1])) == len(List[-1]), "Array elements must be unique"
    assert len(List[-1]) <= len(string_list[0]), "The last string element should not be longer than the first string element"
    assert all(s.isalpha() for s in string_list), "All string elements must contain only alphabetical characters"
    assert all(50 >= x >= 30 for x in List[-1]), "Array elements must be positive numbers between 50 and 30"
    assert len(List[-1]) == len(string_list), "Length of the array element must be equal to the number of string elements"

    string_list = List[0:-1]
    array_element = List[-1]
    
    concatenated_string = ''.join(string_list)
    print(f"Concatenated String: {concatenated_string}")

    character_counts = [len(s) for s in string_list]
    print(f"Character Counts: {character_counts}")

    reversed_strings = [s[::-1] for s in string_list]
    print(f"Reversed Strings: {reversed_strings}")

    longest_string = max(string_list, key=len)
    print(f"Longest String: {longest_string}")
    
    max_value = max(List[-1])
    min_value = min(List[-1])
    print(f"Maximum Value in Array: {max_value}")
    print(f"Minimum Value in Array: {min_value}")

def main():
    # Example inputs
    List = ["apple", "banana", "cherry", "date", "elderberry", np.array([10, 20, 30, 40, 50, 60])

    process_strings_and_array(List)

if __name__ == "__main__":
    main()