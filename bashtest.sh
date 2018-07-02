#!/bin/bash

get_name() {
    echo "John"
}

echo "the name is $(get_name)"
NAME=hello
echo {a,b}.py
echo "{a,b}.py"
echo {1..5}
echo ${NAME}
echo "${NAME}"

if [ "hello" = ${NAME} ];then
    echo "non"
fi

if [ hello = ${NAME} ];then
    echo "non2"
fi

if [ world = "world" ]&&[ ${NAME} = "${NAME}" ];then
    echo "non3"
fi

for i in $(find /etc/ -name rc.* 2>/dev/null); do
    echo ${i}
done
for i in /etc/rc.*;do
    echo ${i}
done
for i in $(ls .); do
    echo ${i}
done

PYFILE=$(ls rc.file)
for ele in ${PYFILE}; do
    echo ${ele}
done
while false; do
    echo "s"
done
for i in {1..10}; do
    echo ${i}
done
ls . | while read file; do
    echo "${file}"
done
ls rc.file | while read file; do
    echo "pyfile ${file}"
done

function f1() {
    echo "f1"
}

f2() {
    echo "f2"
    local rtn=24
    echo ${rtn}
    return 255
}


echo "$(f1)--$(f2)"
f2
rtn=$?
echo ${rtn}

f3() {
    ls .
    local var=12
    printf "\necho commanding\n"
}
echo $(f3)
f3

TOPSHELLVAR="top var"
export TOPSHELLVAR
topf() {
    echo "$@"
    echo "func in top"
}
export -f topf

echo $BASH_SUBSHELL

#/bin/bash subbash.sh
#. subbash.sh
#exec ./subbash.sh 2>&1
#exec ./subbash.sh 2>1
#exec ./subbash.sh >1.stdout
#exec ./subbash.sh &>/dev/null
echo "current shell PID :$$"
./subbash.sh
#exec ./subbash.sh
func1() {
    if [ $# -lt 10 ];then
        echo "argu number $#, $*, $@"
        return 255
    fi
    return 0
}
IFS='--'
func1 "a" "b" "c" 1 2
echo "regex"
if [[ p =~ ^p$ ]];then
    echo "pythn regex ok"
fi

if [ 12 -gt 10 ];then
    echo "gt"
fi
if((11 > 10));then
    echo "gt2"
fi

LSFILE="$(ls -lt)"
echo ${LSFILE}

TSTSTR="./httptest/tmp/tmp.html"
echo ${TSTSTR%.html}
echo ${TSTSTR%ml}
echo ${TSTSTR##*m}
echo ${TSTSTR#*m}
echo ${TSTSTR##*/}
echo ${TSTSTR/tmp/TMP}
echo ${TSTSTR:0:3}
echo ${TSTSTR:3:3}
echo ${TSTSTR#*p}
echo ${TSTSTR%html}
echo ${TSTSTR##*tmp/}
echo ${TSTSTR#./}
echo ${TSTSTR%tm*}
echo ${TSTSTR%%tm*}
echo ${TSTSTR//tmp/TMP}
echo ${TSTSTR/%tmp*/TMP}
echo ${TSTSTR/#*test/TMP}
echo ${#TSTSTR}

ARRAYVAR=("a" "b" "c")
echo "${ARRAYVAR} echo array"
for i in $(echo ${ARRAYVAR}); do
    echo ${i}
done

for i in ${ARRAYVAR}; do
    echo "${i} for arry"
done
echo ${ARRAYVAR} | while read ele; do
    echo "while ${ele}"
done
for i in "${ARRAYVAR[@]}"; do
    echo "array ${i}"
done
DUPARRY=("${ARRAYVAR[@]}")
echo ${DUPARRY[@]}

traperr() {
  echo "ERROR: ${BASH_SOURCE[1]} at about ${BASH_LINENO[0]}"
}

set -o errtrace
trap traperr ERR
#echo hello | grep foo

func2() {
    case "$#" in
        0 | 1)
            echo "argus numless than 2"
            ;;
        2)
            echo "argus num 2"
            ;;
        *)
            echo "no num"
            ;;
    esac
}

func2 1