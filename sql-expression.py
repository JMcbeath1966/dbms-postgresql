from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = (
    "Artist", meta,
)

with db.connect() as connection: