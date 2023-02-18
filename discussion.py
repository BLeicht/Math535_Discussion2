import sys
import random
import numpy as np
from skimage import io, color, util


def main(imageFilePath="Ondra_sampling.jpg", randomSeed=0):
    coverArray = OutputAsGrayscale(imageFilePath)
    payload = CreatePayload(imageFilePath, int(randomSeed))
   
    stegoArray = EmbedMessage(coverArray, payload)
 
    rows = coverArray.shape[0]
    columns = coverArray.shape[1]
    numerator = rows*columns
    
    denominator = NumDifferences(coverArray, stegoArray) 
    
    embedEff = round(numerator/denominator, 4)
    print(embedEff)


# Finds the number of different pixels in two grayscale images
def NumDifferences(cover, stego):
    numDiff = 0
    for i in range(cover.shape[0]):
        for j in range(cover.shape[1]):
            if (cover[i][j] != stego[i][j]):
                numDiff += 1
    
    return numDiff

#Takes an RGB image and converts it to grayscale. 
#Returns the grayscale np.array and saves the grayscale image to disk with the word "Grayscale" tacked on the end.   
def OutputAsGrayscale(imageFilePath):
    image = io.imread(imageFilePath)
    image = color.rgb2gray(image)

    image = util.img_as_ubyte(image)
    io.imsave((imageFilePath[:-4] + "Grayscale.png"), image)

    return image




#Creates the payload for the cover at maximum capacity
def CreatePayload(inputImagePath, seed=0):
        random.seed(seed)

        imageArray = io.imread(inputImagePath)
        rows = imageArray.shape[0]
        cols = imageArray.shape[1]
       
 
        payload = np.zeros((rows, cols), dtype=bool)

        for row in range(rows):
            for col in range(cols):
                payload[row][col] = random.randint(0, 1)


        return payload

# Embeds the hidden message in the cover image array
def EmbedMessage(coverImageArray, hiddenMessage):
    stegoImageArray = coverImageArray.copy()
    for i in range(coverImageArray.shape[0]):
        for j in range(coverImageArray.shape[1]):
            stegoImageArray[i][j] -= stegoImageArray[i][j]%2
            stegoImageArray[i][j] += hiddenMessage[i][j]

    io.imsave("stegoImage.png", stegoImageArray)
    return stegoImageArray
