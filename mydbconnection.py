import configparser
import os
import paramiko
import psycopg2
import pymongo
from sqlalchemy import create_engine

def connect_to_db(config_file, db_name, ssh=False, local_port=None, remote_port=None,section=None, ssh_section=None):
    # Read configuration information from file
    config = configparser.ConfigParser()
    config.read(config_file)
    section = section
    user = config[section]['user']
    password = config[section]['password']
    host = config[section]['host']
    port = config[section].getint('port')
    if remote_port:
        port = remote_port
    db_type = config[section]['type']
    
    if ssh:
        # Read configuration information from file
        config = configparser.ConfigParser()
        config.read(config_file)
        ssh_section = ssh_section
        user_ssh = config[ssh_section]['user']
        password_ssh = config[ssh_section]['password']
        host_ssh = config[ssh_section]['host']
        port_ssh = config[ssh_section].getint('port')
        # Connect to database using SSH tunnel
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host_ssh, username=user_ssh, password=password_ssh)

        # Forward a local port to the remote database server
        transport = ssh.get_transport()
        dest_addr = (host, port)
        if local_port:
            local_port = local_port
        else:
            local_port = port
        local_addr = ('localhost', local_port)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        host = host
        port = local_port
    
    if db_type == 'postgresql':
        # Connect to PostgreSQL database using SQLAlchemy
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
        conn = engine.connect()
        return conn
    elif db_type == 'mysql':
        # Connect to MySQL database using SQLAlchemy
        engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{db_name}')
        conn = engine.connect()
        return conn
    elif db_type == 'mongodb':
        # Connect to MongoDB database
        client = pymongo.MongoClient(f'mongodb://{user}:{password}@{host}:{port}/')
        return client[db_name]
    else:
        raise ValueError(f"Unsupported database type: {db_type}")