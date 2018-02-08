import paramiko

def deploy(key = 'key/test_key.pem', server_ip = None, prefix = None):
    '''
    key - ssh key to login into the server
    server_ip - ip address of the server
    prefix - prefix of the associated file
    '''
    # Create a client object
    client = paramiko.client.SSHClient()
    # Autoaddkey if not available
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    # Connect to the server
    client.connect(server_ip, pkey = paramiko.RSAKey.from_private_key_file(key), username='testtest')
    # Execute command to clone repository
    print 'Connected to server'
    # Check if repository exists
    stdin, stdout, stderr = client.exec_command('cd data_ingestion_system')
    if stderr.read() != '':
        # Clone repository if not present
        print 'Cloning repository'
        stdin, stdout, stderr = client.exec_command('git clone https://github.com/vinnsvinay/data_ingestion_system')
    else:
        # Pull repository if present
        print 'Pulling repository'
        stdin, stdout, stderr = client.exec_command('cd data_ingestion_system; git pull')
    # Adding a crontab
    stdin, stdout, stderr = client.exec_command('crontab -l > json_cron')
    cron_command = 'echo "* * * * * python /home/testtest/data_ingestion_system/json_parser.py {}" \
                            >> json_cron'.format(prefix)
    stdin, stdout, stderr = client.exec_command(cron_command)
    stdin, stdout, stderr = client.exec_command('crontab json_cron')
    print('Running cronjob')
    

server_ip = '52.89.29.79'
key = '/home/vinay/Documents/AWS_keys/test_key.pem'

deploy(key, server_ip, prefix = 'sample')