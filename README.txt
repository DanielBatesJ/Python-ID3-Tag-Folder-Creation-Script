# ID3 Tag Folder Creation and File Organization Script #

This tool is used for specific file hierarchy in relation to ID3 audio tags. For music catagorization

## How to use as intended: ##
1.) Make sure you have Python set up, and install TinyTag (https://pypi.org/project/tinytag/ or https://github.com/devsnd/tinytag)
2.) Check to make sure your audio files have the following tags:
- Total Number of tracks (Used to determine if the song is a part of an album)
- Album Artist Name (The program uses album artist over artist so that collaborations between artists on albums doesn't interfere)
- Album Name (Used to name the second tiered folder)
- Year (Used to name the second tiered folder)
- I would highly recommend Tag Scanner (https://www.xdlab.ru/en/) for any tag editing needs.
3.) Set up the base path.	
- Change 
	-basePath = ""
- to 
	-basePath = "YOUR DIRECTORY HERE"
- Example: basePath = "C:/Users/CurrentUser/Music/"
- IMPORTANT: Make sure to change the back-slashes ('\') to forward slashes ('/') or else Python won't read your directory
4.) The script is set up to only pay attention to .mp3, .m4a and .wav files
-To add another file type (Such as .flac, .ogg etc)
	-Add an additional statement to this line
		-if name.endswith((".mp3", ".m4a", ".wav")):
	-with
		-, ".FILE_EXTENSION"
	-after ".wav"

- Example: if name.endswith((".mp3", ".m4a", ".wav", ".flac")):
- Feel free to remove codecs you don't want to be effected
5.) Run the script with Python
- The hierarchy will be as follows
	-\ALBUM ARTIST\YEAR - ALBUM\

# What you can change: #
- The easiest user edits can be done to the folder names.
- Lines
        - firstFolder = basePath + '/' + temp_track.albumartist
- &
	- secondFolder = '/' + year + ' - ' + temp_track.album
- define the naming convention for the two folders in the hierarchy.
- The options for changing folder naming are listed bellow.
		- temp_track.album         # album as string
		- temp_track.albumartist   # album artist as string
		- temp_track.artist        # artist name as string
		- temp_track.audio_offset  # number of bytes before audio data begins
		- temp_track.bitrate       # bitrate in kBits/s
		- temp_track.comment       # file comment as string
		- temp_track.disc          # disc number
		- temp_track.disc_total    # the total number of discs
		- temp_track.duration      # duration of the song in seconds
		- temp_track.filesize      # file size in bytes
		- temp_track.genre         # genre as string
		- temp_track.samplerate    # samples per second
		- temp_track.title         # title of the song
		- temp_track.track         # track number as string
		- temp_track.track_total   # total number of tracks as string
		- temp_track.year          # year or data as string

- If you wanted to expand the year to a more specific date, remove
 	- [:4]
- from the line
	- year = temp_track.year[:4]
- This value 4 limits the number of characters in year tag. If you wanted, for example, the whole iTunes release date, including date and time, to be on your folder, this would be how to get that.

### For any other questions, feel free to email me: ###
DanielBatesJ@gmail.com

### References: ###
- @TutorialSpotUK
	- https://www.youtube.com/watch?v=rnW2ibT89Hw
	- Used for the bare outline of the function, Tiny Tags implementation
- @pybear881
	- https://www.youtube.com/watch?v=CHQb85Y1z7Q
	- Used for shutil implementation
