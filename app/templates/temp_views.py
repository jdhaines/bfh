# data extraction page
@app.route("/data_extraction", methods=['GET', 'POST'])
def data_extraction():
    form = singleExtract()

    if request.method == 'POST':
        # top buttons chosen (single bushing)
        if request.form['submit'] in ('Download CSV' or 'Display in Browser'):
            # form entry isn't correct
            if form.validate() is False:
                # Re-show the plants page
                return render_template('data_extraction.html', title="Plants Input"
                                   " Page - Bushing Failure Historian",
                                   form=form)
            # form input is correct, do the database thing
            else:
                # save the bushing serial number
                test_bushing_serial = form.bushingSerial.data

#             # grab data
                lookup = models.Bushing.query.filter_by(
                bushingSerial=test_bushing_serial).first()
                
                # Bushing isn't in the database, throw an error.
                if lookup is None:
                    return render_template('data_extraction.html', title="Plants I"
                                       "nput Page - Bushing Failure Historian",
                                       form=form, noBushing=True)

                # Bushing is in the database, get them the information
                # and process button presses)
                else:
                    # They clicked download single csv
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

                        # start just like option above
                        bushing_serials = []
                        bushing_serials.append(test_bushing_serial)
                        csv_data = writecsvio(bushing_serials)

                        # send csv_data to csvtohtml function and get back html
                        html_stringio = csvtohtml(csv_data)
                        html_data = html_stringio.getvalue()

                        return render_template('display.html',
                                               title="Results Display - Bushing "
                                               "Failure Historian", form=form,
                                               data=Markup(html_data))   
        # bottom buttons chosen (all bushings)
        else:
            # They clicked download all bushings in a csv
            if request.form['submit'] == 'Download All':

                # Grab all the bushings from the database and
                # send it to writecsvio which will return a
                # stringIO object with the contents of the csv
                # file written to it.
                bushing_serials = []
                bushing_list = models.Bushing.query.all()
                for b in bushing_list:
                    bushing_serials.append(b.bushingSerial)
                return 'test'
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

                return render_template('display.html',
                                       title="Results Display - Bushing "
                                       "Failure Historian", form=form,
                                       data=Markup(html_data))
    # request method is GET
    elif request.method == 'GET':
        return render_template('data_extraction.html', title="Plants Input"
                           " Page - Bushing Failure Historian",
                           form=form)