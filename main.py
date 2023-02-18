import sys
from discussion import main


if (__name__ == "__main__"):
    if (len(sys.argv) <= 2):
        print("\nRunning with default values!\nIf you want to change the parameters, the cli arguments are as follows:\n1) FilePath\n2) Seed for message generation\n")
        main()
    else:
        main(imageFilePath=sys.argv[1], randomSeed=sys.argv[2])
