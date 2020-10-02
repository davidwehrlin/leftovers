docker run --name cdw-container djwehrlin/leftovers:1.0
if [ "$?" != 0 ]
then
    echo "Error occurred while running"
    echo "Make sure the cdw-container is not running"
    echo "Make sure the cdw-image exists"
    echo "Run clean.sh then build.sh"
fi
