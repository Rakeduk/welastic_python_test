# Welastic - test 
Basic Python recruitment tasks for Welastic

## Technologies
- Python 3.10
- SQLite 3.38 
 
## Data Base
#### Usage
To use scripts, you have to install SQLite (for Ubuntu users - `sudo apt-get install sqlite3`)
```console
python3 exc_1_database.py
python3 exc_1_queries.py
```
#### Issues:
SQLite does not support  `SELECT JSON_OBJECT(*)` which force to write every *key* and *value* inside `JSON_OBJECT`

## Firebase
The first solution which comes to mind is just checking if the user is already connected. Due to official [documentation](https://firebase.google.com/docs/database/web/offline-capabilities) this information is included in `/.info/connected` so potential pseudocode would look like this:
```
if already_connected(/.info/connected) != true then
    create_connection()
else
    continue script
```
This solution may work if we have access to this file without already creating a connection. 

Second idea would be to just simple create another file which contains information about connection status and modify it inside our script
```
if is_connected_file_value != true then
    create_connection()
    connection_file = true 
else 
    continue script 
.
.
.
if closing_connection() then
    connection_file = false
```
This should work, however almost for sure it's *bad practice*

Solution isn't obvious, and further analyses drive me to think that we cannot complete this task with **clear solution** and probably the program has bad architecture. If part of code should be executed only once, it should be in a different script. 


## Amazon S3 file uploader/downloader
Scripts allow us to upload/download multiple files directly to S3 Bucket with `boto3` 
#### Usage
Simple pass file name with extension as input argument (file has to be in same folder as script)
```console
# Upload one file
python3 s3_file_uploader.py test_file.txt

# Upload multiple files
python3 s3_file_uploader.py test_file.txt my_script.py hello_world.txt
```
To download file, similarly pass file name as argument
```console
python3 s3_file_downloader.py test_file.txt
```
## WeatherAPI
Script shows temperature from 3 cities and use [weatherapi.com](https://www.weatherapi.com/)
#### Usage
To use script, you need to add your own Api Key into api_key.py
```console
python3 weatherApi.py 
```



