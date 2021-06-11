

class GTXClient:

    def __init__(self, restAPIClient):
        self.restAPIClient = restAPIClient

    def addNewTransaction(signers):

        newGTX = Gtx(RestAPIClient.BlockchainRID)

        for signer in signers:
            newGTX.AddSignerToGtx(signer)

        
