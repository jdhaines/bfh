"""Views module for the flask app."""

from flask import render_template, request, make_response, Markup  # flash
from app import app, db, models, pages
from .forms import bushingInfo, bushingSN, singleExtract
import csv
from io import StringIO


# index view function - home page
@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    """Display the home (index) page."""
    return render_template("index.html",
                           title="Bushing Failure Historian",)


# get_sn page
@app.route("/get_sn", methods=['GET', 'POST'])
def get_sn():
    """Display the get_sn page."""
    form = bushingSN()
    form2 = bushingInfo()

    # POST means the user is sending information to the app
    if request.method == 'POST':

        # form input isn't correct
        if form.validate() is False:

            # Re-show the get_sn page
            return render_template("get_sn.html", title="Bushing Lookup",
                                   form=form)

        # form input is correct, do the database thing
        else:

            # save the bushing serial number
            test_bushing_serial = form.bushingSerial.data

            # grab data from the db
            lookup = models.Bushing.query.\
                filter_by(bushingSerial=test_bushing_serial).first()

            # Bushing isn't in the database, send them to enter new data
            if lookup is None:

                # reshow plants page, display new bushing message
                return render_template('plants.html',
                                       title="Plants Input Page - Bushing Fail"
                                       "ure Historian", form=form2,
                                       newBushingEntry=True)

            # Bushing is in the database, send them to edit data & display
            # the known data from the db
            else:

                # reshow plants page, display bushing exists message, and
                # send the bushing data to the page for dispaly in the form
                # fields
                return render_template('plants.html', title="Plants Input Page"
                                       " - Bushing Failure Historian",
                                       form=form2, lookup=lookup,
                                       bushingExists=True)

    # We're simply displaying the page, not getting user input
    elif request.method == 'GET':
        return render_template("get_sn.html", title="Bushing Lookup",
                               form=form)


# plants page
@app.route("/plants", methods=['GET', 'POST'])
def plants():
    """Display the plants page."""
    form = bushingInfo()

    # POST means the user is sending information to the app
    if request.method == 'POST':

        # form input isn't correct
        if form.validate() is False:

            # Re-show the plants page
            return render_template('plants.html', title="Plants Input Page - "
                                   "Bushing Failure Historian", form=form)

        # form input is correct, do the database thing
        else:

            # query the database for bushing details
            test_bushing_serial = form.bushingSerial.data
            lookup = models.Bushing.query.filter_by(
                bushingSerial=test_bushing_serial).first()

            # bushing doesn't exist...add it
            if lookup is None:

                # First, grab the form data and put it in a new bushing object
                new_bushing = models.Bushing(
                    bushingSerial=form.bushingSerial.data,
                    bushingModel=form.bushingModel.data,
                    bushingPlant=form.bushingPlant.data,
                    bushingFurnace=form.bushingFurnace.data,
                    installationComments=form.installationComments.data,
                    startupComments=form.startupComments.data,
                    reason1=form.reason1.data,
                    reason1Comments=form.reason1Comments.data,
                    reason2=form.reason2.data,
                    reason2Comments=form.reason2Comments.data
                )

                # Add it to the database session
                db.session.add(new_bushing)

                # Commit the new bushing to the database
                db.session.commit()

            # bushing exists in the database.
            else:

                # if the form field has data in it, send it to the database
                # overwriting what previously existed
                if form.bushingModel.data:
                    lookup.bushingModel = form.bushingModel.data
                if form.bushingPlant.data:
                    lookup.bushingPlant = form.bushingPlant.data
                if form.bushingFurnace.data:
                    lookup.bushingFurnace = form.bushingFurnace.data
                if form.installationComments.data:
                    lookup.installationComments = \
                        form.installationComments.data
                if form.startupComments.data:
                    lookup.startupComments = form.startupComments.data
                if form.reason1.data:
                    lookup.reason1 = form.reason1.data
                if form.reason1Comments.data:
                    lookup.reason1Comments = form.reason1Comments.data
                if form.reason2.data:
                    lookup.reason2 = form.reason2.data
                if form.reason2Comments.data:
                    lookup.reason2Comments = form.reason2Comments.data

                # Commit the updated bushing to the database
                db.session.commit()

            # Kick the user back to the plants page with sucess flag
            return render_template("plants.html", success=True)

    # We're simply displaying the page, not getting user input
    elif request.method == 'GET':

        # Show the plants page
        return render_template('plants.html', title="Plants Input Page - "
                               "Bushing Failure Historian", form=form)


