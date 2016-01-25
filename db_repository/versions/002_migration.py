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
    Column('reason1', String(length=40)),
    Column('reason1Comments', Text),
    Column('reason2', String(length=40)),
    Column('reason2Comments', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bushing'].columns['reason1'].create()
    post_meta.tables['bushing'].columns['reason1Comments'].create()
    post_meta.tables['bushing'].columns['reason2'].create()
    post_meta.tables['bushing'].columns['reason2Comments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bushing'].columns['reason1'].drop()
    post_meta.tables['bushing'].columns['reason1Comments'].drop()
    post_meta.tables['bushing'].columns['reason2'].drop()
    post_meta.tables['bushing'].columns['reason2Comments'].drop()
