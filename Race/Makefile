clean:
	@echo "[Cleaning directory]"
	@rm -r Code/__pycache__

run:
	@echo "[Running Application]"
	@python3 Code/Main.py
	@echo "[Application terminated]"

ut:
	@echo "[Uploading changes to Tester]"
	@git add .
	@git commit -m $(arg)
	@git push origin master-tester
	
