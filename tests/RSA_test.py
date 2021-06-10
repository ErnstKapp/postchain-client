import sys
sys.path.append("../src")
from PostChainUtil import PostChainUtil

""" Testing of RSA keypairs """
keys = PostChainUtil.MakeKeyPair()
testMessage = "message to be hashed"
testHash = PostChainUtil.Sha256Hash(testMessage)
sig = PostChainUtil.Sign(testHash ,keys[0]) #PKCS1_v1_5.new(keys[0])
verified = PostChainUtil.VerifyMessage(testHash, keys[1], sig)
assert verified, 'Signature verification failed'
print('Succesfully verified message')
