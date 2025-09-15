#!/bin/sh

if [ ! -f karate.jar ]; then
    # karate was not found, so go get it
    sh get_karate.sh
fi

# run the app server in the background
sh run.sh &

if [ -f karate_results ]; then
    rm karate_results
fi

java -cp  karate.jar com.intuit.karate.Main test/karate/ > karate_results
cat ./karate_results

echo Karate tests status: 
if grep -q "failed: 0" ./karate_results; then
    echo Passed
else
    echo Failed
fi

# kill everything including the app server
trap "trap - TERM && kill -- -$$" INT TERM EXIT
