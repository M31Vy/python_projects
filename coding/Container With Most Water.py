def water(height):
    left = 0
    right = len(height)-1
    h = min(height[left],height[right])
    ans = h*(right-left)
    while left<right:
        if height[left]<height[right]:
            m=height[left]
            left += 1
        else:
            m=height[right]
            right -= 1
        if m>h:
            h = m
            x = h*(right-left+1)
            if x>ans:
                ans = x
    return ans