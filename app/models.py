from app import db


class Bushing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bushingSerial = db.Column(db.String(20), index=True)
    bushingModel = db.Column(db.String(20), index=True)
    bushingPlant = db.Column(db.String(20), index=True)
    bushingFurnace = db.Column(db.String(40), index=True)

    def __repr__(self):
        return '<Bushing %s (%s)>' % (self.bushingSerial, self.bushingModel)

# end
