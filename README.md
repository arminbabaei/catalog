# Project Item Catalog

## Project Overview
You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Project Display Example
Note: The screenshots on this page are just examples of one implementation of the minimal functionality. You are encouraged to redesign and strive for even better solutions.

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

In this sample project, the homepage displays all current categories along with the latest added items.

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0c98_localhost8080/localhost8080.png "Title Text")

http://localhost:8000/
Selecting a specific category shows you all the items available for that category.

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0d0e_snowboarding/snowboarding.png "Title Text")

http://localhost:8000/catalog/Snowboarding/items
Selecting a specific item shows you specific information of that item.

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0d7a_item/item.png "Title Text")

http://localhost:8000/catalog/Snowboarding/Snowboard
After logging in, a user has the ability to add, update, or delete item info.

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0df0_edititem/edititem.png "Title Text")

http://localhost:8000/ (logged in)

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0e51_snowboardloggedin/snowboardloggedin.png "Title Text")

http://localhost:8000/catalog/Snowboarding/Snowboard (logged in)

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0e8c_snowboardedit/snowboardedit.png "Title Text")

http://localhost:8000/catalog/Snowboard/edit (logged in)

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0ec8_snowboarddelete/snowboarddelete.png "Title Text")

http://localhost:8000/catalog/Snowboard/delete (logged in)
The application provides a JSON endpoint, at the very least.

![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/598e0f11_catalogjson/catalogjson.png "Title Text")

http://localhost:8000/catalog.json


## Installation

### Install VirtualBox

VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the _platform package_ for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

**Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com.](https://www.vagrantup.com/downloads.html) Install the version for your operating system.

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

![vagrant --version](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584881ee_screen-shot-2016-12-07-at-13.40.43/screen-shot-2016-12-07-at-13.40.43.png)

_If Vagrant is successfully installed, you will be able to run_ `vagrant --version`
_in your terminal to see the version number._
_The shell prompt in your terminal may differ. Here, the_ `$` _sign is the shell prompt._

### Download the VM configuration

Use Github to fork and clone, or download, the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

You will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory:

![vagrant-directory](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png)

_Navigating to the FSND-Virtual-Machine directory and listing the files in it._
_This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows._

## Instructions

### Start the virtual machine

From your terminal, inside the **vagrant** subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

![vagrant-up-start](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png)

_Starting the Ubuntu Linux installation with `vagrant up`._
_This screenshot shows just the beginning of many, many pages of output in a lot of colors._

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

![linux-vm-login](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png)

_Logging into the Linux VM with `vagrant ssh`._

### Logged in

If you are now looking at a shell prompt that starts with the word `vagrant` (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

If not, take a look at the [Troubleshooting](#troubleshooting) section below.

### The files for this course

Inside the VM, change directory to `/vagrant` and look around with `ls`.

The files you see here are the same as the ones in the `vagrant` subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

### Running the database

The PostgreSQL database server will automatically be started inside the VM. You can use the `psql` command-line tool to access it and run SQL statements:

![linux-vm-PostgreSQL](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58489186_screen-shot-2016-12-07-at-14.46.25/screen-shot-2016-12-07-at-14.46.25.png)

_Running `psql`, the PostgreSQL command interface, inside the VM._

### Logging out and in

If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again.

If you reboot your computer, you will need to run `vagrant up` to restart the VM.