# documentation page
@app.route("/documentation")
def documentation():
    """Display the documentation page."""
    # display the page without any additional data
    return render_template("documentation.html",
                           title="Documentation - Bushing Failure Historian")


# data extraction page
@app.route("/data_extraction", methods=['GET', 'POST'])
def data_extraction():
    """Display data_extraction page."""
    form = singleExtract()

    # POST means the user is sending information to the app
    if request.method == 'POST':

        # they've pressed one of the top buttons (single bushing)
        if (request.form['submit'] == 'Download CSV' or
                request.form['submit'] == 'Display in Browser'):

            # form entry isn't correct
            if form.validate() is False:

                # Re-show the plants page
                return render_template('data_extraction.html', title="Plants I"
                                       "nput Page - Bushing Failure Historian",
                                       form=form)

            # form input is correct, do the database thing
            else:
                # query the database for bushing details
                test_bushing_serial = form.bushingSerial.data
                lookup = models.Bushing.query.filter_by(
                    bushingSerial=test_bushing_serial).first()

                # Bushing isn't in the database
                if lookup is None:

                    # reshow data_extraction page, but pass key to show no
                    # bushing error
                    return render_template('data_extraction.html', title="Plan"
                                           "ts Input Page - Bushing Failure Hi"
                                           "storian", form=form,
                                           noBushing=True)

                # Bushing is in the database, get them the information
                # and process button presses)
                else:

                    # They clicked download single csv button
                    if request.form['submit'] == 'Download CSV':

                        # grab the bushingSN they put in the form and
                        # send it to writecsvio which will return a
                        # stringIO object with the contents of the csv
                        # file written to it.
                        bushing_serials = []
                        bushing_serials.append(test_bushing_serial)
                        csv_data = writecsvio(bushing_serials)

                        # make the response, prepare the file, and send
                        # for download
                        output = make_response(csv_data.getvalue())
                        output.headers["Content-Disposition"] = \
                            "attachment; filename=download.csv"
                        output.headers["Content-type"] = "text/csv"
                        return output

                    # They clicked display single bushing in browser
                    else:  # request.form['submit'] == 'Display in Browser':

                        # grab the bushingSN they put in the form and
                        # send it to writecsvio which will return a
                        # stringIO object with the contents of the csv
                        # file written to it.
                        bushing_serials = []
                        bushing_serials.append(test_bushing_serial)
                        csv_data = writecsvio(bushing_serials)

                        # send csv_data to csvtohtml function and get back html
                        html_stringio = csvtohtml(csv_data)
                        html_data = html_stringio.getvalue()

                        # show display page and send the html data we just got
                        return render_template('display.html',
                                               title="Results Display - Bushin"
                                               "gFailure Historian", form=form,
                                               data=Markup(html_data))

        # bottom buttons chosen (all bushings).  This section mostly needed
        # because these buttons don't need the form to validate.
        else:

            # They clicked download all bushings in a csv
            if request.form['submit'] == 'CSV':

                # Grab all the bushings from the database and
                # send it to writecsvio which will return a
                # stringIO object with the contents of the csv
                # file written to it.
                bushing_serials = []
                bushing_list = models.Bushing.query.all()
                for b in bushing_list:
                    bushing_serials.append(b.bushingSerial)
                csv_data = writecsvio(bushing_serials)

                # make the response, prepare the file, and send
                # for download
                output = make_response(csv_data.getvalue())
                output.headers["Content-Disposition"] = \
                    "attachment; filename=download.csv"
                output.headers["Content-type"] = "text/csv"
                return output

            # They clicked display all bushings in a csv
            else:  # request.form['submit'] == 'Display All':

                # start just like option above
                bushing_serials = []
                bushing_list = models.Bushing.query.all()
                for b in bushing_list:
                    bushing_serials.append(b.bushingSerial)
                csv_data = writecsvio(bushing_serials)

                # send csv_data to csvtohtml function and get back html
                html_stringio = csvtohtml(csv_data)
                html_data = html_stringio.getvalue()

                # show display page and send the html data we just got
                return render_template('display.html',
                                       title="Results Display - Bushing "
                                       "Failure Historian", form=form,
                                       data=Markup(html_data))

    # request method is GET, simply show the page
    elif request.method == 'GET':

        # show the data_extraction page
        return render_template('data_extraction.html', title="Plants Input"
                               " Page - Bushing Failure Historian",
                               form=form)


