# 例3：一到面试题：
# list1=[7, -8, 5, 4, 0, -2, -5]
# #要求1.正数在前负数在后 2.整数从小到大 3.负数从大到小
# sorted(list1,key=lambda x:(x<0,abs(x)))
# 解题思路：先按照正负排先后，再按照大小排先后。
[0, 4, 5, 7, -2, -5, -8]