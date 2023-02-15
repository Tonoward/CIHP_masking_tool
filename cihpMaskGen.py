import cv2
import numpy as np
import os
import argparse
from pathlib import Path



def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Required arguments
    parser.add_argument("--inpath", help="The output path for the masks", type=str)
    parser.add_argument("--outpath", help="The output path for the masks", type=str)

    # Optional arguments
    parser.add_argument("--hair", help="Hair", action="store_true")
    parser.add_argument("--hat", help="Hat", action="store_true")
    parser.add_argument("--face", help="Face", action="store_true")
    parser.add_argument("--torso", help="Torso or upper bare skin part of the body. this includes the neck", action="store_true")
    parser.add_argument("--top_inner", help="Inner clotes for the torso (T-shirts, shirts, blouses, etc.)", action="store_true")
    parser.add_argument("--top_outer", help="Outer clothes apart from the inner ones, this is only valid if there is an inner clothing piece. this category may include Sweaters, jackets, etc.", action="store_true")
    parser.add_argument("--arm_left", help="Left arm, including the hand", action="store_true")
    parser.add_argument("--arm_right", help="Right arm, including the hand", action="store_true")
    parser.add_argument("--dress", help="Dress", action="store_true")
    parser.add_argument("--bottom_pants", help="Bottom clothing such as pants, or even an overall", action="store_true")
    parser.add_argument("--bottom_shorts", help="Bottom clothing in the category of short pants", action="store_true")
    parser.add_argument("--leg_left", help="Left leg", action="store_true")
    parser.add_argument("--leg_right", help="Right leg", action="store_true")
    parser.add_argument("--shoe_left", help="Left shoe", action="store_true")
    parser.add_argument("--shoe_right", help="Right shoe", action="store_true")

    # Print version
    parser.add_argument("--version", action="version", version='%(prog)s - Version 1.0')

    # Parse arguments
    args = parser.parse_args()

    # Convert args to a dictionary
    checkArgsDict = vars(args)

    # Remove the outpath and version from the dictionary
    checkArgsDict = {k: checkArgsDict[k] for k in set(list(checkArgsDict.keys())) - set(['outpath', 'version'])}

    checkflag = False

    if not args.inpath:
        parser.error('Please provide the input path with --inpath. Check --help to know how to use it')

    if not args.outpath:
        parser.error('Please provide the output path with --outpath. Check --help to know how to use it')

    for key in checkArgsDict.keys():
        if checkArgsDict[key] == True:
            checkflag = True
            break

    if not checkflag:
        parser.error('Please provide at least one item to mask. Check --help to know what items are available')

    return args

maskColors = {
    'hair': [0,0,255],
    'hat': [0,0,128],
    'face': [255,0,0],
    'torso': [0,51,85],
    'top_inner': [0,85,255],
    'top_outer': [221,119,0],
    'arm_left': [221,170,51],
    'arm_right': [255,255,0],
    'dress': [85,0,0],
    'bottom_pants': [85,85,0],
    'bottom_shorts': [0,128,0],
    'leg_left': [170,255,85],
    'leg_right': [85,255,170],
    'shoe_left': [0,255,255],
    'shoe_right': [0,170,255]
}

def process(path):

    img = cv2.imread(path)

    # Create a black image with the size of the original image on just one channel
    maskSum = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    # Array to store the masks for the required item
    masks=[np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)]*15

    i=0
    for key in maskColors.keys():
        if getattr(args, key) == True:
            maskVal = maskColors[key]
            masks[i] =(img[:, :, 0:3] == maskVal).all(2)
        i = i+1     
            
    maskSum = 255*(maskSum + masks[0] + masks[1] + masks[2] + masks[3] + masks[4] + masks[5] + masks[6] + masks[7] + masks[8] + masks[9] + masks[10] + masks[11] + masks[12] + masks[13] + masks[14])
    maskSum = maskSum.clip(0, 255).astype("uint8")

    return maskSum


if __name__ == '__main__':
    # Parse the arguments
    args = parseArguments()

    i = 1

    for (image_file) in os.listdir(args.inpath):
        if image_file.endswith(".png"):
            print(f"processing {i}th image...")
            cv2.imwrite(os.path.join(args.outpath, Path(image_file).stem + "_mask.png"), process(os.path.join(args.inpath, image_file)))
            i = i+1
    
    print(f"Done processing {i-1} images.")


    

    