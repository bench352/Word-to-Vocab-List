"""
The MIT License (MIT)

Copyright (c) 2022 Ben Choy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import math
import os
from PyDictionary import PyDictionary
from deep_translator import GoogleTranslator

# Displaying progress bar for word looking up
def progressBar(ithItem, ttl):
    completePerc = math.ceil(ithItem / ttl * 25)
    remainPerc = 25 - math.ceil(ithItem / ttl * 25)
    print(
        "█" * completePerc,
        " " * remainPerc,
        "  Looking up (",
        ithItem,
        " of ",
        ttl,
        ")",
        sep="",
        end="\r",
    )


userChoice = ""
print("{WORDS TO VOCABULARY LIST - LITE}")
print("By: Ben Choy")
print("\nThis program can accept a plain text (.txt) file, automatically")
print("look up all the words in it, and generate a Markdown (.md) file")
print("containing meaning and Chinese translation of each word. It also")
print("supports creation of plain text file for importing to Anki.")
print("\n===============================================================")
wordSet = set()
errorWordList = list()
engDict = PyDictionary()
syno = set()
anto = set()

while True:
    print("\n{MAIN MENU}\n")
    print("Enter keyword to select one of the following options:")
    print("[C] Generate vocab list from text file")
    print("[D] Convert the outputted Markdown file to Word Document")
    print("[exit] Quit program")
    print()
    userChoice = input("> ")

    # If user chooses "Generate vocab list from text file"
    if userChoice == "C":
        while True:
            print("\n===============================================================")
            print("\n{GENERATE VOCAB LIST FROM TEXT FILE}\n")
            print("In the plain text file, words should be separated by space or")
            print("line breaks ONLY.")
            print("Enter the file path for the text file:\n")
            userChoice = input("> ")

            try:
                # Open the text file and read words from it
                f = open(userChoice, "r")
                print("\nLoading word list... ", end="")
                wordSet.clear()
                for line in f:
                    tmpLine = line.rstrip("\n")
                    for w in tmpLine.split(" "):
                        wordSet.add(w)
                f.close()
                wordSet.discard("")
                wordList = sorted(wordSet)
                wordListLen = len(wordList)
                print("Found " + str(wordListLen) + " word(s)!")

                errorWordList.clear()

                # Prompt user to choose output options
                makeMarkdown = False
                makeTXT = False
                print("\nDo you want to create a Markdown file for word meanings")
                print("and Chinese translation?")
                print("[Y] Yes     [N] No\n")
                userChoice = input("> ")
                if userChoice == "Y":
                    makeMarkdown = True
                print()

                print("Do you want to create a plain text file for importing to Anki?")
                print("[Y] Yes     [N] No\n")
                userChoice = input("> ")
                TXTMode = 0
                if userChoice == "Y":
                    makeTXT = True
                    print("\nSelect mode for plain text file output:")
                    print("[1] English Word - English Meaning")
                    print("[2] English Word - Chinese Translation")
                    print("[3] English Word - English Meaning & Chinese Translation\n")
                    while True:
                        userChoice = input("> ")
                        if userChoice == "1" or userChoice == "2" or userChoice == "3":
                            TXTMode = int(userChoice)
                            break
                        else:
                            print(
                                "\n<Error> Invalid input! Please input [1], [2] or [3] only.\n"
                            )
                print()

                # Creation of output files
                if makeMarkdown or makeTXT:

                    if makeMarkdown:
                        f = open("Output.md", "w", encoding="utf-8")

                        # Create heading for Markdown file
                        f.write("# Vocabulary List\n\n")
                        f.write(
                            "Meaning of words from WordNet\n\nChinese translation by Google Translate\n\nSynonyms and antonyms from WordNet\n\n"
                        )

                    if makeTXT:
                        cf = open("Output.txt", "w", encoding="utf-8")
                    idx = 1

                    for w in wordList:
                        progressBar(idx, wordListLen)
                        singleWDict = engDict.meaning(w, True)

                        if singleWDict is None:
                            errorWordList.append(w)
                        else:

                            # Looking up English meaning of each word and write to files
                            if makeMarkdown:
                                f.write("## " + w + "\n\n")
                            if makeTXT:
                                cf.write(w + ';"')
                            for key in singleWDict:
                                if makeMarkdown:
                                    f.write("**[" + key + "]** ")
                                if makeTXT and (TXTMode == 1 or TXTMode == 3):
                                    cf.write("[" + key + "] ")
                                for meaning in singleWDict[key]:
                                    if makeMarkdown:
                                        f.write(meaning + "; ")
                                    if makeTXT and (TXTMode == 1 or TXTMode == 3):
                                        cf.write(meaning + "; ")
                                if makeMarkdown:
                                    f.write("\n\n")
                                if makeTXT and (TXTMode == 1 or TXTMode == 3):
                                    cf.write("\n")

                            # Looking up Chinese translation of each word and write to files
                            translatedWord = GoogleTranslator(
                                source="auto", target="zh-TW"
                            ).translate(w)
                            if makeMarkdown:
                                f.write("**[中譯]** " + translatedWord + "\n\n")
                            if TXTMode == 3:
                                cf.write("[中譯] ")
                            if makeTXT and (TXTMode == 2 or TXTMode == 3):
                                cf.write(translatedWord)
                            if makeTXT:
                                cf.write('";\n')

                        idx += 1

                    # Finished looking up all the words
                    # Close the files
                    if makeMarkdown:
                        f.close()
                    if makeTXT:
                        cf.close()

                    # Completed file creation
                    print("File creation completed! File saved as [", end="")
                    if makeMarkdown:
                        print("Output.md", end="")
                    if makeMarkdown and makeTXT:
                        print("] & [", end="")
                    if makeTXT:
                        print("Output.txt", end="")
                    print("]")

                    # If there're words that cannot be looked up
                    # Ask user if he/she wants to see them
                    if len(errorWordList) > 0:
                        print(
                            len(errorWordList),
                            " word(s) cannot be looked up! Do you want to check out?",
                            sep="",
                        )
                        print("[Y] Yes     [N] No\n")
                        userChoice = input("> ")
                        if userChoice == "Y":
                            print("\nList of word(s) that cannot be looked up:")
                            for ew in errorWordList:
                                print(ew, end="; ")
                            print()
                    print(
                        "\n==============================================================="
                    )

                else:
                    print("<Error> No file type is selected for export.")
                break

            # If user enters an incorrect file path
            except IOError:
                print("\n<Error> File input error!")
                print("Do you want to try again?")
                print("[Y] Yes     [N] No\n")
                userChoice = input("> ")
                if userChoice != "Y":
                    break

    # If user chooses "Generate vocab list from text file"
    elif userChoice == "D":
        print()
        try:
            if os.path.exists("Output.md"):
                print("Converting file...", end="\r")
                systemCMD = "pandoc -t docx Output.md -o Output.docx"
                CMDresult = os.system(systemCMD)
                if CMDresult == 0:
                    print("Convertion success! File saved as [Output.docx]")
            else:
                print("\n<Error> [Output.md] not found!")
        except Exception as e:
            print(e)

    # If user chooses to quit the program
    elif userChoice == "exit":
        break

    # If user enters a wrong command
    else:
        print("\n<Error> Invalid command!")
