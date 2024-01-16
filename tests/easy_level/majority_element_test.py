import pytest

from easy_level.majority_element import MajorityElement


class TestMajorityElement:
    @pytest.mark.parametrize("nums,output", [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ])
    def test_majority_element(self, nums, output):
        assert MajorityElement.majority_element(nums=nums) == output
