class RemoveDuplicatesFromSortedArray:
    @staticmethod
    def remove_duplicates(nums: list[int]) -> int:
        result = {}
        dup_index = []

        for index in range(len(nums)):
            if nums[index] in result.keys():
                dup_index.append(index)
            else:
                result[nums[index]] = nums[index]

        for index in dup_index[::-1]:
            nums.remove(nums[index])

        return len(nums)
