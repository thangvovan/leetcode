class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        print(ax1 >= bx2, ay1 >= by2, ax2 <= bx1, ay2 <= by1)
        if ax1 >= bx2 or ay1 >= by2 or ax2 <= by1 or ay2 <= by1:
            return ((ax2 - ax1) * (ay2 - ay1)) + ((bx2 - bx1) * (by2 - by1))
        else:
            cx1 = ax1 if ax1 >= bx1 else bx1
            cy1 = ay1 if ay1 >= by1 else by1
            cx2 = ax2 if ax2 <= bx2 else bx2
            cy2 = ay2 if ay2 <= by2 else by2
        return (((ax2 - ax1) * (ay2 - ay1)) + ((bx2 - bx1) * (by2 - by1)) - ((cx2 - cx1) * (cy2 - cy1)))