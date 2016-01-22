from flask.ext.wtf import Form
from wtforms import StringField, SelectField  # , RadioField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class bushingInfo(Form):
    # Bushing Information Section
    bushingSerial = StringField(u'Bushing S/N',
        validators=[DataRequired('Please enter a serial number (ex. BD012345)')])
    submit = SubmitField("Lookup")
    bushingModel = SelectField(u'Bushing Model',
        # validators=[DataRequired('Please select a bushing model from the drop-down box')],
        choices=[
                 ('', 'Select one...'),
                 ('D41T-147', 'D41T-147'),
                 ('D42S-340', 'D42S-340'),
                 ('D42T-345', 'D42T-345'),
                 ('D44T-340', 'D44T-340'),
                 ('D48S-300', 'D48S-300'),
                 ('D48T-300', 'D48T-300'),
                 ('D48T-380', 'D48T-380'),
                 ('D34-130', 'D34-130'),
                 ('D34-185', 'D34-185'),
                 ('D34-205', 'D34-205'),
                 ('D34-220', 'D34-220'),
                 ('D48-260', 'D48-260'),
                 ('D48-375', 'D48-375'),
                 ('D34-140', 'D34-140'),
                 ('D34-250', 'D34-250'),
                 ('D40-315', 'D40-315'),
                 ('D45-125', 'D45-125')
        ])
    bushingPlant = SelectField(u'Bushing Plant',
        # validators=[DataRequired('Please select a bushing plant from the drop-down box.')],
        choices=[
                 ('', 'Select one...'),
                 ('Cleburne', 'Cleburne'),
                 ('Etowah', 'Etowah'),
                 ('Waterville', 'Waterville')
        ])
    bushingFurnace = SelectField(u'Bushing Furnace',
        # validators=[DataRequired('Please select a bushing furnace from the drop-down box.')],
        choices=[
                 ('', 'Select one...'),
                 ('1901 (Cleburne)', '1901 (Cleburne)'),
                 ('3303 (Etowah)', '3303 (Etowah)'),
                 ('3304 (Etowah)', '3304 (Etowah)'),
                 ('9211 (Waterville)', '9211 (Waterville)'),
                 ('9212 (Waterville)', '9212 (Waterville)')
        ])
    # Installation Section
    # installationIssues = RadioField(u'Installation Issues',
    #     choices=[
    #             ('Yes', 'Yes'),
    #             ('No', 'No')
    #     ])
    # installationComments = TextAreaField(u'Installation Comments')

    # Submit Button
    submit = SubmitField("Submit")


class bushingSN(Form):
    bushingSerial = StringField(u'Bushing S/N',
        validators=[DataRequired('Please enter a serial number (ex. BD012345)')])
    submit = SubmitField("Lookup")

# end
