from app import models
import csv
from io import StringIO
import json


def writeCSV(bushingSerials):
    """
    Take in a list of bushing serial numbers.  Use that number to query the database
    and get a python dictionary that can be written to a file or displayed.
    """

    # get column names from db
    fieldnames = [m.key for m in models.Bushing.__table__.columns]

    # get column names directly
    column_hash = {
        'id': 'ID',
        'bushingSerial': 'Serial',
        'bushingModel': 'Model',
        'bushingPlant': 'Plant',
        'bushingFurnace': 'Furnace',
        'installationComments': 'Install Comments',
        'startupComments': 'StartUp Comments',
        'reason1': 'Failure Reason 1',
        'reason1Comments': 'Comments1',
        'reason2': 'Failure Reason 2',
        'reason2Comments': 'Comments2'
    }

    # get column names in order
    colnames = []
    for f in fieldnames:
        colnames.append(column_hash[f])

    with open('test.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colnames,
                                lineterminator='\n')
        writer.writeheader()
        for b in bushingSerials:
            # load the single bushing db info
            bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

            # make the bushing dictionary
            bushingDict = bushing.__dict__

            # remove the extra sqlalchemy key/value
            del bushingDict['_sa_instance_state']

            # fix column names
            for d in bushingDict:
                if d in column_hash.keys():
                    bushingDict[column_hash[d]] = bushingDict.pop(d)

            # write the row to the csvfile
            writer.writerow(bushingDict)

    csvfile.close()
    return colnames


def csvtojson(fieldnames):
    csvfile = open('test.csv', 'r')
    jsonfile = open('file.json', 'w')

    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    csvfile.close()
    jsonfile.close()


def csvtoxml():
    csvFile = 'test.csv'
    xmlFile = 'test.xml'

    csvData = csv.reader(open(csvFile))
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlData.write('<csv_data>' + "\n")

    rowNum = 0
    for row in csvData:
        if rowNum == 0:
            tags = row
            # replace spaces w/ underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else:
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>'
                              + row[i] + '</' + tags[i] + '>' + "\n")
            xmlData.write('</row>' + "\n")

        rowNum += 1

    xmlData.write('</csv_data>' + "\n")
    xmlData.close()


def prettyPrintCSV(bushingSerials):
    return True

# def gatherCSV(bushingSerials):
    # """
    # Take in a list of bushing serial numbers.  Use that number to query the
    # database and get a python dictionary. Return a single variable with an
    # array of strings to be displayed.
    # """

    # # get column names
    # fieldnames = [m.key for m in models.Bushing.__table__.columns]

    # # add fieldnames as the first string in the array
    # data = StringIO()
    # writer = csv.DictWriter(data, fieldnames=fieldnames,
    #                         lineterminator='\n')
    # writer.writeheader()
    # for b in bushingSerials:
    #         # load the single bushing db info
    #         bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

    #         # make the bushing dictionary
    #         bushingDict = bushing.__dict__

    #         # remove the extra sqlalchemy key/value
    #         del bushingDict['_sa_instance_state']

    #         # append next row in the array
    #         writer.writerow(bushingDict)
    #         print(data.read())

colnames = writeCSV(['BD017950', 'BD017525', 'asdf'])
csvtoxml()
# end
