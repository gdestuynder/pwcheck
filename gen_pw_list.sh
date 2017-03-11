#!/bin/bash

cat SecLists/Passwords/*txt|sort -u > pw_list.txt
wc -l pw_list.txt
