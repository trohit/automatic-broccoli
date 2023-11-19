# simple DB
# From Designing Data Intensive Applications
# $ db_set 123456 '{"name":"London","attractions":["Big Ben","London Eye"]}'
# $ db_set 42 '{"name":"San Francisco","attractions":["Golden Gate Bridge"]}'
# $ db_get 42

#!/bin/bash
die () {
    echo "$*"
    exit 1
}

function db_set () {
    echo "$1,$2" >> database
}

function db_get () {
    grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
}

# main
cmd=$1
shift
grep -q "function $cmd () {" $0 || die "wrong argument: '$cmd'"
$cmd "$@"
