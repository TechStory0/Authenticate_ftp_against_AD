sudo apt -y install ufw
sudo ufw enable
UFW rules
sudo ufw allow from 10.10.10.135 proto tcp to any port 22
sudo ufw allow proto udp from 10.10.10.0/24 to any port 137
sudo ufw allow proto udp from 10.10.10.0/24 to any port 138
sudo ufw allow proto tcp from 10.10.10.0/24 to any port 139
sudo ufw allow proto tcp from 10.10.10.0/24 to any port 445
sudo ufw allow from 10.10.10.0/24 proto tcp to any port 21
