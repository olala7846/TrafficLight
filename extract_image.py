import csv

CSV_FILE = 'dayTraining/dayClip1/frameAnnotationsBULB.csv'
with open(CSV_FILE, 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        for key, val in row.iteritems():
            print('{}: {}'.format(key, val))
        break



