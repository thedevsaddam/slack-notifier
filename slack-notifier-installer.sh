#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

git clone https://github.com/thedevsaddam/slack-notifier.git
chmod -R 777 slack-notifier
cd slack-notifier
echo "* * * * * python $PWD/notifier.py" >> /etc/crontab

echo -e "${GREEN}Everything is ready, mate!${NC}"
