from liquibase.diff import changelog
from liquibase.update import sql

changes = changelog()
sql = sql(changes).decode("utf-8") 

print(sql)
