#! /bin/bash

function geturl {

	if [$1 == "Oslo"]; then
		url="https://pent.no/59.9127,10.7461"
	elif [$1 == "Bergen"]; then
		url="https://pent.no/60.39323,5.3245"	
	fi

}
echo $url
