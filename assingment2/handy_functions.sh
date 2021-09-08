#!/bin/bash -x

function move {

	if ["$#" -ne 1]; then
		echo "Illegal input. Useage: move src dst"
		exit 2

	fi
	# Assingning variables
	src = $1
	dst = $2

	
	# Checking if directories exist	
	if [[ ! -d /$src ]]; then
		echo "src dierctory does not exist"
		exit 2
	fi
	if [[ ! -d /$dst ]]; then
		echo "dst dierctory does not exist"
		exit 2
	fi

	echo "Attempting to move $src to $dst"
	mv -rf  $src ./$dst
}
