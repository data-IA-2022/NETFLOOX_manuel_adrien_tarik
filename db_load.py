import mydbconnection as mdbcon
import sqlalchemy
# Connect to the database using an SSH tunnel
conn = mdbcon.connect_to_db('config.yaml', 'mysql_azure_netfloox')

# # Connect to the database directly
# conn = mdbcon.connect_to_db('config.ini', 'mydb', ssh=False)

res = conn.execute('''
 CREATE TABLE netfloox_db.``;
 '''
)

print(res)