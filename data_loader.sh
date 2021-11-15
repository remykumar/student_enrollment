#!/bin/bash

for i in {101..10000}
do 
firstName=`head -$i  firstname_100.dat | tail -1`
lastName=`head -$i lastname_100.dat | tail -1`
curl --data "ids=$i&firstName=${firstName}&lastName=${lastName}&quarter=fall" http://localhost:8080
done 
