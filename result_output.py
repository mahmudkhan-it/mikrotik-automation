import csv
#file
def outputToCSV(output):
    with open('output.csv', 'w', newline='') as file:
        outputFile = csv.writer(file)
        field = ["IP", "NAME", "STATUS"]
        outputFile.writerow(field)
        for e in output:
            outputFile.writerow(e)

