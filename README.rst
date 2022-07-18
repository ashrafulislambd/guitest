========
guiprint
========


.. image:: https://img.shields.io/pypi/v/guiprint.svg
        :target: https://pypi.python.org/pypi/guiprint

.. image:: https://img.shields.io/travis/ashrafulislambd/guiprint.svg
        :target: https://travis-ci.com/ashrafulislambd/guiprint

.. image:: https://readthedocs.org/projects/guiprint/badge/?version=latest
        :target: https://guiprint.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Magically turn your CLI into a GUI program and make it more user friendly.


* Free software: MIT license


Features
--------

* Replaces print() with a nice dialog box
* Replaces input() with a nice input dialog.

Installation
------------

Open your terminal and type the line below to install guiprint

.. code:: bash

	pip install guiprint

In order to use it, first import it and write the following code at the very beginning. Try it on your existing project and your CLI should turn into a basic GUI program.


.. code:: python

	import guiprint
	print = guiprint.print
	input = guiprint.input

After just inserting these lines before any existing CLI program, run the program again and see the magic!

Additional Features
-------------------

To use the Input function as a Yes/No Dialog box, set the optional *mode* parameter to *'yesno'* like this,

.. code:: python

	x = input("Are you sure?", mode="yesno")

You can also let user choose an option from multiple options like this,

.. code:: python

	x = input("What's your favorite cricket team?: ", mode="multiple", options=["Bangladesh", "Zimbabwe", "Australia"]) 

Author: Md. Ashraful Islam