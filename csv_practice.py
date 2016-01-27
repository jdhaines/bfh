from app import models
import csv
from io import StringIO
import json


def writecsv_practice(bushing_serials):
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
        for b in bushing_serials:
            # load the single bushing db info
            bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

            # make the bushing dictionary
            bushing_dict = bushing.__dict__

            # remove the extra sqlalchemy key/value
            del bushing_dict['_sa_instance_state']

            # fix column names
            for d in bushing_dict:
                if d in column_hash.keys():
                    bushing_dict[column_hash[d]] = bushing_dict.pop(d)

            # write the row to the csvfile
            writer.writerow(bushing_dict)

    csvfile.close()
    return colnames


def csvtojson(fieldnames):
    csvfile = open('test.csv', 'r')
    jsonfile = open('file.json', 'w')
    print(fieldnames)
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


def pretty_print_csv(bushing_serials):
    return True


# def gatherCSV(bushing_serials):hing_serials:
    #         # load the single bushing db info
    #         bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

    #         # make the bushing dictionary
    #         bushing_dict = bushing.__dict__

    #         # remove the extra sqlalchemy key/value
    #         del bushing_dict['_sa_instance_state']

    #         # append next row in the array
    #         writer.writerow(bushing_dict)
    #         print(data.read())


def writecsv(bushing_serials):
    """
    Take in a list of bushing serial numbers.  Use that number to query the
    database and get a python dictionary that can be written to a file or
    displayed.
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

    with open('download.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colnames,
                                lineterminator='\n')
        writer.writeheader()
        for b in bushing_serials:
            # load the single bushing db info
            bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

            # make the bushing dictionary
            bushing_dict = bushing.__dict__

            # remove the extra sqlalchemy key/value
            del bushing_dict['_sa_instance_state']

            # fix column names
            for d in bushing_dict:
                if d in column_hash.keys():
                    bushing_dict[column_hash[d]] = bushing_dict.pop(d)

            # write the row to the csvfile
            writer.writerow(bushing_dict)

    csvfile.close()
    # return colnames


def writecsvio(bushing_serials):
    """
    Take in a list of bushing serial numbers.  Use that number to query the
    database and get a python dictionary that can be written to a file or
    displayed.  In this case, save the file to a stringIO object.
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

    csv_data = StringIO()
    writer = csv.DictWriter(csv_data, fieldnames=colnames, lineterminator='\n')
    writer.writeheader()

    for b in bushing_serials:
        # load the single bushing db info
        bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

        # make the bushing dictionary
        bushing_dict = bushing.__dict__

        # remove the extra sqlalchemy key/value
        del bushing_dict['_sa_instance_state']

        # fix column names
        for d in bushing_dict:
            if d in column_hash.keys():
                bushing_dict[column_hash[d]] = bushing_dict.pop(d)

        # write the row to the csvfile
        writer.writerow(bushing_dict)

    return csv_data


def csvtohtml(memory_file):
    """
    Adapted from a snippet found on http://www.ctroms.com/ written by
    Chris Trombley
    """

    # Open the CSV file for reading, and make into a reader object
    memory_file.seek(0)  # who knows why this needs to happen
    reader = csv.reader(memory_file.readlines(), delimiter=',')

    # Create the HTML file for output
    htmlfile = StringIO()

    # initialize rownum variable
    rownum = 0

    # write <table> tag
    htmlfile.write('<table>')

    # generate table contents
    for row in reader:  # Read a single row from the CSV file

        # write header row. assumes first row in csv contains header
        if rownum == 0:
            htmlfile.write('<tr>')  # write <tr> tag
            for column in row:
                htmlfile.write('<th>' + column + '</th>')
            htmlfile.write('</tr>')

        #  write all other rows
        else:
            htmlfile.write('<tr>')
            for column in row:
                htmlfile.write('<td>' + column + '</td>')
            htmlfile.write('</tr>')

        # increment row count
        rownum += 1

    # write </table> tag
    htmlfile.write('</table>')

    return htmlfile

csv_data = writecsvio(['BD017950', 'BD017525', 'asdf'])
htmlfile = csvtohtml(csv_data)
# csv_data = writecsvio(['asdf'])
# print('csv_data', csv_data.getvalue())
print('htmlfile', htmlfile.getvalue())
# csvtojson(colnames)
# end
