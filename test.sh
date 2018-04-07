#!/usr/bin/expect

#########################################
# Mattia Corradi - Dalla Chiara Michele #
#########################################



set file_in [lindex $argv 0];

log_file result.log

spawn sis

expect "sis>"

send "sr $file_in\n"
interact

