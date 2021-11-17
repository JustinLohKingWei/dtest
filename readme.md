# Dtest Summary
 Dtest is a python CLI application which reads a .csv file input of medical records , deduces diagnostic results based on the data, and outputs it to another .csv file .

# Installation guide
 1. Have at least python 2 installed. 
 2. Clone and access the repository via a terminal. 
 3. Run **$ pip install -e.** to install the application

 # Usage
## Reading and Writing to a file
1. Use **dtest -i inputFileName -o outputFileName** to read the file **inputFilename** and write the results to **outputFilename**
## Running Unit tests
1. Use **dtest -t -i -o** to excute all unit tests found in the directory


 # Uninstallation guide
 1. Remove the application using **$ pip uninstall -e.**


# Assumptions taken

- If an invalid value is detected in any of the three tests, only the average between the valid values are computed
- The highest blood sugar level survived by a human is 2656 mg/dl according to this [source](https://www.guinnessworldrecords.com/world-records/highest-blood-sugar-level/?fb_comment_id=811257658947726_974655159274641) , therefore we assume any inputs above this value as faulty and not to be considered.
- We shall also assume that a blood glucose level can be exceedingly low in a person , but not zero at any given time
- Only 3 tests exactly are expected. And format of the given patient data is not subject to change.
- Encoding of received csv files are that of 'ISO-8859-1'
- Only a display of 2 decimal places is required

