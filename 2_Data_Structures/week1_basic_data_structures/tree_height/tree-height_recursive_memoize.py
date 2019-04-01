# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

        def __init__(self):
            self.n = 0
            self.parent = []
            self.memoize = []

        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
            self.memoize = [0] * self.n

        def path_length(self, node_index):
            if self.parent[node_index] == -1:
                return 1

            if self.memoize[node_index]:
                return self.memoize[node_index]

            self.memoize[node_index] = 1 + self.path_length(self.parent[node_index])
            return self.memoize[node_index]

        def compute_height(self):
            return max([self.path_length(i) for i in range(self.n)])


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
