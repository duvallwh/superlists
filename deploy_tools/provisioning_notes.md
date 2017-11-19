Provissioning a new site 
========================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Umbuntu:

	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see config file
* replace SITENAME

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME 

## Folder structure:
Assume user accound at /home/username

.
+-- test