@app.route("/display.html")
def display(data):
    """
    Show the display page with bushing data passed to it.

    mostly this will be called from the data_extraction page, not directly
    from a link
    """
    return render_template('display.html',
                           title="Data Display - Bushing Failure Historian",
                           data=data)


@app.route('/<path:path>/')
def page(path):
    """Send static file will guess the correct MIME type."""
    page = pages.get_or_404(path)
    return render_template('page.html', page=page, pages=pages)


def writecsvio(bushing_serials):
    """
    Take list of bushing serial numbers, output stringIO with csv data.

    Take in a list of bushing serial numbers.  Use that number to query the
    database and get a python dictionary that can be written to a file or
    displayed.  In this case, save the file to a stringIO object.
    """
    # get column names from db
    fieldnames = [m.key for m in models.Bushing.__table__.columns]

    # convert between database entry id and human readable field names
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

    # get column names in order using the hash conversion
    colnames = []
    for f in fieldnames:
        colnames.append(column_hash[f])

    # make a new StringIO object (file-like memory object)
    csv_data = StringIO()

    # start up the csv writer which will write csv data into the StringIO
    # object
    writer = csv.DictWriter(csv_data, fieldnames=colnames)

    # write the first line of column headers
    writer.writeheader()

    # load the bushings from the list of serials.  this works whether we pass
    # a single bushingSN or multiple.
    for b in bushing_serials:
        bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

        # make the dictionary which will be written into csv format
        bushing_dict = bushing.__dict__

        # remove the extra sqlalchemy key/value that is always present
        del bushing_dict['_sa_instance_state']

        # fix column names using column_hash for all of the names in the
        # dictionary
        for d in bushing_dict:
            if d in column_hash.keys():
                bushing_dict[column_hash[d]] = bushing_dict.pop(d)

        # write the row to the csvfile
        writer.writerow(bushing_dict)

    return csv_data


def csvtohtml(memory_file):
    """
    Take in stringIO csv and output stringIO with html.

    Adapted from a snippet found on http://www.ctroms.com/ written by
    Chris Trombley.  Pass in a StringIO memory file with csv data... generally
    one that was created by the writecsvio function above.  We'll get another
    stringIO object with html table data which can be plugged into a page to
    produce a table.
    """
    # Open the CSV file for reading, and make into a reader object
    memory_file.seek(0)  # who knows why this needs to happen, but it does
    reader = csv.reader(memory_file.readlines(), delimiter=',')

    # Create the HTML file for output
    htmlfile = StringIO()

    # initialize rownum & colnum variable
    rownum = 0
    colnum = 0

    # write opening <table> tag
    htmlfile.write('<table>')

    # generate table contents
    for row in reader:  # Read a single row from the CSV file

        # write header row. assumes first row in csv contains header.  Also
        # put classes into each column so we can size them.
        if rownum == 0:
            htmlfile.write('<tr class="first_row">')  # write <tr> tag
            colnum = 0
            for column in row:
                htmlfile.write('<th class=col_' + str(colnum) + '>' + column +
                               '</th>')
                colnum += 1
            htmlfile.write('</tr>')

        # write all other odd rows and add an odd class so we can style
        # every other row pretty.  Also put classes into each column so
        # we can size them.
        elif rownum % 2 == 1:
            htmlfile.write('<tr class="odd_row">')
            colnum = 0
            for column in row:
                htmlfile.write('<td class=col_' + str(colnum) + '>' + column +
                               '</td>')
                colnum += 1
            htmlfile.write('</tr>')

        # write all other even rows and add an even class so we can style
        # every other row pretty.  Also put classes into each column so we
        # can size them.
        else:
            htmlfile.write('<tr class="even_row">')
            colnum = 0
            for column in row:
                htmlfile.write('<td class=col_' + str(colnum) + '>' + column +
                               '</td>')
                colnum += 1
            htmlfile.write('</tr>')

        # increment row count
        rownum += 1

    # write close </table> tag
    htmlfile.write('</table>')

    return htmlfile

# end
