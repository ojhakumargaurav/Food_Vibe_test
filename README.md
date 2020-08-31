# Food_Vibe_test
Frontend: Vue.js
Backend: Bottle(python framework)
database: Mongodb
deployment: Docker

To run the python code base :

just go in food_vibe_codebase folder and pass command "python food_vibe_test.py"

or Deploy in Docker using : 

cd food_vibe_codebase
docker build . -t <app_name>
docker run --rm -it -p 8080:9092 <app_name>


and to run the vue js code as dockerfile is also there either u can build and run the index file using node js command: "npm build"

or navigate to folder food_vibe_ui2
and run "docker build . -t <app_name you like>"
and then "docker run -d -p 8080:80 <app_name you like>"
