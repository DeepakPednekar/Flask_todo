
[ ! -d venv ] && echo "enviromen dir doensn't exist " && exit 1

source venv/bin/activate
export FLASK_APP=flaskr
export FLASK_ENV=development
