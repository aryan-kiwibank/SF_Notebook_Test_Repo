from snowflake.snowpark import Session

session = Session.builder.config("connection_name", "personal_db_conn").create()

df = session.table("RAW.CUSTOMER")
df.show(2)

print("Now running sql:")
session.sql("select * from RAW.CUSTOMER limit 5").show(5)
