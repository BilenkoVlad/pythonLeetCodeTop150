import pytest

from easy_level.merge_sorted_array import MergeSortedArray


class TestMergeSortedArray:
    @pytest.mark.parametrize("nums1,m,nums2,n,output", [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ])
    def test_merge(self, nums1, m, nums2, n, output):
        assert MergeSortedArray.merge(nums1=nums1, m=m, nums2=nums2, n=n) == output
