#!/usr/bin/python3

import sys, re, ffmpeg, os

try:
    filename = sys.argv[1]
    filepath = os.path.join(os.getcwd(), filename)
    bookFile = ffmpeg.input(filepath, vn=None)

    metaDict = ffmpeg.probe(filepath,show_chapters=None)
    os.makedirs(filename.split('.')[0])
    os.chdir(filename.split('.')[0])

except IndexError:
    print("File name missing, must have file name passed as argument")
    sys.exit(1)

for i in range(0,len(metaDict['chapters']),1):
    chapTitle = metaDict['chapters'][i]['tags']['title']
    chapTitle = re.sub("['-]", "", chapTitle)
    startTime = metaDict['chapters'][i]['start_time']
    endTime = metaDict['chapters'][i]['end_time']
    chapNum = metaDict['chapters'][i]['id'] + 1

    trackName = "{}.mp3".format(chapTitle)

    outbound = ffmpeg.output(bookFile,trackName,ss=startTime,to=endTime,map_chapters="-1")
    ffmpeg.run(outbound)
