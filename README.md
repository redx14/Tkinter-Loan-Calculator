# Tkinter-Loan-Calculator
Allows user to input multiple different loans at time and provide how much they can pay monthly. The program will generate a file that will break down how long it will take to pay off each loan, total interest that will be paid over the total length of the loan, and provide insight on which loan should be paid off first based on the interest.

##########################

THIS WILL NOT WORK ON MACOS > v11.2

##########################

In order to get it working you must use both brew and pyenv to install tkinter and python seperately so that the python reinstall grabs the tkinter properlly.
Run the following commands:

1. brew uninstall tcl-tk uninstall the old tk if you have it

2. pyenv uninstall 3.10.5 ...or whatever your current global Python version is

3. brew install tcl-tk grab a fresh install of tk

4. pyenv install 3.10.5 grab a fresh install of Python 3.10.5 (or whichever)

5. pyenv global 3.10.5 set your global Python version (matching the version you just installed above)

You need to install tk via homebrew before installing Python with pyenv because pyenv will automatically try to use whatever tk package it can find when it installs Python.

This will also work if you are using pyenv to upgrade from one version of Python to another.
