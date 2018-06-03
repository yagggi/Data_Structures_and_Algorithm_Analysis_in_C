

class AVLTree:

    def __init__(self, value=None, right=None, left=None, hight=-1):
        self.value = value
        self.right = right
        self.left = left
        self.hight = hight

    def check_balance(self):
        return