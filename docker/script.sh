#!/bin/bash
sleep 5
curl https://cpw.state.co.us/Documents/Leftover.pdf > Leftover.pdf
pdftotext -raw Leftover.pdf text.txt
cat text.txt | tr -d "[:space:]" > file1.txt
curl --data "@file1.txt" <AWS_LAMBDA_URL>


sleep 25
curl https://cpw.state.co.us/Documents/Leftover.pdf > Leftover.pdf
pdftotext -raw Leftover.pdf text.txt
cat text.txt | tr -d "[:space:]" > file2.txt
cmp --silent text1.txt text2.txt
if [ "$?" == 1 ]
then
    curl --data "@file2.txt" <AWS_LAMBDA_URL>
fi