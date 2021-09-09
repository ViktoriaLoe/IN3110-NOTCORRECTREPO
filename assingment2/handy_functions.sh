#!/bin/bash -x

input1="$1"
input2="$2"

 function_move () {
	# Assingning variables
	src=$input1
	dst=$input2

	
	# Checking if directories exist	
	if [ ! -d "$src" ]; then
		echo " $src src dierctory does not exist"
		exit 2
	fi
	# find / -type d -name $src > $src
	if [ ! -d "$dst" ]; then
		echo "dst dierctory does not exist"
		exit 2
	fi

	echo "Attempting to move $src to $dst"
	mv $src ./$dst
}

echo "$1 input1, $2 input2"
if [ $# -lt 2 ]; then
	echo "Illegal input. Useage: move src dst"
	exit 2

fi
function_move 
