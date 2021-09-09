#!/bin/bash -x

dst=""
src=""

 function_move () {
	# Checking if directories exist	
	check_if_exist $src "src"

	check_if_exist $dst "dst"


	echo "Moving directory and it's content $src to $dst"
	

	# In the case of file specific move, errors are not handeled
	if [ ! -z $1 ]; then
		src=$src/*$1
		echo "Only moving "$1" files"
	fi
		
	mv  $src ./$dst

}

check_if_exist () {

	if [ ! -d $1 ]; then
		echo " $2 dierctory does not exist"
		
		# If the dir doesn't exist the user wil get to option to create one
		if [ $2 = "dst" ]; then
			create_dir 
		else
			exit 1
		fi
	fi
}

create_dir () {
	echo "Do you want to create a directory with that name?"
	read reply

	if [ "$reply" = "yes" ]; then
		echo "Do you want it to add the current date to your dir name?"
		read reply2

		if [ "$reply2" = "yes" ]; then
			date=$(date '+%Y-%m-%d %H:%M')
			mkdir "date-$dst"
		else
			mkdir $dst
		fi
	fi
}

if [ $# -lt 2 ]; then
	echo "Illegal input. Useage: script src dst"
	exit 1
else
	dst=$2
	src=$1
	function_move $3 
fi

