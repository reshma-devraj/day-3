# 4) Next Greater Element to the Right
def next_greater_elements(arr):
    stack = []
    res = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res
