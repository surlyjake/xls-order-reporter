class ReportGenerator:
    def __init__(self,xlsFile):
        self.xlsFile = xlsFile
    def report1(self):
        print "report1"
        print self.xlsFile.enumFields()

