#!/usr/bin/perl

print "Enter a string: ";
my $str = <>;
chomp($str);
my $reverse_str = reverse $str;

if ($str eq $reverse_str)
{
	print "The string is a palindrome!\n";
}
else
{
	print "The string is not a palindrome.\n";
}
