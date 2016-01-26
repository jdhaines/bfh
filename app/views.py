from flask import render_template, request, flash, make_response
from app import app, db, models
from .forms import bushingInfo, bushingSN, extract
from io import StringIO
# from csv import writer


# index view function
@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html",
                           title="Bushing Failure Historian",)


# get_sn page
@app.route("/get_sn", methods=['GET', 'POST'])
def get_sn():
    form = bushingSN()
    form2 = bushingInfo()
    if request.method =='POST':
        # form input isn't correct
        if form.validate() == False:

            # Re-show the get_sn page
            return render_template("get_sn.html", title="Bushing Lookup",
                                   form=form)
        # form input is correct, do the database thing
        else:
            # save the bushing serial number
            testbushingSerial = form.bushingSerial.data

            # grab data
            lookup = models.Bushing.query.filter_by(bushingSerial=testbushingSerial).first()
            if lookup == None:
                # Bushing isn't in the database, send them to enter new data
                return render_template('plants.html',
                        title="Plants Input Page - Bushing Failure Historian",
                        form=form2, newBushingEntry=True)
            else:
                # Bushing is in the database, send them to edit data & display
                # the known data from the db
                return render_template('plants.html',
                        title="Plants Input Page - Bushing Failure Historian",
                        form=form2, lookup=lookup, bushingExists=True)

    elif request.method =='GET':
        return render_template("get_sn.html", title="Bushing Lookup",
                                   form=form)


# plants page
@app.route("/plants", methods=['GET', 'POST'])
def plants():
    form = bushingInfo()
    if request.method == 'POST':
        if form.validate() == False:

            # Re-show the plants page
            return render_template('plants.html',
                        title="Plants Input Page - Bushing Failure Historian",
                        form=form)
        else:
            # Store the bushing data to the database

            testbushingSerial = form.bushingSerial.data

            lookup = models.Bushing.query.filter_by(bushingSerial=testbushingSerial).first()

            if lookup == None:  # bushing doesn't exist...add it
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
            else:  # bushing exists, update it
                if form.bushingModel.data:
                    lookup.bushingModel = form.bushingModel.data
                if form.bushingPlant.data:
                    lookup.bushingPlant = form.bushingPlant.data
                if form.bushingFurnace.data:
                    lookup.bushingFurnace = form.bushingFurnace.data
                if form.installationComments.data:
                    lookup.installationComments = form.installationComments.data
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
    elif request.method == 'GET':
        return render_template("plants.html",
                        title="Plants Input Page - Bushing Failure Historian",
                        form=form)


# documentation page
@app.route("/documentation")
def documentation():
    return render_template("documentation.html",
                           title="Documentation - Bushing Failure Historian")


# data extraction page
@app.route("/data_extraction", methods=['GET', 'POST'])
def data_extraction():
    form = extract()
    return render_template("data-extraction.html",
                           title="Data Extraction - Bushing Failure Historian",
                           form=form)
    if request.method =='POST':
        # form input isn't correct
        if form.validate() == False:

            # Re-show the get_sn page
            return render_template("data-extraction.html",
                           title="Data Extraction - Bushing Failure Historian",
                           form=form)
        # form input is correct, do the database thing
        else:
            # save the bushing serial number
            testbushingSerial = form.bushingSerial.data

            # grab data
            lookup = models.Bushing.query.filter_by(bushingSerial=testbushingSerial).first()
            if lookup == None:
                # Bushing isn't in the database, throw an error.
                return render_template('plants.html',
                        title="Plants Input Page - Bushing Failure Historian",
                        form=form, noBushing=True)
            # else:
            #     # Bushing is in the database, get them the information
            #     if request.form['singleButton'] == 'Download CSV':
            #         # They clicked download csv
                    

            #     else:
            #         # They clicked display in browser
            #         return render_template('display.html',
            #             title="Plants Input Page - Bushing Failure Historian"
            #               data=data)


@app.route("/display.html")
def display(data):
    return render_template('display.html',
                           title="Data Display - Bushing Failure Historian",
                           data=data)


def writeCSV(bushingSerials):
    """
    Take in a list of bushing serial numbers.  Use that number to query the database
    and get a python dictionary that can be written to a file or displayed.
    """

    # get column names
    fieldnames = [m.key for m in models.Bushing.__table__.columns]

    with open('test.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                lineterminator='\n')
        writer.writeheader()
        for b in bushingSerials:
            # load the single bushing db info
            bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

            # make the bushing dictionary
            bushingDict = bushing.__dict__

            # remove the extra sqlalchemy key/value
            del bushingDict['_sa_instance_state']

            # write the row to the csvfile
            writer.writerow(bushingDict)

    csvfile.close()


def gatherCSV(bushingSerials):
    """
    Take in a list of bushing serial numbers.  Use that number to query the
    database and get a python dictionary. Return a single variable with an
    array of strings to be displayed.
    """

    # get column names
    fieldnames = [m.key for m in models.Bushing.__table__.columns]
    for b in bushingSerials:
            # load the single bushing db info
            bushing = models.Bushing.query.filter_by(bushingSerial=b).first()

            # make the bushing dictionary
            bushingDict = bushing.__dict__

            # remove the extra sqlalchemy key/value
            del bushingDict['_sa_instance_state']
# end
