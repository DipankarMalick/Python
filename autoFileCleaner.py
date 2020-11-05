import os

#If folder not exist then create folder
def createFolder(folder):
    if not os.path.exists(folder):
        print("Folder not Created")
        print("Creating New Folder.......\nFolder Created Successfully!")
        os.makedirs(folder)

# Move Files into Folder
def move(folderName,files):
    print("Moving Files into Specific Folder.........")
    for file in files:
        os.replace(file, f"{folderName}/{file}") 
    print("Done!")     
    

files = os.listdir()
files.remove("autoFileCleaner.py")
print("Checking folder........")
createFolder('Images')
createFolder('Docs')
createFolder('Media')
createFolder('Others')
print("Checking Files......")
imgExts = [".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

docExts = [".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts] 

mediaExts = [".mp4",".mp3",".flv",".mkv",".webm"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts):
        others.append(file)

#Move files into created folder
move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Others",others)
