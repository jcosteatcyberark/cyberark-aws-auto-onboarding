import subprocess
import sys
import rsa
import base64
from log_mechanism import LogMechanism

DEBUG_LEVEL_DEBUG = 'debug' # Outputs all information
logger = LogMechanism()


def save_key_pair(pemKey):
    # Save pem to file
    logger.trace(caller_name='save_key_pair')
    logger.info('Saving key pair to file')
    savePemToFileCommand = 'echo {0} > /tmp/pemValue.pem'.format(pemKey)
    subprocess.call([savePemToFileCommand], shell=True)
    subprocess.call(["chmod 777 /tmp/pemValue.pem"], shell=True)

def decrypt_password(instance_password_data):
    logger.trace(caller_name='decrypt_password')
    passwd = base64.b64decode(instance_password_data)
    with open ("/tmp/pemValue.pem", 'r') as f:
        private = rsa.PrivateKey.load_pkcs1(f.read())
    decrypted_password = rsa.decrypt(passwd,private).decode("utf-8")
    return decrypted_password
