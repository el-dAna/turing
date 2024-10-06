install:
	echo "INSTALLING PACKAGES"
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	echo "TESTING CODE"
	python test.py 

format:
	echo "FORMATING CODE"
	black --line-length 50  app.py

lint:
	echo "LINTING CODE"
	pylint app.py

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