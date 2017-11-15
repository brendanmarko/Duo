## Cleans project directory
clean:
	@echo "[Cleaning directory]"
	@if test -d Code/__pycache__ ; then echo "[Removing files]"; \
	rm -r Code/__pycache__; \
	fi	

## Runs the application
run:
	@echo "[Running Application]"
	@python2 Code/Main.py
	@echo "[Application terminated]"

## Uploads project changes to master:testera
## Requirements: arg=new_commit_name
## ie) make ut arg="Race0.00"
ut:
	@echo "[Uploading changes to Tester]"
	@git add .
	@git commit -m $(arg)
	@git push origin master:tester
	
## Uploaps project changes to master
## Requirements: arg=new_commit_name
## ie) make um arg="Race0.00"
um:
	@echo "[Uploading changes to Master]"
	@git add .
	@git commit -m $(arg)
	@git push origin master
