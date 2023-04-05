<?php
$user = strtolower(readline("Choose rock, paper, or scissors: "));
$num = rand(1,100);
$choices = array("rock", "paper", "scissors");
if (!(in_array($user, $choices))) {
	echo "Invalid input, Please try again.\n";
	exit();
}
$comp = $choices[$num % 3];

if (strcmp($user, $comp) == 0) {
	echo "Sorry, you and the Computer chose ", $user, ", try again.\n"; 
}
else {
	switch ($user) {
		case "rock":
			if (strcmp($comp, "paper") == 0) {
				echo "Sorry, you lost. The computer chose paper.\n";
			}
			else {
				echo "Congratulations! You won! The computer chose scissors.\n";
			}
			break ;
		case "paper":
			if (strcmp($comp, "scissors") == 0) {
				echo "Sorry, you lost. The computer chose scissors.\n";
			}
			else {
				echo "Congratulations! You won! The computer chose rock.\n";
			}
			break ;
		default:
			if (strcmp($comp, "rock") == 0) {
				echo "Sorry, you lost. The computer chose rock.\n";
			}
			else {
				echo "Congratulations! You won! The computer chose paper.\n";
			}
	}
}
