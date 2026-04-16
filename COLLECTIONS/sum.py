from collections import deque
nums = [1,2,3,4,5,6]
window = 3
d = deque(nums[:window])
print(sum(d), end=" ")
for i in range(window, len(nums)):
    d.popleft()
    d.append(nums[i])
    print(sum(d), end=" ")
