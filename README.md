# DnD_image_downloader
This is meant to help download images from DnDBeyond.  

There is no GUI, so if you want to use it, you'll have to do some tinkering.  Mainly you'll need to tell it where in your directory your files are.  There are 3 variables you will need to update initially:
download_path (line 43)
directory (line 92)
txt_file (line 104)

The script is made to look for files with a specific naming convention.  I've included an 'example_structure' folder here on GitHub.  You can rename the example_structure folder to anything you like.  The script will prompt you to tell it the 'Book abbreviation used in the directory'.  Input whatever you have renamed the example_structure folder.  The script will then parse the .txt files in the 'Chapters_Source_Page' folder.  The .txt files should be the page sources from the different chapters of the book for which you are getting images.  It is important that the text files have exactly 4 characters in their names.  Their names are used to build a list of files, and if each file does not have a unique 4 character name, files could be skipped or missed when the script is parsing them.

You will need to manually populate the .txt files.  This can be done by navigating to the chapter in the book you are downloading images for, right clicking on the page, selecting 'view page source' or a similar option, and finally copying and pasting the text from the page source to the .txt file.
