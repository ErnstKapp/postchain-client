import sys
sys.path.append("../src/GTV/Merkle")
from MerkleTreeNode import MerkleTreeNode, buildTree

""" Test for merkle tree """

inputString = " leaf1, leaf2, leaf3 ,leaf4,leaf5 ,leaf6 leaf7, leaf8, leaf9 "
leavesString = inputString[1:len(inputString)-1]
leaves = leavesString.split(",")
f = open("merkle.tree", "w")
root = buildTree(leaves,f)
f.close()
