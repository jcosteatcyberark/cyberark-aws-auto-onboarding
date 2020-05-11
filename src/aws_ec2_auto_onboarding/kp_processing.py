import subprocess


def save_key_pair(pemKey):
    # Save pem to file
    savePemToFileCommand = 'echo {0} > /tmp/pemValue.pem'.format(pemKey)
    subprocess.call([savePemToFileCommand], shell=True)
    subprocess.call(["chmod 777 /tmp/pemValue.pem"], shell=True)


def run_command_on_container(command, print_output):
    decryptedPassword = ""
    with subprocess.Popen(' '.join(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p:
        if print_output:
            decryptedPassword = print_process_outputs_on_end(p)
        else:
            p.wait()
    return [p.returncode, decryptedPassword]


def print_process_outputs_on_end(p):
    out = p.communicate()[0].decode('utf-8')
    # out = filter(None, map(str.strip, out.decode('utf-8').split('\n')))
    return out
