import mydbconnection as mdbcon
from sqlalchemy import text
# Connect to the database using an SSH tunnel
conn = mdbcon.connect_to_db('config.yaml', 'mysql_azure_netfloox')

# # Connect to the database directly
# conn = mdbcon.connect_to_db('config.ini', 'mydb', ssh=False)

res = conn.execute(text('''
 CREATE TABLE `netfloox_db`.`toto`(
  `id_toto` VARCHAR(50) NOT NULL,
  `first` VARCHAR(45) NULL,
  `last` VARCHAR(45) NULL,
  `codes` VARCHAR(10) NULL,
  PRIMARY KEY (`id_toto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
 ''')
)

print(res)