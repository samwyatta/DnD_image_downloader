# Image downloader.  Requires you to copy and paste website source page to .txt file.
# Outputs images saved as image_{chapter_identifier}_{image_number}.

import re
import requests
import os

# Functions that will be part of the main function

def parse_text(txt_file, pattern):
    if int(len(url_list)) > 0:
        i = int(len(url_list))
    else:
        i = 0
    with open(txt_file, errors='ignore') as file:
    # Loop through each line in the file
        text = file.read()
    urls = re.findall(pattern, text)
    for url in urls:
        url_list.append(url)
        # we don't want tiny thumbnail images, yuck!
        
        # The following if statements will get rid of the string after the filetype and then append the correct file type
        if '.jpg' in url_list[i]: 
            url_list[i] = url_list[i].split('.jpg')[0]+'.jpg'
        if '.png' in url_list[i]: 
            url_list[i] = url_list[i].split('.png')[0]+'.png'
        if '.jpeg' in url_list[i]: 
            url_list[i] = url_list[i].split('.jpg')[0]+'.jpeg'
        if 'thumbnail' in url_list[i]:
            del url_list[i]
            # we subrtract 1 from the counter or else the loop will throw an error because 'i' will be greater than the last item in the list.
            i = i-1
        i = i+1
    print('parse_text: finished')            
                
def download_image(url_list):
    i = 0
    n = 0
    for url in url_list:
        # use the requests library to access the image url
        response = requests.get(url)
        download_path = rf'D:\Photos_to_upload\{book}\test\{book}_image_{chapter_identifier}_'
        if response.status_code == 200:
            #append the counter and '.png' to the filepath to make unique .png files
            #'wb' lets you write binary rather than text to save an actual image instead of some crazy string
            with open(download_path+str(i)+'.png', "wb") as f:
                f.write(response.content)
                n = n+1
            # print(f"Image '{download_path}{i}' successfully downloaded!")
        else:
                print(f"Failed to download image '{download_path}{i}'.")
                # this will help us see what problems our urls have so we can update the parse_text function to do a better job!
                bad_url_index.append(i)
        i = i + 1
    print("download_image: finished")
    print(f'{n} image(s) dowloaded')

def build_ch_lists(directory):
    # function to build lists that have the paths for the .txt files and the chapter identifier tag
    # these lists will be used to tell the parse_text and download_image functions where files are and how to name images.
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            chapter_identifier = filename[-8:-4]
            ch_dir_list.append(filename)
            ch_id_list.append(chapter_identifier)

def main():
    parse_text(txt_file, pattern1)
    parse_text(txt_file, pattern2)
    parse_text(txt_file, pattern3)
    # print(url_list)
    download_image(url_list)
    i=0
    if int(len(bad_url_index)) >= 1:
        print("List of failed urls:")
        for item in bad_url_index:
            print(f"index number {bad_url_index[i]}: " + url_list[bad_url_index[i]])
            i = i+1
    else:
        print("main: finished")
    
# Variables and objects that exist outside of functions
ch_dir_list = []
ch_id_list = []
url_list = []
bad_url_index = []
i = 0
# print("Enter the book abbreviation: ")
print('Enter the Book abbreviation used in the directory: ')
book = input()
directory = f'D:\Photos_to_upload\{book}\Chapters_Source_Page'
chapter_identifier = '' 


pattern1 = 'https://www.dndbeyond.com/attachments/.{45}'
pattern2 = 'https://www.dndbeyond.com/avatars/.{40}'
pattern3 = 'https://media.dndbeyond.com/compendium-images/.{75}'

build_ch_lists(directory)
ch_count = 0
for d in ch_dir_list:
    chapter_identifier = ch_id_list[ch_count]
    txt_file = f'D:\Photos_to_upload\{book}\Chapters_Source_Page\{chapter_identifier}.txt'
    main()
    url_list.clear()
    bad_url_index.clear()

    ch_count = ch_count + 1