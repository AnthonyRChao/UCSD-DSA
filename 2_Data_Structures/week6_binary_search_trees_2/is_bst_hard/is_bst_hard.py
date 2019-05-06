#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(i, mn, mx):
  if not i in tree:
      return True
  if tree[i][0] < mn or tree[i][0] > mx:
      return False
  return IsBinarySearchTree(tree[i][1], mn, tree[i][0] - 1)  and IsBinarySearchTree(tree[i][2], tree[i][0], mx)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree = {}
  int_max = sys.maxsize
  int_min = - sys.maxsize - 1
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target = main).start()
