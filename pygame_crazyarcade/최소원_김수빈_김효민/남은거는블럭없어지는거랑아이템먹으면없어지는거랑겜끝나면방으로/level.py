class Level:
    def __init__(self):
        self.relevel1=''

    def updateFile(self,up):
        f = open('1plevel.txt','r')
        file = f.readlines()
        last = int(file[0])
        if  1<= last:
            last += up
            f.close()
            file = open('1plevel.txt','w')
            file.write(str(last))
            file.close()
            return last
        return last

class Level2:
    def __init__(self):
        self.relevel2 = ''

    def updateFile(self,up):
        f = open('2plevel.txt','r')
        file = f.readlines()
        last = int(file[0])
        if  1<= last:
            last += up
            f.close()
            file = open('2plevel.txt','w')
            file.write(str(last))
            file.close()
            return last
        return last
