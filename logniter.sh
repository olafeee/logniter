#!/bin/sh
/usr/bin/python3 logniter.py

start() {
    cd $workdir
    /usr/bin/python /etc/logniter/logniter.py &
    echo "Server started."
}
stop() {
    pid=`ps -ef | grep '[p]ython /etc/logniter/logniter.py' | awk '{ print $2 }'`
    echo $pid
    kill -15 $pid
    sleep 1
    echo "Server stopped."
}
case "$1" in
  start)
    start
    ;;
  stop)
    stop   
    ;;
  *)
    echo "Usage: /etc/init.d/tornado-tts {start|stop|restart}"
    exit 1
esac
exit 0