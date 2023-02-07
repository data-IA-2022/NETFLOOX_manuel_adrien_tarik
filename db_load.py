import mydbconnection as mdbcon
import sqlalchemy
# Connect to the database using an SSH tunnel
conn = mdbcon.connect_to_db('C:\\Users\\tarik\\OneDrive\\Documents\\Formation_Dév_IA\\Projet_Netfloox\\config.ini', 'DB_NETFLOOX_MAT', ssh=False, local_port=3308, remote_port=3306,section='mysql_azure_netfloox', ssh_section='ssh_tunnel')

# # Connect to the database directly
# conn = mdbcon.connect_to_db('config.ini', 'mydb', ssh=False)

res = conn.execute('''
 SHOW DATABASES;
 '''
)

print(res)