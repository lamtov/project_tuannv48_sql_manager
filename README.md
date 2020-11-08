# check server build:
    docker images | grep docker-registry:4000/base_sfd_lamtv10:q
# build code to image:
```sh
ssh root@172.16.30.86 (pass 123456a@) mkdir tuannv48

scp -r ProjectTuannv48 root@172.16.30.86:/home/tuannv48
cd ProjectTuannv48
docker build -t tuannv48_sql_manager:v1 .
```

# create database:
```sh
docker run -d --network=host --privileged -v /u01/docker/docker_log/mysql:/var/log/ -v /usr/share/docker/:/usr/share/docker/ -u mysql -e PXC_START='BOOTSTRAP' -e SQL_SST_USER="sstuser" -e SQL_SST_PASSWD="fPWOWrsMGLaBaP74iK57XoOyJy8aAEew" --name mysql docker-registry:4000/mysqlp_v20:q
docker exec -it mysql bash
mysql -u root
CREATE USER 'lamtv10'@'%' IDENTIFIED BY 'lamtv10';
GRANT ALL PRIVILEGES ON *.* TO 'lamtv10'@'localhost' IDENTIFIED BY "lamtv10";
GRANT ALL PRIVILEGES ON *.* TO 'lamtv10'@'%' IDENTIFIED BY "lamtv10";
GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'lamtv10'@'localhost';
```
# using file ProjectTuannv48/test_tuannv48/siddhi_databasev4.sql create database
# check database in database.svg

# run the code:
```sh
docker run -d --network=host --name tuannv48_database_manager -e DATABASE_URL="mysql+pymysql://vimtool:vimtool@172.20.3.75/vimtool" tuannv48_sql_manager:v1
```
# test the code:
```sh
all the api swagger  in : http://127.0.0.1:1234/api/v1/
for example to get 
http://127.0.0.1:1234/api/v1/threshold_lists
http://127.0.0.1:1234/api/v1/threshold_lists/4
```
# test api codeL
check in file ProjectTuannv48/test_tuannv48/curl_test.py 
un command each test case and run test.





