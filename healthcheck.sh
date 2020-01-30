# while [ "$( curl -s 54.254.166.52:4444/wd/hub/status | jq -r .value.ready )" != "true" ]
while [ "$( curl -s http://localhost:4444/wd/hub/status | jq -r .value.ready )" != "true" ]
do
    sleep 1
    echo "aheho"
done

echo "Checking if hub is done"
# pytest -v --html=reports/test_sample_report.html
