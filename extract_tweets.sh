#!/bin/bash

start_year=2012
end_year=2016

# hour to collect
hour="12"

# Dir to save to
mkdir -p $HOME/tweets

for year in $(seq $start_year $end_year); do
    for month in $(seq -w 1 12); do
        for day in 01 07 14 21; do 
            file_path="/net/corpora/twitter2/Tweets/$year/$month/${year}${month}${day}:$hour.out.gz"
            if [ -f "$file_path" ]; then
                output_file="$HOME/tweets/${year}${month}${day}.txt"
                zless $file_path | /net/corpora/twitter2/tools/tweet2tab -i id hashtags rt.id > $output_file
                echo "Finished processing: $output_file"
            fi
        done
    done
done
