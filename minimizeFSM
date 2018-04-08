#!/usr/bin/expect

#########################################
# Mattia Corradi - Dalla Chiara Michele #
#########################################

if {$argc != 1} {
  puts "Numero di argomenti errato"
  puts "Devi inserire come parametro il nome della fsm da minimizzare"
  exit 1
}

set file_in [lindex $argv 0];
set file_out [lindex $argv 1];

spawn sis

expect "sis>"

send "rl $file_in\n"

send "state_minimize\n"
send "state_assign jedi\n"
send "stg_to_network\n"
send "wl $file_out\n"
send "quit\n"
interact

