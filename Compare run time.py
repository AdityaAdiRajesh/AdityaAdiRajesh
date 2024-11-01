import os
import magic
import stat
from pypdf import PdfReader
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import time
reportSINInfo = []

file = open("Report Generation File","w")
file.close()



def change_file_permissions(filepath):
    try:
        # Change the file permission to allow read access (rwx for owner)
        os.chmod(filepath, stat.S_IRWXU)

    except Exception as e:
        print(f"Failed to change permissions for {filepath}: {e}")



from luhn import *
def checkForSin(listOfCharachters, possibleReturn):
    print(listOfCharachters)
    acceptedChar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '-', '_', ',', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    accepteNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    if len(listOfCharachters) >= 9:
        for values in listOfCharachters:
            if values in acceptedChar:

                possibleReturn.append(values)
                if len(possibleReturn) == 9:

                    allowed = 0
                    returnValue = ''
                    for values in possibleReturn:
                        if values in accepteNum:
                            allowed += 1
                            returnValue += str(values)
                    if allowed == 9:

                        return verify(returnValue)
            else:
                possibleReturn = []


    return 'No SIN'






def list_files_in_directory(directory):
    # List to store file names and their full paths
    file_paths = []

    # Walk through all directories and files within the given directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Full path of the file
            full_path = os.path.join(dirpath, filename)
            try:
                # Use magic to detect the file type
                file_type = magic.from_file(full_path)
                fileTypeSpesific = file_type.split(',')

                #THIS CHUNK OF CODE PROCESSES PDF DOCUMENTS
                if fileTypeSpesific[0].strip() == "PDF document":
                    print(f"\nProcessing PDF: {full_path}")
                    print(f"File Type: {fileTypeSpesific[0]}")
                    reader = PdfReader(full_path)  # Pass the full path of the file here
                    # Print the number of pages in the PDF
                    print(f"Number of pages: {len(reader.pages)}")
                    # Get the first page from the PDF file
                    numOfNum = 0

                    if len(reader.pages) != 0:
                        page = reader.pages[0]
                        # Extract text from the first page
                        text = page.extract_text()
                        charachterString = str(text).split()
                        setOfValaues = []
                        setOfSin = []
                        acceptedStringNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                        acceptedNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                        for values in charachterString:
                            for charachters in values:
                                setOfValaues.append(charachters)

                                if charachters in acceptedStringNum or charachters in acceptedNum:
                                    numOfNum +=1
                        print(f"Number of numbers in the file: {numOfNum}")

                        if numOfNum >= 9:
                            returnValue = checkForSin(setOfValaues, setOfSin)
                            print(f"SIN Found: {returnValue}")
                            if returnValue == True:
                                reportFile = open('Report Generation File', 'a')
                                mainReportFile = open("Full Report Genertation", 'a')
                                SINInfo = f"SIN found in {filename}, Full Path: {full_path}"
                                if SINInfo not in reportSINInfo:
                                    reportSINInfo.append(f"SIN found in {filename}, Full Path: {full_path}")
                                    mainReportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                                    reportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                                    reportFile.close()
                                    mainReportFile.close()
                                else:
                                    mainReportFile.close()
                                    reportFile.close()




                        else:
                            print("No SIN Found")


                    else:
                        print(f"PDF is empty: {full_path}")
                # THIS IS THE END OF THE PDF PROCESSING CODE
                #elif fileTypeSpesific[0].strip() == "txt":
                elif str(filename).split('.')[1] == 'txt':
                    #____ FILE IS READ AS EMPTY FIX RN =(
                    fileToRead = open(full_path,'r')
                    lineOfInfoStored = fileToRead.readlines()
                    acceptedStringNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ,'-','_','.',' ','/']
                    acceptedNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                    setOfValuesThatWork = []
                    returnList = []
                    for values in lineOfInfoStored:

                        if len(values) >=1:
                            for charachters in values:
                                if charachters in acceptedStringNum or charachters in acceptedNum:
                                    setOfValuesThatWork.append(charachters)
                                    if len(setOfValuesThatWork) >=9:
                                        strippedSIN = []
                                        for char in setOfValuesThatWork:
                                            if char in acceptedNum:
                                                strippedSIN.append(char)
                                        returnVal = checkForSin(strippedSIN,returnList)
                                        print(f"SIN FOUND: {returnVal}")
                                        if returnVal == True:
                                            reportFile = open('Report Generation File', 'a')
                                            mainReportFile = open("Full Report Genertation",'a')
                                            SINInfo = f"SIN found in {filename}, Full Path: {full_path}"
                                            if SINInfo not in reportSINInfo:
                                                reportSINInfo.append(f"SIN found in {filename}, Full Path: {full_path}")
                                                mainReportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                                                reportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                                                reportFile.close()
                                                mainReportFile.close()
                                            else:
                                                mainReportFile.close()
                                                reportFile.close()


                                else:
                                    setOfValuesThatWork = []










                    fileToRead.close()






            except PermissionError:
                change_file_permissions(full_path)
                try:
                    # Retry reading file type after changing permissions
                    file_type = magic.from_file(full_path)
                    file_paths.append(full_path)
                except Exception as e:
                    print(f"Failed to process {full_path} even after changing permissions: {e}")
            except Exception as e:
                # Handle other exceptions (e.g., file not found)
                print('')


# Input: specify the directory you want to scan

listOfLabels = []
def subRun(directory):
    print(list_files_in_directory(directory))
    openedFile = open("Report Generation File",'r')

    for lines in openedFile:
        if lines not in listOfLabels:
            label = Label(root, text=str(lines))
            listOfLabels.append(label)
            # this creates x as a new label to the GUI
            label.pack()

    openedFile.close()
def destroy(listOfLabels):
    for labels in listOfLabels:
        labels.destroy()
        listOfLabels.remove(labels)





    # create root window
root = tk.Tk()

# root window title and dimension
root.title("Directory Parser")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))



img = ImageTk.PhotoImage(Image.open("magnifying.png"))
panel = Label(root, image = img)
panel.pack()

# Data Entry
# creating a label for password

my_label = tk.Label(root, text = "Enter Directory Here ")
my_label.pack()

entry = tk.Entry(root, width=20)
entry.pack()
# creating button

btn = tk.Button(root, text="Search", command=lambda: subRun(directory = (entry.get()).strip('"')))
btn.pack()

btn = tk.Button(root, text="Reset Results", command=lambda: destroy(listOfLabels))
btn.pack()

print(time.time())

# running the main loop
root.mainloop()

