import os,sys
class SuperFileUtil(object):
    def __init__(self, filePath):
        self.filePath = filePath
        self.isExist = None
        self.isDir = None
        


    def _isDirection(self):
        if(self.isExist == None):
            self.isExist = self._isExist()
            if(self.isExist is False):
                return None
        if(os.path.isdir(self.filePath)):
            isDir = True
            return True
        else:
            isDir = False
            return False

    def _isExist(self):
        if os.path.exists(self.filePath) is True:
            self.isExist = True
            return True
        else:
            self.isExist = False
            return False
        
    def fileList(self):
        if(self.isExist == None):
            if(self._isExist() == False):
                return None
        fileList = []
        if(self.isDir == None):
            if(self._isDirection() == False):
                return [self.filePath]

        for root, dirs, files in os.walk(self.filePath):
            #for dirs in dirs:
            #    print(os.path.join(root, dirs))
            for file in files:
                print(os.path.join(root, file))
        return fileList
        
        

        
sfu = SuperFileUtil("""E:\\testDir""")

#print(sfu._isExist())
print(sfu.fileList())

#sfu.isExist()

"""
t = sfu.isExist()
print(t)
print(sfu.isDirection())
""" 
    
