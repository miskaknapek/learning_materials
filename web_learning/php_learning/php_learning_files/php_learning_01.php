
<?php
echo "hellow human";

//  variables
$x = 6;
echo $x;
$y = "five";
echo "\n" . $x . " === " . $y . "\n\n" ; 
//

// spacer // spacer // spacer
echo "\n\n"; 


// conditionals
if( $x > 5 ){
	echo "x (" . $x . ") is greater than five ";
} else{
	echo "x (" . $x . ") is less than five ";
}

// spacer // spacer // spacer
echo "\n\n"; 

//  loop(s)
for( $i = 0; $i < $x ; $i++ ){
	echo "$i === " . $i . "\n"; 
}


// spacer // spacer // spacer
echo "\n\n"; 

//  arrays 
$arr1 = array("a", "b", "c", "d" );
echo "arr1 = " . $arr1  . "\n";
echo $arr1[0];

// spacer // spacer // spacer
echo "\n\n"; 

// add an element to the end of the array
$arr1[] = "e";
echo "arr1 = " . $arr1;


// print array function 
function printArray( $inarray ){

	for( $i = 0; $i < count( $inarray ); $i++ ){
		echo "\n" . " i(" . $i . ") ==== " . $inarray[ $i ] . "\n" ;
	}

}

// call print function
printArray( $arr1 );


// spacer // spacer // spacer
echo "\n\n"; 


//  try foreach

foreach( $arr1 as $value ){
	echo $value . "\n" ;
}


//  end spacing 
echo "\n\n";
?>



















