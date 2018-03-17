#!/usr/bin/env bash

set -e

PG_VERSION=$1
if [ -z "$PG_VERSION" ]
  then
    PG_VERSION=42.2.0
fi

JAR_PATH=liquibase/jar/postgresql.jar
JAR_URI=https://jdbc.postgresql.org/download/postgresql-$PG_VERSION.jar

rm -f $JAR_PATH
curl $JAR_URI > $JAR_PATH

set +e

JAVA_OUT=`java -jar $JAR_PATH`
EXIT_CODE=$?

if [[ $JAVA_OUT = *"PgJDBC driver is not an executable"* ]]; then
  exit 0
fi

if [ $EXIT_CODE -ne 0 ] 
  then
    java -version
    echo 'ERROR: postgresql.jar not working download the jar for your java version eg. `get-postgresql.sh 9.4.1212.jre7` see "https://jdbc.postgresql.org/download.html".'
fi

exit $EXIT_CODE