from snowflake.snowpark import Session

session = Session.builder.config("connection_name", "personal_db_conn").create()

df = session.table("RAW.TEST_TOPIC_V1__RAW")
df.show(2)

print("Now running sql:")
session.sql("select * from RAW.TEST_TOPIC_V1__RAW limit 5").show(5)
