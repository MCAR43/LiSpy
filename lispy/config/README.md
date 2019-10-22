# VPS Box Configuration

Following these commands will result in a secure environment where the site may be hosted.

## Base Setup:
Update box and install prequesite and utility packages

```
apt-get update
apt-get upgrade
apt-get autoremove
apt-get dist-upgrade
sudo reboot
apt-get install htop zip unzip dos2unix npm mariadb-server nginx
```


## MySQL Setup:
#### Config: `/etc/mysql/mysql.conf.d/mysqld.cnf`

```
mysql_secure_installation
mysql -u root -p
```

To add a sub-user, type MySQL and enter:

```
USE MYSQL;
CREATE USER 'developer'@'%' IDENTIFIED BY 'xxx';
GRANT ALL PRIVILEGES ON *.* TO 'developer'@'%';
SELECT host, user, password FROM mysql.user;
```


## Security Setup:

Change root password:
```
passwd
-> input
```

Add new user with only keys:
```
adduser --disabled-password --gecos "" developer
su developer
mkdir ~/.ssh/
nano ~/.ssh/authorized_keys
```

Disable direct root login:
```
su root
-> Enter password
nano /etc/ssh/sshd_config
-> PermitRootLogin no
sudo service ssh restart
```

## Ngninx Setup:
Hosts the site by proxying the Express server for the domain

```
mkdir /keys
chown developer:developer /keys/
-> upload
cd /etc/nginx/sites-available/
pico studytime.live
ln -s /etc/nginx/sites-available/studytime.live /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default
```
