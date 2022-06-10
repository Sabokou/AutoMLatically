DIR=/volume
if test -d "$DIR"; then
    export BASE_DIR=/volume
    echo volume mount detected:
else
    export BASE_DIR=/app
    echo no volume mount detected:
fi
echo "Using base directory $BASE_DIR ..."