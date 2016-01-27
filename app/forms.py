from flask.ext.wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class bushingInfo(Form):
    # Bushing Information Section
    bushingSerial = StringField(u'Bushing S/N',
        validators=[DataRequired('Please enter a serial number (ex. BD012345)')])
    # submit = SubmitField("Lookup")
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
    installationComments = TextAreaField(u'Installation Comments')
    startupComments = TextAreaField(u'Installation Comments')
    # Primary Failure Mode Section
    reason1 = SelectField(u'Primary Reason',
        # validators=[DataRequired('')],
        choices=[
                ('', 'Select one...'),
                ('Glass Leak', 'Glass Leak'),
                ('Damaged Tips', 'Damaged Tips'),
                ('Leaking Tips', 'Leaking Tips'),
                ('Ceramic in Tips', 'Ceramic in Tips'),
                ('Global Sag', 'Global Sag'),
                ('Localized Sag', 'Localized Sag'),
                ('Flood', 'Flood'),
                ('Devitrification', 'Devitrification'),
                ('Poor Performance', 'Poor Performance'),
                ('Damaged Tip Plate', 'Damaged Tip Plate'),
                ('Profile', 'Profile'),
                ('Ear Burned Off', 'Ear Burned Off'),
                ('Leaking Cooling Tube', 'Leaking Cooling Tube'),
                ('Thermocouple Failure', 'Thermocouple Failure'),
                ('Cooling Ring Failure', 'Cooling Ring Failure'),
                ('Damaged Supports', 'Damaged Supports'),
                ('Contamination', 'Contamination'),
                ('Product/Process Change', 'Product/Process Change'),
                ('Rebuild', 'Rebuild'),
                ('Curtailment', 'Curtailment'),
                ('Experimental', 'Experimental'),
                ('No Damage Identified', 'No Damage Identified')
        ])
    reason1Comments = TextAreaField(u'Primary Reason Comments')
    # Secondary Failure Mode Section
    reason2 = SelectField(u'Secondary Reason',
        # validators=[DataRequired('')],
        choices=[
                ('', 'Select one...'),
                ('Glass Leak', 'Glass Leak'),
                ('Damaged Tips', 'Damaged Tips'),
                ('Leaking Tips', 'Leaking Tips'),
                ('Ceramic in Tips', 'Ceramic in Tips'),
                ('Global Sag', 'Global Sag'),
                ('Localized Sag', 'Localized Sag'),
                ('Flood', 'Flood'),
                ('Devitrification', 'Devitrification'),
                ('Poor Performance', 'Poor Performance'),
                ('Damaged Tip Plate', 'Damaged Tip Plate'),
                ('Profile', 'Profile'),
                ('Ear Burned Off', 'Ear Burned Off'),
                ('Leaking Cooling Tube', 'Leaking Cooling Tube'),
                ('Thermocouple Failure', 'Thermocouple Failure'),
                ('Cooling Ring Failure', 'Cooling Ring Failure'),
                ('Damaged Supports', 'Damaged Supports'),
                ('Contamination', 'Contamination'),
                ('Product/Process Change', 'Product/Process Change'),
                ('Rebuild', 'Rebuild'),
                ('Curtailment', 'Curtailment'),
                ('Experimental', 'Experimental'),
                ('No Damage Identified', 'No Damage Identified')
        ])
    reason2Comments = TextAreaField(u'Secondary Reason Comments')

    # Submit Button
    submit = SubmitField(u"Submit")


class bushingSN(Form):
    bushingSerial = StringField(u'Bushing S/N',
      validators=[DataRequired('Please enter a serial number (ex. BD012345)')])
    submit = SubmitField("Lookup")


class singleExtract(Form):
    bushingSerial = StringField(u'Bushing S/N',
      validators=[DataRequired('Please enter a serial number (ex. BD012345)')])
    submit = SubmitField(u'Button')

# end
