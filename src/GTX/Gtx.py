
class Gtx:

    def __init__(self, BlockchainRID):
        self.BlockchainID = BlockchainRID
        self.Operations = []
        self.Signers = []
        self.Signatures = []

    def AddOperationToGtx(self, opName, *args):

        if(len(self.Signatures) != 0):
            raise Exception('gtx already signed')
        opArr = []
        opArr.append(opName)
        for arg in args:
            opArr.append(arg)

        self.Operations.append(opArr)
        return self

    def AddSignerToGtx(self, signer):

        if(self.Signers.len() != 0):
            raise Exception('gtx already signed')

        self.Signers.add(signer)

    def Sign(self, privKey, pubKey):
        bufferToSign = self.GetBufferToSign

    def GetBufferToSign(self):
        oldSignatures = self.Signatures
        self.Signatures.clear()

        #encodedBuffer = Gtv.Hash(GetGtvTxBody(true))
        self.Signatures = oldSignatures

        return encodedBuffer
