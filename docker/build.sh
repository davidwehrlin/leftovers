#!/bin/bash
echo "Checking to make sure docker is installed ..."
docker --version > /dev/null 2>&1
if [ "$?" ]
then
    echo "Building Docker Container ..."
    docker build -t djwehrlin/leftovers:1.0 . > /dev/null 2>&1
    echo "COMPLETE: Built new image named 'cdw-image'"
else
    echo "Install docker before building container"
fi