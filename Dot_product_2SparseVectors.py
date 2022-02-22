###https://blog.csdn.net/Xiao_Spring/article/details/112974910

class SparseVector:
    def __init__(self, nums:List[int]):
        self.num = {i:x for i,x in enumerate(nums) if x!=0}

    def dotProduct(self, vec:'SparseVector')->int:
        return sum([x*vec.num[i] if i in vec.num else 0 for i, x in self.num.items())
