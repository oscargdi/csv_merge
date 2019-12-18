# CSV merger
This is an utility to merge a set of CSV files in a folder into a single file. It is built in Python 3.7.x, so it is **important** to have that version installed:

## Environment Setup

In order to initialize your development environment, you should perform the following steps:

### Install Python 3.7.x

You should install **Python 3.7.x** in your machine, to do so go to [download page](https://www.python.org/downloads/) and install any of the 3.7.x releases for your Operating System.

### Install VirtualEnv

VirtualEnv allows you to create isolated Python environments for the different projects you work in. This is useful when trying different version of packages or when wanting  to install same environment accross multiple developers.

You should install **virtualenv** in your machine. Once Python is installed, use **pip**(package manager) to achieve this by executing the following:

> Note:
> Mac OS brings Python 2 out of the box. This cause that using only **pip** command executes the Python 2 package manager. To avoid this, once Python 3 is installed you must use **pip3** command to manage the packages for this version of Python.

In Mac OS:

```bash
$ pip3 install virtualenv
```

In Windows, there should not be any issue with different pip versions:
```bash
$ pip install virtualenv
```

### Create a virtual environment
Once **virtualenv** is installed, in the corresponding git repository folder, execute the command:

```bash
$ virtualenv .venv
```

It will create a folder called **.venv** (naming is a convention) that contains all the python packages and dependencies out of the box.

To activate the virtual environment, you should run:

In Mac OS (within project folder):
```bash
$ source .venv/bin/activate
```

In Windows (within project folder):
```bash
$ .venv\Scripts\activate
```

Right after you activate your virtual environment, you should see and indicator that it is active like this:

```bash
(.venv) $ 
```

### Install python packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python packages. You can install them directly by executing:

In Mac OS:
```bash
(.venv) $ pip3 install -r requirements.txt
```

In Windows:
```bash
(.venv) $ pip install -r requirements.txt
```

## Build project
To build the project, you should use **Pyinstaller** which packs the script into a single executable file. To do so, you have to run:

```bash
(.venv) $ pyinstaller csv_merger.csv --clean --onefile
```

Pyinstaller will create a `dist` folder which contains the executable file.