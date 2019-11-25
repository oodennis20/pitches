# Let The Pitch Out!

## Built By [Dennis](https://github.com/oodennis20/pitches/)

## Description
An application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will read on them and leave comments to give their feedback on them.


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See the pitches other people have posted.
* submit a pitch in any category.
* be signed in for me to leave a comment
* view the pitches I have created in my profile page.
* comment on the different pitches and leave feedback.

## [Specifications](SPECS.md)

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/oodennis20/pitches/
        $ cd pitches

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test

## Technologies Used
* Python3.6
* Flask

## [MIT.license](license.txt)

