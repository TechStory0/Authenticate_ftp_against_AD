sudo apt -y install cron
sudo crontab -e
32 23 * * * /usr/bin/python3.9 /home/scripts/script.py
sudo crontab -l