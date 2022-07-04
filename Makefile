MAKEFLAGS := '--silent'

dev: upload-folder
	python main.py

upload-folder:
	rm -rf uploads
	mkdir uploads
