from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from math import *


NUMBERS = ['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALEGBRA = ['+', '-', '+/-', u"\u00D7", u"\u00F7"]
TRIGONOMETRY = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']
LOGARITHMIC = ['ln', 'log', '10'u"\u207f", 'e'u"\u207f"]
POWERS = ['x'u"\u207f", 'x'u"\u00b2", 'x'u"\u00b3", u"\u221A", u"\u00b3"u"\u221A"]
CONSTANTS = ['e', u"\u03C0"]
COMBINATORICS = ['n!', 'nCr', 'nPr']
CALCFUNCTION = ['DEL', '=', 'C']
MISCELLANEOUS = ['(', ')', '%', 'MOD']



class CalcGridLayout(GridLayout):

    actualExp = ''
    DEG_RAD = False
    justPrint = False
    lastState = []

    def negate(self, calculation):
        if calculation:
            try:
                displayText = str(-1 * eval(calculation))
            except Exception:
                self.display.text = 'Error'
    def calculate(self):
        if self.actualExp:
            try:
                self.actualExp = str(eval(self.actualExp))
            except Exception as e:
                print(e)
        return self.actualExp

    def modes(self, text):
        if text == 'DEG':
            self.DEG_RAD = True
            return 'RAD'
        else:
            self.DEG_RAD = False
            return 'DEG'

    def setExp(self, text):
        pass

    def getVal(self, displayText, text):

        #----Numbers----
        if text in NUMBERS:
            displayText = self.numberOp(text)
       
        #----Combinatorics----
        elif text in COMBINATORICS:
            displayText = self.combinatronicOp(text)
       
        #----Trigonometry----
        elif text in TRIGONOMETRY:
            displayText = self.trigoOp(text)
        
        #----Logarithmic----
        elif text in LOGARITHMIC:
            displayText = self.logOp(text)
        
        #----Powers----
        elif text in POWERS:
            displayText = self.powerOp(text)
        
        #----Algebra----
        elif text in ALEGBRA:
            displayText = self.algebraOp(text)
        
        #----Constants----
        elif text in CONSTANTS:
            displayText = self.constantOp(text)
        
        #----Calculator Functions----
        elif text in CALCFUNCTION:
            displayText = self.calcFunc(text)
        
        #----Miscellaneous----
        elif text in MISCELLANEOUS:
            displayText = self.miscOp(text)
        
        else:
            displayText = self.actualExp = ''
            displayText = text + ' Handle This'
        return displayText
    
    def numberOp(self, text):
        displayText = self.display.text
        self.lastState.append((self.actualExp, self.display.text)) 
        if self.justPrint:
            self.actualExp = ''
            displayText = ''
            self.justPrint = False
        self.actualExp += text
        displayText += text
        return displayText

    def trigoOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == 'sin':
            if self.DEG_RAD:
                self.actualExp = 'sin(' + self.actualExp + ')'
            else:
                self.actualExp = 'sin(radians(' + self.actualExp + '))'
            displayText = 'sin(' + displayText + ')'
        elif text == 'cos':
            if self.DEG_RAD:
                self.actualExp = 'cos(' + self.actualExp + ')'
            else:
                self.actualExp = 'cos(radians(' + self.actualExp + '))'
            displayText = 'cos(' + displayText + ')'
        elif text == 'tan':
            if self.DEG_RAD:
                self.actualExp = 'tan(' + self.actualExp + ')'
            else:
                self.actualExp = 'tan(radians(' + self.actualExp + '))'
            displayText = 'tan(' + displayText + ')'
        return displayText

    def algebraOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == '+/-':
            if self.actualExp[0] == '-':
                self.actualExp = self.actualExp[1:]
                displayText = displayText[1:]
            else:
                self.actualExp = '-' + self.actualExp
                displayText = '-' + displayText
        elif text == '+':
            self.actualExp = self.actualExp + '+'
            displayText += '+'
        elif text == u"\u00F7":
            self.actualExp = self.actualExp + '/'
            displayText += u"\u00F7"
        elif text == u"\u00D7":
            self.actualExp = self.actualExp + '*'
            displayText += u"\u00D7"
        elif text == '-':
            self.actualExp = self.actualExp + '-'
            displayText += '-'
        self.lastSate = text 
        return displayText

    def logOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == 'ln':
            self.actualExp = 'log(' + self.actualExp + ')'
            displayText = 'ln(' + displayText + ')'
        elif text == 'log':
            self.actualExp = 'log10(' + self.actualExp + ')'
            displayText = 'log(' + displayText + ')'
        elif text == '10'u"\u207f":
            self.actualExp = 'pow(10, ' + self.actualExp + ')'
            displayText = '10^' + displayText
        elif text == 'e'u"\u207f":
            self.actualExp = 'pow(e, ' + self.actualExp + ')'
            displayText = 'e^' + displayText
        return displayText

    def powerOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == 'x'u"\u207f":
            self.actualExp = self.actualExp + '**'
            displayText += '^'
        elif text == 'x'u"\u00b2":
            self.actualExp = 'pow(' + displayText + ', 2)'
            displayText += u"\u00b2"
        elif text == 'x'u'\u00b3':
            self.actualExp = 'pow(' + displayText + ', 3)'
            displayText += u'\u00b3'
        elif text == u"\u221A":
            self.actualExp = 'sqrt(' + self.actualExp + ')'
            displayText = u"\u221A" + displayText
        elif text == u"\u00b3"u"\u221A":
            self.actualExp = 'pow(' + self.actualExp + ', 1/3)'
            displayText = u"\u00b3"u"\u221A" + displayText
        return displayText

    def calcFunc(self, text):
        self.justPrint = False
        displayText = self.display.text
        print(self.actualExp, displayText)
        if text == 'C':
            self.actualExp = ''
            displayText = ''
            self.lastState = []
        elif text == 'DEL':
            if self.actualExp:
                self.actualExp, displayText = self.lastState.pop()
            else:
                displayText = ''
        elif text == '=':
            self.justPrint = True
            try:
                self.actualExp = str(eval(self.actualExp))
                displayText = self.actualExp
            except Exception:
                self.actualExp = ''
                displayText = 'Error'
        return displayText

    def combinatronicOp(self, text):
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == 'n!':
            self.actualExp = 'factorial(' + self.actualExp + ')'
            displayText += '!'
        elif text == 'nCr':
            displayText = 'Not Supported'
        elif text == 'nPr':
            displayText = 'Not Supported'
        return displayText

    def miscOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == '(':
            self.actualExp += text
            displayText += text
        elif text == ')':
            self.actualExp += text
            displayText += text
        elif text == '%':
            self.actualExp = ''
            displayText = 'Not Supported'
        elif text == 'MOD':
            self.actualExp += '%'
            displayText += 'mod'
        return displayText

    def constantOp(self, text):
        self.justPrint = False
        self.lastState.append((self.actualExp, self.display.text)) 
        displayText = self.display.text
        if text == u"\u03C0":
            self.actualExp = self.actualExp + 'pi'
            displayText += u"\u03C0"
        elif text == 'e':
            self.actualExp = self.actualExp + 'e'
            displayText += 'e'
        return displayText
    
class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()

