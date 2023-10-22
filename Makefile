install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:

format:	
	black *.py 

lint:
	#disable comment to test speed
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py 
	#ruff linting is 10-100X faster than pylint
	#ruff check *.py
	
all: install lint test format deploy
