#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KatieHarte
#
# Created:     23/04/2016
# Copyright:   (c) KatieHarte 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""This is a little program that simulates the amount of half and whole tabs in
Charlie's bottle of folic acid. He gets a half tab every day. I pick one tablet
out of the container, and if it is already cut in half I give it to him as is,
otherwise, I cut it in half and put the other half back in the bottle. I'm
assuming the half and whole tablets are evenly distributed through the bottle"""

import random

open('Single-pill-simulator.txt', 'w').close()
open('Pill-simulator-combined-results.txt', 'w').close()

def pillSimulator(numCycles):

    for x in range(numCycles):
        tabs = 500.0
        doses = 0
        halfTabs = 0
        wholeTabs = 500

        while tabs > 0:
            doses += 1
            tabs -= 0.5

            if halfTabs == 0:
                wholeTabs -= 1
                halfTabs += 1

            elif wholeTabs == 0:
                halfTabs -= 1

            else:
                currentOdds = halfTabs/(halfTabs + wholeTabs) * 100
                currentRandomNum = random.randint(0, 100)

                if currentOdds >= currentRandomNum:
                    halfTabs -= 1

                else:
                    wholeTabs -= 1
                    halfTabs += 1

            f = open('Single-pill-simulator.txt', "a")
            f.write("half tabs: " + str(halfTabs) + "\n")
            f.write("whole tabs: " + str(wholeTabs) + "\n")
            f.close()

        print("all done!")

pillSimulator(1)