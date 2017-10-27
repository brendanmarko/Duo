## Cleans project directory
clean:
	@echo "[Cleaning directory]"
	@rm -r Code/__pycache__

## Runs the application
run:
	@echo "[Running Application]"
	@python3 Code/Main.py
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
