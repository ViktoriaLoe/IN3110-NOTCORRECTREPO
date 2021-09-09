#!/bin/bash -x


 function_move () {
	# Assingning variables

	echo "$1 input1, $2 input2"
		
	# Checking if directories exist	
	check_if_exist $1 "dst"

	check_if_exist $2 "src"

	# find / -type d -name $src > $src

	echo "Attempting to move $1 to $2"
	mv * $1 ./$2

}

check_if_exist () {

	if [ ! -d $1 ]; then
		echo " $2 dierctory does not exist"
		exit 1 
	fi
}

if [ $# -lt 2 ]; then
	echo "Illegal input. Useage: script src dst"
	exit 1
fi

function_move $1 $2 
