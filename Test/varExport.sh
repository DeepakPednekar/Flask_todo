#!/bin/bash

[ $# != 2 ] && printf "%20s\n" "[*] args required <username> <password>" && exit 1;

data={\"username\":\"$1\",\"password\":\"$2\"};
_header='Content-Type:application/json';
result=$(curl -H $_header localhost:5000/auth -d "$data");

pattern=`echo $result | grep --regex='"e.*"' -o `;
echo $pattern