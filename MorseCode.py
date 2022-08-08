#!/usr/bin/env python3
#Morse Code Trainer
from audioplayer import AudioPlayer
from time import sleep
from multiprocessing import Process


def main():

    alphabet = { "a":13, "b":3111, "c":3131, "d":311,           #Defined morse code conversion dictionary 
                "e":1, "f":1131, "g":331, "h":1111, "i": 11,    #1 - dot, 3 - dash
                "j":1333, "k":313, "l":1311, "m":33, "n":31,    #Makes length conversion easier
                "o":333, "p":1331, "q":3313, "r":131, "s":111,
                "t":3, "u":113, "v":1113, "w":133, "x":3113,
                "y":3133, "z":3311, 1:13333, 2:11333, 3:11133,
                4:11113, 5:11111, 6:31111, 7:33111, 8:33311,
                9:33331, 0:33333, ".":131313, "?":113311}

    #Import text to be translated, either from text file or hardcoded
    #sentenceInput = "thanks this was fun"
    sentenceInput = importText()
    sentenceInput = sentenceInput.lower()
    sentence = sentenceInput.split()

    #start audio playing in seperate Process
    morseCode = Process(target= audio, args= (sentence, True, alphabet,))
    morseCode.start()

    #Create text input box so you can type the answer as you hear it
    answer = input("Type the words you hear: ")
    answer = answer.lower()
    answerlist = answer.split()
    if answerlist == sentence:
        print("Correct")
    else:
        print("Incorrect")
        print(sentence)
        print(answerlist)

def importText():
    f = open("testing_text.txt", "r")
    sentence = f.read()
    print(sentence)
    return (sentence)

def audio(sentence, standardMode, alphabet): 
    tone = AudioPlayer("800hz.wav")

    #Standard Timing
    wpm = 25
    unit = 60/(50*wpm)

    #Farnsworth Timing
    s = 20 #trans_wpm
    c = 18 #char_wpm
    ta = (60*c - 37.2*s) / (s*c) 
    tc = 3*ta/19 #Period Between Characters
    tw = 7*ta/19 #period between words
    #print (ta, tc, tw, unit)

    if standardMode == False:
        for word in sentence:
            #print(word)
            for letter in word:
                l = alphabet.get(letter)
                tone.play()
                tone.pause()
                for digit in str(l):
                    digit = int(digit)*unit
                    tone.resume()
                    sleep(digit) #length of symbol (dot/dash)
                    tone.pause()
                    sleep(unit) #between symbol space
                tone.stop()
                sleep(tc) #between Letter space
            sleep(tw)
    else:
         for word in sentence:
            #print(word)
            for letter in word:
                l = alphabet.get(letter)
                tone.play()
                tone.pause()
                for digit in str(l):
                    digit = int(digit)*unit
                    tone.resume()
                    sleep(digit) #length of symbol (dot/dash)
                    tone.pause()
                    sleep(unit) #between symbol space
                tone.stop()
                sleep(unit*3) #between Letter space (3 units)
            sleep(unit*7)

if __name__ == '__main__':
    main()
