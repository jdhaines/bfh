from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
bushing = Table('bushing', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('bushingSerial', String(length=20)),
    Column('bushingModel', String(length=20)),
    Column('bushingPlant', String(length=20)),
    Column('bushingFurnace', String(length=40)),
    Column('installationComments', Text),
    Column('startupComments', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bushing'].columns['installationComments'].create()
    post_meta.tables['bushing'].columns['startupComments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bushing'].columns['installationComments'].drop()
    post_meta.tables['bushing'].columns['startupComments'].drop()
