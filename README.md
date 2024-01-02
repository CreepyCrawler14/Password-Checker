# Description
This tool was created so people can quickly check if a password exists within a password list.
To use this tool you will need to download a password list from a different source.
This tool does not come with a built in password list.
Depending on how powerful your device is, the password checker tool can run through most password lists in under 10 seconds.
Run all of the commands below in a linux terminal adding sudo permissions where required.
# How To Run
apt update && upgrade

apt install git -y

git clone https://github.com/CreepyCrawler14/Password-Checker.git

apt install pip -y

pip install flask

cd Password-Checker

python3 app.py

Then in your web browser go to http://127.0.0.1:5000
