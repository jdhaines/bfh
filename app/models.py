"""Describe the Bushing class for the bushing historian app."""
from app import db


class Bushing(db.Model):
    """Database models for bushing historian."""

    id = db.Column(db.Integer, primary_key=True)
    bushingSerial = db.Column(db.String(20), index=True)
    bushingModel = db.Column(db.String(20), index=True)
    bushingPlant = db.Column(db.String(20), index=True)
    bushingFurnace = db.Column(db.String(40), index=True)
    installationComments = db.Column(db.Text, index=True)
    startupComments = db.Column(db.Text, index=True)
    reason1 = db.Column(db.String(40), index=True)
    reason1Comments = db.Column(db.Text, index=True)
    reason2 = db.Column(db.String(40), index=True)
    reason2Comments = db.Column(db.Text, index=True)

    def __repr__(self):
        """Explain how to display the class."""
        return '<Bushing %s (%s)>' % (self.bushingSerial, self.bushingModel)

# end
