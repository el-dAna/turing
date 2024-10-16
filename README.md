# turing

black --line-length 50  file1.py
autopep8 --in-place --aggressive --aggressive file1.py

black --line-length 50  file1.py
autopep8 --in-place --aggressive --aggressive file1.py
pycodestyle --first file1.py

pylint app.py --fix