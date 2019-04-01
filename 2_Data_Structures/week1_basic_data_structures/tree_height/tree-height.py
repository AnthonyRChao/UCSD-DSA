# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

        def read(self):
            self.n = int(sys.stdin.readline())
            self.relationships = list(map(int, sys.stdin.readline().split()))

        def build_tree(self):
            self.nodes = {}
            for child, parent in enumerate(self.relationships):
                if parent == -1:
                    self.root = child
                if parent not in self.nodes:
                    self.nodes[parent] = [child]
                else:
                    self.nodes[parent].append(child)

        def compute_height_bfs(self):
            q = []

            q.append([self.root, 1])
            maxHeight = 1

            while q:
                parent, height = q.pop()
                if parent in self.nodes:
                    height += 1
                    if height > maxHeight:
                        maxHeight = height
                    for child in self.nodes[parent]:
                        q.append([child, height])
            return maxHeight


def main():
  tree = TreeHeight()
  tree.read()
  tree.build_tree()
  print(tree.compute_height_bfs())

threading.Thread(target=main).start()
