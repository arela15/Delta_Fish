from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
carrito__producto = Table('carrito__producto', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_carrito', Integer),
    Column('id_producto', Integer),
    Column('cantidad', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['carrito__producto'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['carrito__producto'].drop()
