from PostChainUtil import PostChainUtil

class Transaction:

    def __init__(self, gtx, restClient):
        self.gtx = gtx
        self.restClient = restClient

    def addOperation(name, *args):
        gtx.AddOperationToGtx(name, *args)

    def Sign(privKey, pubKey):

        if(pubKey == None):
            pubKey = PostChainUtil.getPublicKey(privKey)

        self.gtx.Sign(privKey, pubKey)

    def GetTxRID():
        return(GetBufferToSign().decode('utf8'))

    def GetBufferToSign():
        return self.gtx.GetBufferToSignGTX();

    def AddSignature(pubKey, signature):
        self.gtx.AddSignature(pubKey, signature)

    
