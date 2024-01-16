class MajorityElement:
    @staticmethod
    def majority_element(nums: list[int]) -> int:
        result = {}

        for num in nums:
            if num in result.keys():
                result[num] += 1
            else:
                result[num] = 1

        max_value = 1
        return_value = 0
        for key, value in result.items():
            if value >= max_value:
                max_value = value
                return_value = key

        return return_value
