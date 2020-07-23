import zipfile, os

def backupToZip(folder):
    """Backup the entire content of "folder" into a ZIP file"""
    
    folder = os.path.abspath(folder)

    #Find out wich version of backup     
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        
    #Create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    
    #Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding file in {foldername}...')
        #Add the current folder to the ZIP file
        backupZip.write(foldername)
        
        #Add all the file in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    
    print('Done!')

backupToZip('/home/russianbb/www/automate_python')