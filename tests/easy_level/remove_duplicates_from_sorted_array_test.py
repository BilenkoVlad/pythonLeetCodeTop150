import pytest

from easy_level.remove_duplicates_from_sorted_array import RemoveDuplicatesFromSortedArray


class TestRemoveDuplicatesFromSortedArray:
    @pytest.mark.parametrize("nums,output", [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    ])
    def test_remove_duplicates(self, nums, output):
        assert RemoveDuplicatesFromSortedArray.remove_duplicates(nums=nums) == output
