nums = [2,20,25,-10,78,4,0,-29,21]

higher = lower = nums[0]
for n in nums:
    if n > higher:
        higher = n
    if n < lower:
        lower = n

print("Highest number is ", higher)
print("Lowest number is ", lower)