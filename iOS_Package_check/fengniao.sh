#! /usr/bin/expect

spawn fengniao -p project_path -r jpg JPG jpeg png gif imageset

expect {

 "(l)ist|(d)elete|(i)gnore" { send "l\n"}

 "you have no unused resources in path" {send "\n"}

        }

expect eof

exit
