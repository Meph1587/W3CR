from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from writer import writer
from reader import reader
import hashlib
import json
import time
import sys
from datetime import datetime
from W3CR import W3CR


pkey = None
addr = None 
web3 = Web3(HTTPProvider('---LINK---'))

#initiate lib
CR = W3CR(addr,pkey,web3,None)


#make 2 commit-reveal
cmm = {
    "Data" : "Something",
}

CR.Commit(cmm)

time.sleep(40)

CR.Reveal()

time.sleep(20)


cmm = {
    "Data" : "SomethingElse",
}

CR.Commit(cmm)

time.sleep(40)

CR.Reveal()

time.sleep(60)

count = 0


#read 
while True:

    if count < -50:
        break;

    else:
        res = CR.CheckAndGetData(count) 

        if res == None:
            break;

        else:
            print (res) 
            count = count-4









