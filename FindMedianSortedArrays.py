class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array1, array2 = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(array1) > len(array2):
            array1, array2 = array2, array1
        
        start, end = 0, len(array1) - 1
        while True:
            i = (start + end) // 2
            j = half - i - 2

            arr1left = array1[i] if i >= 0 else float("-infinity")
            arr1right = array1[i + 1] if (i + 1) < len(array1) else float("infinity")
            arr2left = array2[j] if j >= 0 else float("-infinity")
            arr2right = array2[j + 1] if (j + 1) < len(array2) else float("infinity")

            if arr1left <= arr2right and arr2left <= arr1right:
                if total % 2:
                    return min(arr1right, arr2right)
                else:
                    return (max(arr1left, arr2left) + min(arr1right, arr2right)) / 2
            elif arr1left > arr2right:
                end = i - 1
            else:
                start = i + 1
