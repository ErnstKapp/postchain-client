from Crypto.Hash import SHA256


class MerkleTreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.hashValue = SHA256.new(bytes(value, encoding = 'utf8'))
        self.hashValue.digest()

def buildTree(leaves,f):
    nodes = []
    for i in leaves:
        nodes.append(MerkleTreeNode(i))

    while len(nodes)!=1:
        temp = []
        for i in range(0,len(nodes),2):
            node1 = nodes[i]
            if i+1 < len(nodes):
                node2 = nodes[i+1]
            else:
                temp.append(nodes[i])
                break
            toPrint1 = node1.hashValue.hexdigest()
            toPrint2 = node2.hashValue.hexdigest()
            f.write("Left child : "+ node1.value + " | Hash : " + toPrint1 +" \n")
            f.write("Right child : "+ node2.value + " | Hash : " + toPrint2 +" \n")
            concatenatedHash = toPrint1 + toPrint2
            parent = MerkleTreeNode(concatenatedHash)
            parent.left = node1
            parent.right = node2
            toPrintParent = parent.hashValue.hexdigest()
            f.write("Parent(concatenation of "+ node1.value + " and " + node2.value + ") : " +parent.value + " | Hash : " + toPrintParent +" \n")
            temp.append(parent)
        nodes = temp
    return nodes[0]
