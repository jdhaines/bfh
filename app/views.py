from flask import render_template, request, flash  # , redirect
from app import app, db, models
from .forms import bushingInfo, bushingSN


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
                        startupComments=form.startupComments.data)

                # Add it to the database session
                db.session.add(new_bushing)

                # Commit the new bushing to the database
                db.session.commit()
            else:  # bushing exists, update it
                # return form.bushingModel.data
                if form.bushingModel.data:
                    lookup.bushingModel = form.bushingModel.data
                if form.bushingPlant.data:
                    lookup.bushingPlant = form.bushingPlant.data
                if form.bushingFurnace.data:
                    lookup.bushingFurnace = form.bushingFurnace.data

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

# end
