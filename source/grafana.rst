Time Series Viewer
===========================


Setup Database Connection
---------------------------

* Click Connection
* Click Add new connection
* Search "influxdb"
* Click Data Source InfluxDB
* Click Add New Data Source

.. image:: images/database_setup_connection_1.jpg
    :width: 100%

* Fill the database name
* Choose Query language "Flux"
* add URL http://influxdb:8086
* toggle Basic auth

.. image:: images/database_setup_connection_2.jpg
    :width: 100%

* Fill Basic Auth Details

    * Username: gemini-user
    * Password: gemini-password

* Fill InfluxDB Details

    * Organization: TNO
    * Token: <create token InfluxDB>
    * Default Bucket: gemini-project

* Click Save & test

.. image:: images/database_setup_connection_3.jpg
    :width: 100%

* Create Token Influx DB
* login to http://<yourdomain>:8086
* Fill username and password
* Generate API token
* Click All Access API Token
* Fill Description, e.g. gemini-token
* Copy the API token and put in InfluxDB Details

.. image:: images/database_setup_connection_4.jpg
    :width: 100%


Create Dashboard
---------------------------