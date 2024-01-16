class MergeSortedArray:
    @staticmethod
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1.extend(nums2)

        for i in range(len(nums1)):
            for j in range(0, len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]

        if nums1[0] >= 0:
            while 0 in nums1:
                nums1.remove(0)
