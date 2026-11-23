class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)  
        # Array ki total length calculate kar rahe hain.

        answer = [1] * n
        # Ek new array bana rahe hain jisme n positions hongi.
        # Initially har position par 1 store hai.
        # Example: nums = [1,2,3,4]
        # answer = [1,1,1,1]

        # STEP 1: PREFIX PRODUCT

        prefix = 1
        # Prefix product ko 1 se initialize kiya.
        # 1 isliye kyunki multiplication mein 1 neutral value hai.

        for i in range(n):
            # Array ke har index par iterate kar rahe hain.
            # i = 0, 1, 2, 3

            answer[i] = prefix
            # Current index ke LEFT side ke elements ka product
            # answer[i] mein store kar rahe hain.
            # Current element ko abhi multiply nahi karna hai.

            prefix *= nums[i]
            # Current element ko prefix mein multiply kar rahe hain.
            # Ye next index ke liye prefix product ready karega.

        # STEP 2: SUFFIX PRODUCT

        suffix = 1
        # Suffix product ko 1 se initialize kiya.
        # Right side mein initially koi element nahi hai.

        for i in range(n - 1, -1, -1):
            # Array ko RIGHT TO LEFT traverse kar rahe hain.
            # Example: n = 4
            # i = 3, 2, 1, 0

            answer[i] *= suffix
            # Answer mein already prefix product stored hai.
            # Ab usko current index ke RIGHT side ke
            # suffix product se multiply kar rahe hain.
            # Isse current element ke alawa sabka product mil jayega.

            suffix *= nums[i]
            # Current element ko suffix mein multiply kar rahe hain.
            # Ye next left index ke liye suffix product ready karega.

        return answer
        # Final answer array return kar rahe hain.