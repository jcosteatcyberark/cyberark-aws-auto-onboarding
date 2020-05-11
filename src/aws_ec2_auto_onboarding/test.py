#!/usr/bin/python3

import requests

print("Hello")

def call_rest_api_post(url, request, header):
    try:
        restResponse = requests.post(url, data=request, timeout=30, verify=False, headers=header, stream=True)
    except Exception:
        print("Error occurred during POST request to PVWA")
        return None
    return restResponse

pvwaBaseUrl = "https://pvwa.cyberarklab.fr/PasswordVault"
header = { "content-type": "application/json", "Authorization": "YzE3YzdkZjEtNjRlZS00OTk0LTg1NzktNDE2MTA3NTdlMjdiOzc5OEMxNkREQTE1NUYyQjg7MDAwMDAwMDIzNjA4MkNEOTBENUIyQ0QxMjVDREY3OEVDRDU1REUzRDhFRTcyRTFERkRFQTQwRjRGM0JDMEZCMjhFOTRDNEI4MDAwMDAwMDA7" }

# Get Password
accountId="52_3"
getPasswordUrl="{0}/api/Accounts/{1}/Password/Retrieve".format(pvwaBaseUrl, accountId)
reason="""{ "reason":"AWS Python TEST" }"""
getPasswordResponse=call_rest_api_post(getPasswordUrl, reason, header)
#print(getPasswordResponse.text)

# Set password
setPasswordUrl="{0}/WebServices/PIMServices.svc/Account".format(pvwaBaseUrl)
safeName="CYBR_AWS_SSHKeys"
platform_id="CYBR_Lambda_UnixSSHKeys"
account_name="test_account_python_pvwa_2"
# Remove any quote. Safe because encoded in Base64
password_trimmed0=str(getPasswordResponse.text).replace('"', '')
password_trimmed1=password_trimmed0.replace("\n", "\\n")
password_trimmed2=password_trimmed1.replace("\r", "\\r")
#print(password_trimmed1)
username="ec2-user"
address="1.1.1.4"
safe_name="CYBR_Unix Administrators"
data = """{{
    "account" : {{
        "safe":"{0}",
        "platformID":"{1}",
        "address":"{5}",
        "accountName":"{2}",
        "password":"{3}",
        "username":"{4}",
        "disableAutoMgmt":"false"
    }}
}}""".format(safe_name, platform_id, account_name, password_trimmed2, username, address)
print(data)
postPasswordResponse=call_rest_api_post(setPasswordUrl, data, header)
print(postPasswordResponse)

