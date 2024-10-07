install:
	# """
	# Install the required packages for the project.

	# This target upgrades pip to the latest version and installs
	# all dependencies listed in the requirements.txt file.
	# """
	echo "INSTALLING PACKAGES"
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	# """
	# Run tests for the project.

	# This target executes the test script (test.py) to ensure
	# that the code behaves as expected.
	# """
	echo "TESTING CODE"
	python test.py 

format:
	# """
	# Format the Python code using Black.

	# This target formats app.py according to the specified line length
	# of 50 characters. Black is a code formatter that enforces a consistent
	# style across Python files.
	"""
	echo "FORMATING CODE"
	black --line-length 50 app.py

lint:
	# """
	# Lint the Python code using Pylint.

	# This target runs Pylint on app.py to check for coding standards,
	# potential errors, and other issues. Specific warning categories are disabled
	# for a cleaner output.
	# """
	echo "LINTING CODE"
	pylint --disable=R,C,W1203,E1101,E0401,W0612,W0718 app.py

#pylint --disable=R,C,W1203,E1101 utils #cli #utilscli
#python -m pytest -vv test_main.py
#pylint --disable=R,C,W1203,E1101 mlib cli utilscli
#lint Dockerfile
#docker run --rm -i hadolint/hadolint < Dockerfile

# deploy:
# 	#push to ECR for deploy
# 	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
# 	docker build -t mlops .
# 	docker tag mlops:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/mlops:latest
# 	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/mlops:latest

	
all: install lint test format