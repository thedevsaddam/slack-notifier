# Slack notifier
This script will help you to send slack scheduled notification (message) like `daily stand up meeting`, `prayer reminder` etc

---
### Installation

Open terminal ( ctrl+alt+t ) and go to __Downloads__ directory

```bash
cd ~/Downloads/
```

Clone the repository

```bash
git clone https://github.com/thedevsaddam/slack-notifier.git
```
or download the zip file manually and unzip to __Downloads__ directory

Change permission to 777

```bash
sudo chmod -R 777 notifier
```
Open crontab in edit mode

```bash
crontab -e
```

Copy the line below and paste
```bash
* * * * * python /home/YOUR_USER_NAME/Downloads/slack-notifier/notifier.py
```
Replace YOUR_USER_NAME by your user name.

_Note:  To get username type `whoami` in interminal_

### Configuration
1. Create a slack bot user
1. Collect the access token
1. Open `config.py` and set thee slack access token and other information like `channel name`, `user name`
1. Adjust the prayer time

### Contributor
* [Syed Sirajul Islam Anik](https://github.com/ssi-anik)
* [Ahmed shamim](https://github.com/me-shaon)

**NB:** Make sure you install ```request``` module.

_Thank you :)_
