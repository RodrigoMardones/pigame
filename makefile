createEnv:
	python3 -m venv venv

runEnv:
	source venv/bin/activate

install:
	pip3 install -r requirements.txt

rundev:
	python3 src/main.py