from databases import Database
from sqlalchemy import DateTime, create_engine, MetaData, Table, Column, Integer, String

DB_URL = "postgresql://root:root@postgres/scraper"

database = Database(DB_URL)
metadata = MetaData()

process = Table (
  "process",
  metadata,
  Column("id", Integer, primary_key=True, index=True),
  Column("start_date", DateTime, index=True, nullable=True),
  Column("end_date", DateTime, index=True,nullable=True),
  Column("timestamp", DateTime, index=True),
  Column("state", String, index=True),
  Column("user_id", String, index=True),
  Column("url", String, nullable=True),
  Column("observation", String,nullable=True),
  Column("content_scraping", String,nullable=True),
  Column("title_scraping", String, nullable=True),
  Column("date_scraping", String, nullable=True),
)

engine = create_engine(DB_URL)
metadata.create_all(engine)
