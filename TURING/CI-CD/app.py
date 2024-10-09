def manipulate_lists_and_strings(
    list_a, list_b, string_a, string_b, string_c
):
    # Uniform slicing standard: start : stop : step
    # if start and step are the begining and end of list,
    # then the slicing standard adopted is: :: step

    # List slicing operations
    sliced_list_a = list_a[
        1:4
    ]  # Get elements from index 1 to 3
    reversed_list_b = list_b[
        ::-1
    ]  # Reverse the list

    # String slicing operations
    sliced_string_a = string_a[
        1:5
    ]  # Get substring from index 1 to 4
    sliced_string_b = string_b[
        :6
    ]  # Get first 6 characters of the string
    sliced_string_c = string_c[
        -7:
    ]  # Get last 7 characters of the string

    # Merging lists with '+' operator
    merged_lists = list_a + list_b

    # Appending list_b to list_a
    list_a += list_b

    # Combine the slices
    combined_list = (
        sliced_list_a + reversed_list_b
    )
    combined_string = (
        sliced_string_a
        + sliced_string_b
        + sliced_string_c
    )

    # Return the results in a dictionary for clarity
    return {
        "sliced_list_a": sliced_list_a,
        "reversed_list_b": reversed_list_b,
        "sliced_string_a": sliced_string_a,
        "sliced_string_b": sliced_string_b,
        "sliced_string_c": sliced_string_c,
        "merged_lists": merged_lists,
        "list_a": list_a,  # list_a has been modified by appending list_b
        "combined_list": combined_list,
        "combined_string": combined_string,
    }


# Example usage
list_a = [0, 1, 2, 3, 4, 5, 6]
list_b = ["a", "b", "c", "d", "e"]
string_a = "HelloWorld"
string_b = "PythonProgramming"
string_c = "CodeReview"

result = manipulate_lists_and_strings(
    list_a, list_b, string_a, string_b, string_c
)
print(result)
