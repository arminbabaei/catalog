# Project Item Catalog

## Project Overview
A Web application that provides a list Cagetory items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Project Setup

$ pip install -r requirements.txt --user

$ psql postgres

postgres=# create database catalog;
postgres=# create user catalog with encrypted password ‘catalog’;
postgres=# grant all privileges on database catalog to catalog;

postgres=# \c catalog 
You are now connected to database "catalog" as user "armin".


catalog=# \l
                         List of databases
   Name    | Owner | Encoding | Collate | Ctype | Access privileges 
-----------+-------+----------+---------+-------+-------------------
 armin     | armin | UTF8     | C       | C     | 
 catalog   | armin | UTF8     | C       | C     | =Tc/armin        +
           |       |          |         |       | armin=CTc/armin  +
           |       |          |         |       | catalog=CTc/armin
 postgres  | armin | UTF8     | C       | C     | 
 template0 | armin | UTF8     | C       | C     | =c/armin         +
           |       |          |         |       | armin=CTc/armin
 template1 | armin | UTF8     | C       | C     | =c/armin         +
           |       |          |         |       | armin=CTc/armin
(5 rows)


catalog=# \dt
            List of relations
 Schema |     Name      | Type  |  Owner  
--------+---------------+-------+---------
 public | category      | table | catalog
 public | category_item | table | catalog
 public | user          | table | catalog
(3 rows)


postgres=# \d category
                                       Table "public.category"
    Column     |         Type          | Collation | Nullable |               Default                
---------------+-----------------------+-----------+----------+--------------------------------------
 id            | integer               |           | not null | nextval('category_id_seq'::regclass)
 name          | character varying(80) |           | not null | 
 user_id       | integer               |           |          | 
 creation_date | date                  |           |          | 
Indexes:
    "category_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "category_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)
Referenced by:
    TABLE "category_item" CONSTRAINT "category_item_category_id_fkey" FOREIGN KEY (category_id) REFERENCES category(id)

postgres=# \d+ category_item
                                                           Table "public.category_item"
    Column     |          Type          | Collation | Nullable |                  Default                  | Storage  | Stats target | Description 
---------------+------------------------+-----------+----------+-------------------------------------------+----------+--------------+-------------
 id            | integer                |           | not null | nextval('category_item_id_seq'::regclass) | plain    |              | 
 name          | character varying(80)  |           | not null |                                           | extended |              | 
 color         | character varying(250) |           |          |                                           | extended |              | 
 size          | character varying(250) |           |          |                                           | extended |              | 
 price         | character varying(8)   |           |          |                                           | extended |              | 
 description   | character varying(250) |           |          |                                           | extended |              | 
 category_id   | integer                |           |          |                                           | plain    |              | 
 user_id       | integer                |           |          |                                           | plain    |              | 
 creation_date | date                   |           |          |                                           | plain    |              | 
Indexes:
    "category_item_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "category_item_category_id_fkey" FOREIGN KEY (category_id) REFERENCES category(id)
    "category_item_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)
Access method: heap


## Linux Setup

$ sudo -s
$ su - catalog
$ cd /var/www/udacity_item_catalog
$ cd /etc/apache2/sites-available

The Rule of Least Privileges			
$ ls -la /home/ubuntu/.ssh

Becoming a super user				
$ sudo ls -la /home/ubuntu/.ssh

Package Source Lists				
$ cat /etc/apt/sources.list

Updating Available Package List		
$ sudo apt-get update

Upgrading Installed Packages		
$ sudo apt-get upgrade
$ sudo apt-get -y install postgresql postgresql-client postgresql-contrib

Install a Package 					
$ sudo apt-get -y install python python-dev python3 python3-dev
$ sudo apt-get -y install apache2 libapache2-mod-wsgi-py3

$ sudo service apache2 restart
$ tail -10 /var/log/apache2/error.log
$ sudo chown -R www-data:www-data /var/www/udacity_item_catalog

$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
$ sudo update-alternatives --display python

$ curl -s localhost
$ grep ^www-data /etc/group

User Management 					
$ cat /etc/passwd

Creating a New User				
$ sudo adduser catalog

Introduction to etc sudoers			
$ sudo cat /etc/sudoers
$ sudo ls /etc/sudoers.d

Giving sudo access	
$ sudo vi /etc/sudoers.d/catalog
$ sudo usermod -aG sudo catalog

Resetting the password				
$ sudo passwd -e catalog 	

Generating Key pairs				
$ ssh-keygen 

Installing Public Key
(server side)
$ mkdir .ssh
$ touch .ssh/authorized_keys
(client side)
$ cat ~/.ssh/id_rsa.pub
(server side)
$ vi .ssh/authorized_keys
$ chmod 700 .ssh
$ chmod 644 .ssh/authorized_keys
(client side)
$ ssh ubuntu@35.183.32.239


Forcing Key Based Authentication
$ sudo vi /etc/ssh/sshd_config
PasswordAuthentication no
$ sudo service ssh restart

UFW
$ sudo ufw status
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow ssh
$ sudo ufw allow 5000/tcp
$ sudo ufw allow www
$ sudo ufw enable


WSGI stands for (Web Server Gateway Inteface)

￼Apache user: www-data						
$ egrep -i "User|Group|SuexecUserGroup" /etc/apache2/envvars

Ownership is the same as apache is running.	
$ sudo ls  -las /var/www/udacity_item_catalog/

Check apache module enabled				
$ sudo apache2ctl -M|grep -i wsgi

mod_wsgi python version					
$ sudo grep wsgi /var/log/apache2/error.log|head -2
$ grep -i wsgi /etc/apache2/sites-enabled/catalog.conf

WSGIScript File

$ cat  /var/www/udacity_item_catalog/catalog.wsgi
import sys
sys.path.insert(0,"/var/www/udacity_item_catalog/")

$ cat /etc/apache2/sites-enabled/catalog.conf

<VirtualHost *:80>
    ServerAdmin armin.babaei@gmail.com
    WSGIDaemonProcess catalog user=catalog group=www-data threads=5
    WSGIProcessGroup catalog
    WSGIScriptAlias / /var/www/udacity_item_catalog/catalog.wsgi
    <Directory /var/www/udacity_item_catalog/>
        Require all granted
    </Directory>
</VirtualHost>


## Project Display Example

http://localhost:5000/
http://localhost:5000/catalog
Selecting a specific category shows you all the Category items available for that category.

![alt text]( "Title Text")

http://localhost:5000/categoty/1/items
Selecting a specific item shows you specific information of that item.

![alt text]( "Title Text")


http://localhost:5000/ (logged in)
http://localhost:5000/catalog (logged in)

![alt text]( "Title Text")

http://localhost:5000/categoty/1/items (logged in)

![alt text]( "Title Text")

http://localhost:5000/categoty/1/items/edit (logged in)

![alt text]( "Title Text")

http://localhost:5000/categoty/1/items/delete (logged in)
The application provides a JSON endpoint, at the very least.

![alt text]("Title Text")

http://localhost:5000/categoty/JSON

http://localhost:5000/categoty/1/items/JSON

http://localhost:5000/categoty/1/items/1/JSON

