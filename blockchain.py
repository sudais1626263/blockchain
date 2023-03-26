import hashlib
def hashgenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()
class block:
    def __init__(self,data,hash,prehash):
        self.data=data
        self.hash=hash
        self.prehash=prehash
class blockchain:
    def __init__(self):
        hashStart=self.starthash=hashgenerator("starthash")
        hashEnd=self.endhash=hashgenerator("endhash")
        
        
        genesys=block('gendata', hashStart,hashEnd)
        self.chain=[genesys]
        
    def addblock(self,data):
        prehash=self.chain[-1].hash
        currenthash=hashgenerator(data+prehash)
        Block=block(data, currenthash, prehash)
        self.chain.append(Block)
        
bc=blockchain()
bc.addblock("1")
bc.addblock("2")

for block in bc.chain:
    print(bc.__dict__)
        
        