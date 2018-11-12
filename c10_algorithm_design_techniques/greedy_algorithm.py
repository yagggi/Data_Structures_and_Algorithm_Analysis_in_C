import sys
sys.path.append("..")
from c06_priority_queue.binary_heap import MinHeap


class HuffmanTree:
    def __init__(self, val, frequency, left=None, right=None):
        self.val = val
        self.freq = frequency
        self.left = left
        self.right = right


class Huffman:
    def __init__(self, chrs):
        self.chrs = chrs
        self.freq_dic = {}
        for chr in self.chrs:
            if not self.freq_dic.get(chr):
                self.freq_dic[chr] = 1
            else:
                self.freq_dic[chr] += 1
        self.nodes = MinHeap(len(self.freq_dic))
        for chr, freq in self.freq_dic.items():
            self.nodes.insert(freq, HuffmanTree(chr, freq))
        self.root = self.compression()
        self.code_dic = {}
        self.__init_code_dic(self.root)

    def min_2(self):
        e1 = self.nodes.delete_min()['ele']
        e2 = self.nodes.delete_min()['ele']
        return e1, e2

    def compression(self):
        while self.nodes.size > 1:
            e1, e2 = self.min_2()
            new_node = HuffmanTree(None, e1.freq + e2.freq, e1, e2)
            self.nodes.insert(new_node.freq, new_node)
        return self.nodes.delete_min()['ele']

    def __init_code_dic(self, node=None, pre=''):
        if not node:
            return
        if node.val:
            self.code_dic[node.val] = pre
        if node.left:
            self.__init_code_dic(node.left, pre + '0')
        if node.right:
            self.__init_code_dic(node.right, pre + '1')


if __name__ == '__main__':
    s = 'sdfasdfsdfffffdsdsdf'
    h = Huffman(s)
    print(h.code_dic, h.freq_dic)
