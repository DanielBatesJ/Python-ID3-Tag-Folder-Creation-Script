import os
import shutil
from tinytag import TinyTag, TinyTagException


def main():

    basePath = "S:/Downloads/To do/Tagged/"  # Change what's in the quotation marks, to be the directory you want to work in
    for root, dirs, files, in os.walk(basePath):
        for name in files:
            if name.endswith((".mp3", ".m4a", ".wav")):  # Keeps the scope limited to the most common music formats
                try:
                    temp_track = TinyTag.get(root + "\\" + name)  # temp_track is the variable used to access the audio tags

                    year = temp_track.year[:4]
                    firstFolder = basePath + '/' + temp_track.albumartist
                    secondFolder = '/' + year + ' - ' + temp_track.album
                    fileLocation = basePath + '/' + name

                    if int(temp_track.track_total) > 1:
                        # If the tag for total tracks in the album is more than one, the bellow functions account for the potential that the directory already exists
                        if os.path.exists(firstFolder):
                            # Path for if the path has already been created, due to previous processing on other tracks in the same collection
                            if os.path.exists(firstFolder + secondFolder):
                                # If a previous song from the collection has already been processed, we move the song to the folder created for the collection.
                                shutil.move(fileLocation, firstFolder + secondFolder)
                                # This is the move command that will move your current file, to the new directory created for it
                            elif not os.path.exists(firstFolder + secondFolder):
                                # Creates the YEAR - ALBUM NAME folder, if it doesn't already exist, and moves the track to it
                                os.makedirs(firstFolder + secondFolder)
                                shutil.move(fileLocation, firstFolder + secondFolder)

                        elif not os.path.exists(firstFolder):
                                # Follows previous steps, only with the path not existing.
                            os.makedirs(firstFolder)
                            if os.path.exists(firstFolder + secondFolder):
                                shutil.move(fileLocation, firstFolder + secondFolder)
                            elif not os.path.exists(firstFolder + secondFolder):
                                os.makedirs(firstFolder + secondFolder)
                                shutil.move(fileLocation, firstFolder + secondFolder)

                    elif int(temp_track.track_total) == 1:
                        # The same code as the first if, only it ignores the chance of more than one song going into a particular folder.
                        if os.path.exists(firstFolder):
                                # Stops the program from looping needlessly
                            return
                        os.makedirs(firstFolder)
                        os.makedirs(firstFolder + secondFolder)
                        shutil.move(fileLocation, firstFolder + secondFolder)
                except TinyTagException:
                        # Catches errors in corrupted audio tags
                    print("Error")


main()
