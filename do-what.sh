DATE=$(date +%Y-%m-%d:%H:%M:%S)
DIR=$(dirname $0)
APP=$(osascript $DIR/do-what.script)
if [ -n "$APP" ]
then
	echo $DATE $APP
fi
