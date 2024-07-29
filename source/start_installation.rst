Installation
===========================

GEMINI Digital Twin is compiled as docker container, thus it will be easy to setup and replicate to
a server (on premises or cloud). It is needed to have a basic knowledge of Docker to install this tool.
Several tutorial can be found in the internet (`example <https://medium.com/@sayalishewale12/docker-compose-and-essential-commands-the-ultimate-guide-to-streamlining-your-container-workflow-8018ca171300>`_)

The pre-requisite software of this installation are:

* Docker Desktop (https://docs.docker.com/engine/install/)
* Docker Compose (https://docs.docker.com/compose/install/)

docker-compose.yml
 .. code-block::
    :linenos:

    version: '3.8'

    networks:
        gemini:

    services:
        gemini_framework:
            image: ghcr.io/gemini-digital-twin/gemini-framework:MVP
            environment:
                - GEMINI_PLANT=HAL
            volumes:
                - project-db:/opt/gemini-project
            depends_on:
                - influxdb
            networks:
                - gemini

        gemini_gui:
            image: ghcr.io/gemini-digital-twin/gemini-user-interface:MVP
            ports:
                - 5101:5101
            environment:
                - GEMINI_FRONTEND_PORT=5101
                - GEMINI_MYSQLDB_URL=mysqldb
            restart: unless-stopped
            volumes:
                - project-db:/opt/gemini-project
                - doc-db:/opt/gemini-documentation
            depends_on:
                - mysqldb
            networks:
                - gemini

        gemini_doc:
            image: ghcr.io/gemini-digital-twin/gemini-documentation:MVP
            restart: unless-stopped
            volumes:
                - doc-db:/opt/gemini-documentation
            networks:
                - gemini

        gemini_project:
            image: ghcr.io/gemini-digital-twin/gemini-project:MVP
            restart: unless-stopped
            volumes:
                - project-db:/opt/gemini-project
            networks:
                - gemini

        mysqldb:
            image: mysql:8.0
            ports:
                - 3306:3306
            environment:
                - MYSQL_ROOT_PASSWORD=root
                - MYSQL_DATABASE=geminidb
            volumes:
                - mysqldb_data-storage:/data/db
                - mysqldb_var_lib-storage:/var/lib/mysql
            restart: unless-stopped
            networks:
                - gemini

        grafana:
            image: grafana/grafana:latest
            ports:
                - 3000:3000
            environment:
                - GF_SECURITY_ALLOW_EMBEDDING=true
                #- GF_SECURITY_COOKIE_SAMESITE=none
            volumes:
                - grafana-storage:/var/lib/grafana
            depends_on:
                - influxdb
            networks:
            - gemini

        influxdb:
            image: influxdb:latest
            ports:
                - 8086:8086
                - 8998:8088
            environment:
                - DOCKER_INFLUXDB_INIT_MODE=setup
                - DOCKER_INFLUXDB_INIT_ORG=TNO
                - DOCKER_INFLUXDB_INIT_BUCKET=gemini-project
                - DOCKER_INFLUXDB_INIT_USERNAME=gemini-user
                - DOCKER_INFLUXDB_INIT_PASSWORD=gemini-password
                - DOCKER_INFLUXDB_INIT_TOKEN=gemini-token
            volumes:
                - influxdb-storage:/var/lib/influxdb
                - influxdb2-storage:/var/lib/influxdb2
                - influxdb2etc-storage:/etc/influxdb2
            restart: unless-stopped
            networks:
                - gemini

    volumes:
        mysqldb_data-storage:
        mysqldb_var_lib-storage:
        grafana-storage:
        influxdb-storage:
        influxdb2-storage:
        influxdb2etc-storage:
        project-db:
        doc-db:

There are several services in this docker-compose.yml file:

#. GEMINI Framework
    This container runs the real-time modules when is called. The container shares volume of
    project-db with other container to have a common project data. The project name should be
    given in GEMINI_PLANT environment variable. This container depends on InfluxDB container to
    access the real-time data.

#. GEMINI User interface (GUI)
    This container provides the web user interface of GEMINI. This container depends on MySQLDB container
    to access user authentication and project. The port number can be defined in GEMINI_FRONTEND_PORT
    environment variable. The container shares volume of project-db with other container to have a
    common project data and volume of doc-db to access the documentation.

#. GEMINI Documentation
    This container provides the web-based documentation of GEMINI. The content is shared with GEMINI
    User Interface container.

#. GEMINI Project
    This container provides the shared volume project-db that can be accessed by GEMINI Framework
    container and GEMINI User Interface container.

#. Grafana
    This is a multi-platform open source analytics and interactive visualization web application.
    It can produce charts, graphs, and alerts for the web when connected to supported data sources.
    It is used to visualize the time series data.

#. MySQLDB
    It is an open-source relational database management system. To handle several data structured of
    GEMINI.

#. InfluxDB
    It is an open-source time series database. It is used for storage and retrieval of time series
    data in fields such as operations monitoring, application metrics, Internet of Things sensor
    data, and real-time analytics. We use this database to store time series data from Geothermal
    assets.









