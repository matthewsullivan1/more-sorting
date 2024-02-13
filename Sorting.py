  from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")


    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)  # Partitioning index
            self.quicksort(low, pi-1)  # Recursively sort elements before partition
            self.quicksort(pi+1, high)  # Recursively sort elements after partition

    def partition(self, low, high):
        """
        Implements in-place partitioning around a pivot.
        Elements less than the pivot are moved to its left, and greater to its right.
        The pivot is chosen using the median_of_three method.
        It is crucial to rearrange the elements within the array itself,
        avoiding the use of additional arrays or significant extra space.
        low : Starting index, high : Ending index
        Returns the partitioning index.
        """

        #index and data stored at the pivot 
        index = self.median_of_three(low, high)
        part_index = low
        data = self.arr[index]
        
        temp = self.arr[index]
        self.arr[index] = self.arr[high]
        self.arr[high] = temp
        
        for i in range(low, high):
            if self.arr[i] < data:
                self.arr[i], self.arr[part_index] = self.arr[part_index], self.arr[i]
                part_index += 1
        
        self.arr[part_index], self.arr[high] = self.arr[high], self.arr[part_index]
        
        return part_index

    def median_of_three(self, low, high):
        """
        Selects the median of the first, middle, and last elements as the pivot.
        This method is used to improve performance by avoiding worst-case scenarios.
        low : Starting index, high : Ending index
        Returns the index of the median element.
        """
        middle = (low + high) // 2

        if self.arr[low] < self.arr[middle]:
            if self.arr[middle] < self.arr[high]:
                return middle
            
            elif self.arr[low] < self.arr[high]:
                return high
            
            else:
                return low
        else:
            if self.arr[low] < self.arr[high]:
                return low
            
            elif self.arr[middle] < self.arr[high]:
                return high
            
            else:
                return middle
        
def counting_sort(arr, exp):

    result = [0] * len(arr)
    count = [0] * 10

    # Count occurrences of each digit.
    for i in range(len(arr)):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # Update count to store the position of the next occurrence
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array.
    i = len(arr) - 1
    while i >= 0:
        digit = (arr[i] // exp) % 10
        result[count[digit] - 1] = arr[i]

        count[digit] -= 1
        i -= 1

    # Copy the output array to arr[] to update the original array
    for i in range(len(arr)):
        arr[i] = result[i]


def radix_sort(arr):
    # Return if array is empty.
    if len(arr) == 0:
        return True
      
    # Find the maximum number to know the number of digits.
    max_num = max(arr)

    # Do counting sort for every digit.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


if __name__ == '__main__':

    # Test quick sorting technique
    def is_sorted(arr):
        if arr == sorted(arr):
            return "Passed!"
        else:
            return "Failed!"

    def test_quicksort():
        """Test the Quicksort algorithm"""
        seed_num = 43   
        seed(seed_num)  # Set the seed for reproducibility
        sorting = Sorting(10)
        for _ in range(10):
            sorting.add(randint(1, 100))

        sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
        print("Quick Sort:", is_sorted(sorting.arr))

    # Test case execution
    test_quicksort()

    # Test radix sorting technique
    def test_radix_sort():
        # Test case 1
        arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
        radix_sort(arr1)
        assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

        # Test case 2
        arr2 = [329, 457, 657, 839, 436, 720, 355]
        radix_sort(arr2)
        assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

        # Test case 3
        arr3 = [1, 200, 3, 400, 5]
        radix_sort(arr3)
        assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

        # Test case 4 (empty array)
        arr4 = []
        radix_sort(arr4)
        assert arr4 == [], f"Test case 4 failed: {arr4}"

        # Test case 5 (array with one element)
        arr5 = [42]
        radix_sort(arr5)
        assert arr5 == [42], f"Test case 5 failed: {arr5}"

        print("All test cases passed!")

    # Run the test cases
    test_radix_sort()
