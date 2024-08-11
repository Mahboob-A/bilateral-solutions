# 110824, Sunday, 05.30 pm 

class FindUniqueElementsInList:
    """Find Unique Elements in a given list."""

    def count_unique_elements_in_list_naive(self, duplicate_elem_list: list) -> int:
        """Naive approach to find unique elements from a list.

        @param: duplicate_elem_list - a list with duplicate elements.

        Time Complexity: O(n^2)

        Space Complexity: O(n)
        """

        if not duplicate_elem_list:
            return 0

        checked_elements = []

        for val in duplicate_elem_list:
            is_unique = True

            for checked_vals in checked_elements:
                if val == checked_vals:
                    is_unique = False
                    break

            if is_unique:
                checked_elements.append(val)

        print("checked elements: ", checked_elements)
        return len(checked_elements)

    def count_unique_elements_in_list_naive_2(self, duplicate_elem_list: list) -> int:
        """Second Naive approach to find unique elements from a list.

        @param: duplicate_elem_list - a list with duplicate elements.

        Time Complexity: O(n^2)

        Space Complexity: O(1)
        """

        if not duplicate_elem_list:
            return 0

        unique_values = 0

        lst_size = len(duplicate_elem_list)
        for i in range(lst_size):
            #     print("i: ", i)
            is_unique = True

            for j in range(i):
                # print("j: ", j)
                if duplicate_elem_list[i] == duplicate_elem_list[j]:
                    is_unique = False
                    break
            #     print()
            if is_unique:
                unique_values += 1

        return unique_values

    def count_unique_elements_in_list_optimized(self, duplicate_elem_list: list) -> int:
        """Optimized approach to find duplicate elements in a list.

        This is efficient approach as lookup complexity in dict has O(1) time complexity
        and the overall algorithm has O(n) time complexity.

        @param: duplicate_elem_list - a list with duplicate elements.

        Time Complexity: O(n)

        Space Complexity: O(n)
        """
        if not duplicate_elem_list:
            return 0

        ans_dict = {}

        for val in duplicate_elem_list:
            ans_dict[val] = None

        return len(ans_dict)


inp_lst = ["a", "a", "b", "c", "b", "z", 1, 1, 2, 1, 3, 2, 1, 3, 1, "a", "k", False, 'python', 'cpp', False, 'python', 'c', 'rust', 'go', 'rust', 'python']  # 27 
# inp_lst = []


unique_element_finder = FindUniqueElementsInList()

def main(inp_lst: list):

    total_unique_elements = unique_element_finder.count_unique_elements_in_list_optimized(
        duplicate_elem_list=inp_lst
    )

    print("\nTotal Unique Elements in the List are: ", total_unique_elements, "\n")


if __name__ == "__main__":

    main(inp_lst=inp_lst)
