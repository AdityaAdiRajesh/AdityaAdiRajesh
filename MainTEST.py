def ReadFirstHalfOfFile(charachterString,numOfNum,filename,full_path,reportSINInfo):
    setOfValaues = []
    setOfSin = []
    acceptedStringNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    acceptedNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for values in charachterString:
        for charachters in values:
            setOfValaues.append(charachters)

            if charachters in acceptedStringNum or charachters in acceptedNum:
                numOfNum += 1
    print(f"Number of numbers in the file: {numOfNum}")

    if numOfNum >= 9:
        returnValue = checkForSin(setOfValaues, setOfSin)
        print(f"SIN Found: {returnValue}")
        if returnValue == True:
            reportFile = open('Report Generation File', 'a')
            mainReportFile = open("Full Report Genertation", 'a')
            SINInfo = f"SIN found in {filename}, Full Path: {full_path}"
            if SINInfo not in reportSINInfo:
                numpy.append(reportSINInfo, f"SIN found in {filename}, Full Path: {full_path}")
                mainReportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                reportFile.write(f"SIN found in {filename}, Full Path: {full_path}\n")
                reportFile.close()
                mainReportFile.close()
            else:
                mainReportFile.close()
                reportFile.close()




    else:
        print("No SIN Found")

def readAndProcess(fileTypeSpesific,filename,full_path,reportSINInfo):
    # THIS CHUNK OF CODE PROCESSES PDF DOCUMENTS
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

            maxIndexOfLIST = len(charachterString)-1
            halfIndexmark = maxIndexOfLIST//2

            ReadFirstHalfOfFile(charachterString[halfIndexmark:],numOfNum,filename,full_path,reportSINInfo)

        else:
            print(f"PDF is empty: {full_path}")
    # THIS IS THE END OF THE PDF PROCESSING CODE
    # elif fileTypeSpesific[0].strip() == "txt":
    elif str(filename).split('.')[1] == 'txt':
        # ____ FILE IS READ AS EMPTY FIX RN =(
        fileToRead = open(full_path, 'r')
        lineOfInfoStored = fileToRead.readlines()
        acceptedStringNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.', ' ', '/']
        acceptedNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        setOfValuesThatWork = []
        returnList = []
        for values in lineOfInfoStored:

            if len(values) >= 1:
                for charachters in values:
                    if charachters in acceptedStringNum or charachters in acceptedNum:
                        setOfValuesThatWork.append(charachters)
                        if len(setOfValuesThatWork) >= 9:
                            strippedSIN = []
                            for char in setOfValuesThatWork:
                                if char in acceptedNum:
                                    strippedSIN.append(char)
                            returnVal = checkForSin(strippedSIN, returnList)
                            print(f"SIN FOUND: {returnVal}")
                            if returnVal == True:
                                reportFile = open('Report Generation File', 'a')
                                mainReportFile = open("Full Report Genertation", 'a')
                                SINInfo = f"SIN found in {filename}, Full Path: {full_path}"
                                if SINInfo not in reportSINInfo:
                                    numpy.append(reportSINInfo, f"SIN found in {filename}, Full Path: {full_path}")
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
