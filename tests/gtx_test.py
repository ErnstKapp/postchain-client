import sys
sys.path.append("../src/GTX")
from Gtx import Gtx

""" Test to add operation to gtx """

arg1 = 2
arg2 = 3

transaction = Gtx(1)
transaction.AddOperationToGtx("foo", arg1, arg2)
print(transaction.Operations)
