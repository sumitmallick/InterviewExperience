def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print("max water contains:")
print(max_area([1,1]))
