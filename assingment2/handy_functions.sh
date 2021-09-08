#!/bin/bash -x

function move {

	if ["$#" -ne 1]; then
		echo "Illegal input"
		exit 2
	fi
	src = $1
	dst = $2

	echo "Attempting to move $src to $dst"
	
	if [src exisits]; then

	fi
	echo "Directory does not exist"
}
