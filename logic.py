"""Module with logical part of the keyboard trainer"""

from collections import defaultdict
import time
from utils import log, match, calculateSpeed, readFromJson, sendToJson
from gui import KeyboardTrainApp, KeyboardListener
from random import randrange

class KeyboardTrainer:
    """Main class of the logical part of the keyboard trainer"""
    def __init__(self):
        """Build the app and run it"""
        self.app = KeyboardTrainApp(self)
        self.app.run()
        self.keyboardInput = None

    def newInput1(self, instance):
        """Starts new phase of input with text from the textarea"""
        need_to_open_file = "Easy level texts/Text" + str(randrange(1, 5)) + ".txt"
        with open(need_to_open_file) as text_1:
            self.text1 = text_1.read()
        log('new')
        insertedText = self.text1
        log('inserted text:', insertedText)

        if len(insertedText) == 0:
            return

        self.keyboardInput = KeyboardInput(insertedText,
                                           self.app, self.endInput)
        self.app.newPhrase(self.keyboardInput, insertedText)

    def newInput2(self, instance):
        """Starts new phase of input with text from the textarea"""
        need_to_open_file = "Hard level texts/Text" + str(randrange(1, 5)) + ".txt"
        with open(need_to_open_file) as text_2:
            self.text2 = text_2.read()
        log('new')
        insertedText = self.text2
        log('inserted text:', insertedText)

        if len(insertedText) == 0:
            return

        self.keyboardInput = KeyboardInput(insertedText,
                                           self.app, self.endInput)
        self.app.newPhrase(self.keyboardInput, insertedText)

    def endInput(self, textLen, totalClicks, inputTime, wrongLetters):
        """Move current data to the file with statistics
        and show the menu with statistics"""
        nowSpeed = calculateSpeed(textLen, inputTime)
        nowMistakes = totalClicks - textLen

        data = readFromJson()
        if 'totalClicks' in data and data['totalClicks'] != 0:
            data['averageSpeed'] *= data['totalClicks']
            data['averageSpeed'] += totalClicks * nowSpeed
            data['totalClicks'] += totalClicks
            data['averageSpeed'] /= data['totalClicks']
            newWrongLetters = defaultdict(int)
            for letter in data['wrongLetters']:
                newWrongLetters[letter] = data['wrongLetters'][letter]
            for letter in wrongLetters:
                newWrongLetters[letter] += wrongLetters[letter]
            data['wrongLetters'] = newWrongLetters
        else:
            data['averageSpeed'] = nowSpeed
            data['totalClicks'] = totalClicks
            data['wrongLetters'] = wrongLetters
        sendToJson(data)

        log('You wrote it!')
        log('Your speed:', nowSpeed)
        log('Your time:', round(inputTime, 1))
        log('Your mistakes:', nowMistakes)
        log('Your average speed:', data['averageSpeed'])

        self.keyboardInput = None
        self.app.endMenu(nowSpeed, nowMistakes, data['averageSpeed'])

    def interupt(self, instance):
        """Interupts input"""
        self.keyboardInput.interupt()

    def reset(self, instance):
        """Delete all saved statistics"""
        sendToJson({})
        self.endInput(0, 0, 10, {})

class KeyboardInput:
    """Class of the one input phase. Getting input and return it to the app"""
    letterNumber = 0
    startTime = 0
    totalClicks = 0
    needToUnbind = False
    wrongLetters = defaultdict(int)

    def __init__(self, text, app, endFunc):
        """Setting up the object and bind the keyboard listener"""
        self.text = text
        self.app = app
        self.endFunc = endFunc
        self.listener = KeyboardListener(self.onKeyDown)

    def onKeyDown(self, keycode, text, modifiers):
        """Fires in key down event.
        Collect new statistic and starts redrawing window"""
        log('The key', keycode, 'have been pressed')
        log(' - modifiers are %r' % modifiers)
        if self.needToUnbind:
            return True

        if self.startTime == 0:
            self.startTime = time.time()

        if keycode[1] == 'enter':
            text = '\n'
        if keycode[1] == 'tab':
            text = '\t'

        if len(keycode[1]) == 1 or keycode[1] == 'spacebar' or\
           keycode[1] == 'tab' or keycode[1] == 'enter':
            self.totalClicks += 1

        if match(text, self.text[self.letterNumber], modifiers):
            log('Right letter!!!')
            self.letterNumber += 1
            self.app.addLetter(self.letterNumber, self.text)
        else:
            log('Wrong letter!!! Got:', text,
                'I needed:', (self.text[self.letterNumber],))
            self.wrongLetters[self.text[self.letterNumber]] += 1

        if len(self.text) == self.letterNumber:
            self.endInput()
            return True
        return False

    def interupt(self):
        """Interupt input and set need to unbind keyboard"""
        self.needToUnbind = True
        self.endInput()

    def endInput(self):
        """Runs trigger function for the end of the input"""
        endTime = time.time()
        self.endFunc(self.letterNumber, self.totalClicks,
                     endTime - self.startTime, self.wrongLetters)
