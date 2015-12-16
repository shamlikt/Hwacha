# App controller layer
from socialMediaControl import socialMediaControl

class appController(object): # concrete class

    def getSmName(self,raw_input):
        try:
            smName = raw_input()
            return smName
        except:
            return "Failed"

    def getSmUserName(self,raw_input):
        try:
            smUserName = raw_input()
            return smUserName
        except:
            return "Failed"

    def getSmUserPasswd(self,raw_input):
         try:
            smPwd = raw_input()
            return smPwd
         except:
            return "Failed"

    def getMessage(self,raw_input):
        try:
            smMsg = raw_input()
            return smMsg
        except:
            return "Failed"
    def getAddList(self, raw_input):
        addlist = []
        try:
           addList = addList.append(raw_input())
            return addList
        except:
            return "Failed"
    def getRmList(self, raw_input):
        rmList = []
        try:
            rmList = rmList.append(raw_input())
            return rmList
        except:
            return "failed"
            

    def getSmList(self,raw_input):
         try:
            smList= raw_input()
            return smList
         except:
            return "Failed"

    def isInSmList(self,raw_input):
        try:
            smName = raw_input()
            smObject = socialMediaControl.socialMediaController()
            boolValue = smObject.isSmAvailable(smName)
            if boolValue == True:
                return True
            else:
                return False
        except Exception as excpt:
            return False

            
