# Slack notifier
This script will help you to send slack scheduled notification (message) like `daily stand up meeting`, `prayer reminder` etc.

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
1. Install `requests` python module, if you don't already have that
```
pip install requests
```
2. Create a slack bot user.
3. Collect the access token.
4. Open `config.py` and set the `slack access token` and other information like `channel name`, `user name`.
5. Adjust the notifier time.

### Contributors
* [Syed Sirajul Islam Anik](https://github.com/ssi-anik)
* [Ahmed shamim](https://github.com/me-shaon)

_Thank you :)_
