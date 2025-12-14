#!/bin/bash

set -e

URL=$1
URL=${URL:-localhost:8080}

echo "Test /health endpoint"
(set -x; curl $URL/health )
echo "Test /predict endpoint"
(set -x; curl $URL/predict -d '{"x": [1,2,3,4]}' )
echo "Test /predict endpoint with incorrect data"
(set -x; curl $URL/predict -d '{"x": [1,2,3]}' )
