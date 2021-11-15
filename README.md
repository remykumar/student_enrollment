# student_enrollment

A small website developed in python flask and mysql to enroll the students in the DevOps program. 

To use the program: 

Step 1 : Clone the repo 

`git clone https://github.com/remykumar/student_enrollment.git`


Step 2 : Run the flash app 

`python3 app.py` 
![Module8_Assignment_DatadogDashboard_Support1](https://user-images.githubusercontent.com/38254327/141740903-db0c9633-c0b8-41a8-af56-0b022fc5b6b4.png)


Step 3 : Access the Enrollment site on localhost 

`http://localhost:8080` 



Step 4 : To upload/insert data via curl to the site 

`curl --data "ids=3&firstName=Jane&lastName=Smith&quarter=spring" http://localhost:8080` 


Step 5 : You can use the data_loader.sh script to upload data in batch/via automation 

`./data_loader.sh`

![Module8_Assignment_DatadogDashboard_Support2](https://user-images.githubusercontent.com/38254327/141741268-ac2306a7-f385-455b-9a05-21cd86bad8fb.png)
