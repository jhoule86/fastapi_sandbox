#!/bin/sh

if [ ! -f karate.jar ]; then
    # karate was not found, so go get it
    sh get_karate.sh
fi

# run the app server in the background
sh run.sh &

java -cp  karate.jar com.intuit.karate.Main test/karate/sample.feature

# kill everything including the app server
trap "trap - TERM && kill -- -$$" INT TERM EXIT
