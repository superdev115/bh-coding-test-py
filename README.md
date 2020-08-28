# bh-coding-test-py
Python project for concept proof (This demonstrates Flask-MVC structure and base exercise)

## Environment Setup(MacOS)
Install Python3 and some tools.
```sh
$ brew update
$ brew install python3
```
Along with Python 3, Homebrew will install **pip**, **setuptools** and **wheel**.

Make sure if python3 and pip3 was installed successfully
```sh
$ python3 --version
$ pip3 --version
```

## Run the project
Extract zip file and move to `bh-coding-test-py` directory in Terminal
```sh
$ ...
$ cd bh-coding-test-py
```

Create a Virtual Environment in the directory and install some dependencies
```sh
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install -r requirements.txt
```

Run the application
```sh
$ python3 runserver.py
```
You will see the app at `http://localhost:5000` on your browser.

## How to use
The app has `Add Product`,  `Load Products`, `List Products`, `Email Schedule` pages.

`Add Product` - add new product with data
`Load Products` - show the active customer products. (This is the default page)
`List Products` - show list of products sorted by **CustomerId**
`Email Schedule` - show email schedule list

You can click `Demo Data` button to use demo products.

