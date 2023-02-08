import yaml
import paramiko
from sqlalchemy import create_engine


def connect_to_db(config_file, section, ssh=False, local_port=None, ssh_section=None):
    # Read configuration information from file
    config = yaml.safe_load(config_file)

    if ssh:
        ssh_config = config[ssh_section]['user']
        # Connect to database using SSH tunnel
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_config['host'], ssh_config['port'], ssh_config['user'], ssh_config['password'])

        if local_port:
            config[section]['port'] = local_port

    # Connect to database using SQLAlchemy
    engine = create_engine('{type}://{user}:{password}@{host}:{port}/{db_name}'.format(**config[section]))
    return engine.connect()
