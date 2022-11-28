"""Some useful functions"""

import json
import easygui
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from config import e2E, e2r, e2R, DEBUG, STAT_FILE_NAME, MAX_SPEED
from char_map import get_all_pixels, get_coords


def log(*args):
    """Just as print, but only if DEBUG == True"""
    if DEBUG:
        print(*args)


def match(key, target, mod):
    """Answer does the pressed key match with target letter"""
    if key == target:
        return True
    if key not in e2E:
        return False
    if ('shift' in mod) ^ ('capslock' in mod):
        # capitalized
        return target in (e2R[key], e2E[key])
    # lower
    return target in (key, e2r[key])


def calculateSpeed(lettersNumber, time):
    """Calculate speed from number of input letters and imput time"""
    return 60 * lettersNumber / time


def readFromJson():
    """Read statistics from file and return it as dictionary"""
    file = open(STAT_FILE_NAME, 'r')
    data = json.load(file)
    file.close()
    return data


def sendToJson(data):
    """Take dictionary with new statistics and write it to the file"""
    file = open(STAT_FILE_NAME, 'w')
    json.dump(data, file)
    file.close()


def formSpeed(speed):
    """Limits the speed for the beautiful output"""
    if speed < MAX_SPEED:
        return str(round(speed, 1))
    return '>' + str(MAX_SPEED)


def getFrequencies(contents):
    """Get the frequencies of certain keypresses in dictionary."""
    heatmapData = np.asarray([[0] * 57] * 21)

    for char in contents:
        coords = get_coords(char)
        if coords:
            for coord in coords:
                x, y = coord
                heatmapData[x][y] += contents[char]

    total = np.sum(heatmapData)
    if total != 0:
        heatmapData = heatmapData / total

    for pixel in get_all_pixels(((18, 18), (19, 34))):
        x, y = pixel
        heatmapData[x][y] *= 0.3

    return heatmapData[::-1]

def mostMissButtons():
    """Return a list with buttons
    with most mistakes from statistic file"""
    data = readFromJson()
    if 'wrongLetters' in data:
        heatmap = [(-c, l) for (l, c) in data['wrongLetters'].items()]
        heatmap.sort()
        return ' '.join([str(x[1]) for x in heatmap][:5])
    return 'No statistics yet'

