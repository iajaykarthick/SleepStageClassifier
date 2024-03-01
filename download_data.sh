#!/bin/bash

S3_BUCKET_URL="s3://physionet-open/sleep-edfx/1.0.0/"

DESTINATION_PATH="data/"

aws s3 sync $S3_BUCKET_URL $DESTINATION_PATH
echo "Data download complete."