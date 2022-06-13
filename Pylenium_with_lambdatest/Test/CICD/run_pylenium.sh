#! /usr/bin/env bash
remote_url="https://$LT_USERNAME:$LT_ACCESS_KEY@hub.lambdatest.com/wd/hub"

filter="pytest -v  ../test_google_search_lambda.py "

poetry run $filter --remote_url=$remote_url

# echo $command
