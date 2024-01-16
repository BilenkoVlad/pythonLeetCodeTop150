import pytest

from easy_level.remove_element import RemoveElement


class TestRemoveElement:
    @pytest.mark.parametrize("nums,val,output", [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
    ])
    def test_remove_element(self, nums, val, output):
        assert RemoveElement.remove_element(nums=nums, val=val) == output
