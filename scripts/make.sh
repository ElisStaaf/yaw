if [! -d "src"]; then
    echo "(ERROR) src/ doesn't exist."
    exit 0
fi

cp src/* $1
