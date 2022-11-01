'''
https://stepik.org/lesson/265105/step/13?unit=246053
'''
nums = [int(input()) for _ in range(3)]
print(max(nums),sum(nums)-(min(nums)+max(nums)),min(nums),sep='\n')