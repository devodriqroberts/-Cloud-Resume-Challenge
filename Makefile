.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy

deploy-site:
	aws s3 sync ./resume-site s3://cloud-resume-challenge-2023

build-deploy-site:
	sam build && sam deploy && aws s3 sync ./resume-site s3://cloud-resume-challenge-2023

invoke-put:
	sam build && sam local invoke CloudResumeChallengePutVisitorCountFunction

invoke-get:
	sam build && sam local invoke CloudResumeChallengeGetVisitorCountFunction