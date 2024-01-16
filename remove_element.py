class RemoveElement:
    @staticmethod
    def remove_element(nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
