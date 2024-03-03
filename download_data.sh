#!/bin/bash

S3_BUCKET_URL="s3://physionet-open/sleep-edfx/1.0.0/"

DESTINATION_PATH="data/"

aws s3 sync $S3_BUCKET_URL $DESTINATION_PATH
echo "Data download complete."

src_dir1="data/sleep-edf-database-expanded-1.0.0/sleep-cassette"
src_dir2="data/sleep-edf-database-expanded-1.0.0/sleep-telemetry"

target_dir="data/sleep-edf-database-expanded-1.0.0/edf"

mkdir -p "$target_dir"

cp -r "$src_dir1"/. "$target_dir"/
cp -r "$src_dir2"/. "$target_dir"/

rm -rf "$src_dir1"
rm -rf "$src_dir2"

echo "Contents of $src_dir1 and $src_dir2 have been combined into $dest_dir."

_sc_participant_sheet="data/sleep-edf-database-expanded-1.0.0/SC-subjects.xls"
_st_participant_sheet="data/sleep-edf-database-expanded-1.0.0/ST-subjects.xls"

sc_participant_sheet="data/sleep-edf-database-expanded-1.0.0/SC-participants.xls"
st_participant_sheet="data/sleep-edf-database-expanded-1.0.0/ST-participants.xls"

mv "$_sc_participant_sheet" "$sc_participant_sheet"
mv "$_st_participant_sheet" "$st_participant_sheet"