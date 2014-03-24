"""
copyFilesDirectory.py

I created this quick hack to save some time to copy a rubric named the same as
each student's powerpoints for the 101 class that I TA for. 

Copies a file from an origLoc to a src folder.
Makes a copy of the origLoc document for each file inside the src folder.
The origLoc document is then renamed to be the same as each file in the src folder

"""


import os
import shutil

#origLoc - file to be copied
#src - Folder where to be copied
def copyFiles(origLoc, src):
    dest = src
    src_files = os.listdir(src) #Returns an array of all files in src folder *powerPointNames
    print src_files

    #file_name would be name of powerpoint
    #src_files would be file location of powerpoints
    for file_name in src_files:
        #copys .docx to src folder
        full_file_name = os.path.join(src,file_name)
        if(os.path.isfile(full_file_name)):
            shutil.copy(origLoc, src)
            
        #gives me the full file name of the current file
        docx_file_name = os.path.join(src, "template.docx")

        position = full_file_name.find(".")
        new_full_file_name = full_file_name[:position] + ".docx"
        os.rename(docx_file_name, new_full_file_name)

copyFiles("/Users/zacharybensley/Desktop/template.docx", "/Users/zacharybensley/Desktop/101Pres")
