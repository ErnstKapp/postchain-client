from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

""" Util functions for postchain client """

class PostChainUtil:


    def Sha256Hash(buffer):
        buffer = bytes(buffer, encoding = 'utf8')
        newHash = SHA256.new()
        newHash.update(buffer)
        newHash.digest()
        return newHash

    def Sign(hashedMessage, privKey):

        #if(len(privKey.n) != 32):
        #     raise Exception("privKey invalid length")

        return PKCS1_v1_5.new(privKey).sign(hashedMessage)

    def MakeKeyPair():
        newKey = RSA.generate(1024)
        return (newKey, newKey.publickey())

    def VerifyKeyPair(privKey):
        return privKey.publickey()

    def VerifyMessage(message, pubKey, signature):
        verifier = PKCS1_v1_5.new(pubKey)
        verified = verifier.verify(message, signature)
        return verified
