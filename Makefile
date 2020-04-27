.PHONY: run freeze deploy

run:
	flask run

freeze:
	./freeze.py

deploy: freeze
	rsync -avh build/ ccs:_www_abaisero
