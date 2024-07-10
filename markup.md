python -m venv requirements.txt
virtualenv myenv
source ./Scripts/activate
pip install -r requirements.txt (for bash under windows)
python app.py

pip install --upgrade werkzeug flask SHOULD not be required with the latest requirements.txt file. To be run otherwise