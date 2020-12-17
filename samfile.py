#!/usr/bin/python3
#!/usr/bin/env python3
import argparse

#parser = argparse.ArgumentParser(description='Enter File location')
#parser.add_argument('--file', type=str,dest="filepaths")
#parser.add_argument('--output',type=str,dest="outputFileName")
#args = parser.parse_args()

#fileToOpen = args.filepaths
#aoutputFileName = args.outputFileName

#f= open(fileToOpen, "r")
f= open("Lactobacillus_crispatus_Aligned.sam")
lines = f.readlines()
fields = sam_string.rstrip().split()
name= field[0]
print(name)