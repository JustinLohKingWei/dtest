import csv
from .pipeline import average,check_diabetes,clean

def dtest(fileInput,fileOutput):
    # create an output file
    outfile = open(fileOutput, 'w')
    outfile_header = "patient_id, glucose_test1, glucose_test2, glucose_test3, average_glucose, diagnostic\n"
    outfile.write(outfile_header)

    # open input file and parse data
    with open(fileInput, 'r', encoding='ISO-8859-1')as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        for row in reader:
            patient_id = row[0]
            glucose_t1 = row[5]
            glucose_t2 = row[6]
            glucose_t3 = row[7]
        # find average of provided blood sugar values
            glucose_average = average(glucose_t1, glucose_t2, glucose_t3)
        # generate results based on average
            diagnostic = check_diabetes(glucose_average)
        # clean data
            cleaned_glucose_t1 = clean(glucose_t1)
            print(cleaned_glucose_t1)
            cleaned_glucose_t2 = clean(glucose_t2)
            print(cleaned_glucose_t1)
            cleaned_glucose_t3 = clean(glucose_t3)
            print(cleaned_glucose_t1)
            line = "{},{},{},{},{},{}\n".format(patient_id, cleaned_glucose_t1, cleaned_glucose_t2, cleaned_glucose_t3, glucose_average, diagnostic)
            outfile.write(line)
    outfile.close
    


