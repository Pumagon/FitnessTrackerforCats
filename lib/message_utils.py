import config

class Message:
    def __init__(self, myDisplay):
        self.thisMachineHasDisplay = config.thisMachineHasDisplay
        self.thisMachineHasConsole = config.thisMachineHasConsole
        
        self.myDisplay = myDisplay

    def showLines(self, lines):
        if self.thisMachineHasDisplay == True:
            self.myDisplay.showLines(lines)

        if self.thisMachineHasConsole == True:
            for i in range(len(lines)):
                print(lines[i])
