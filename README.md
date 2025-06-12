<!-- remove all cache -->
python -m venv venv .
venv\Script\activate
pip insall -r requirement.txt

find . -type d -name "**pycache**" -exec rm -r {} +
