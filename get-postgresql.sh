#!/usr/bin/env sh

set -e

JAR_PATH=liquibase/jar/postgresql-42.2.0.jar
JAR_URI=https://jdbc.postgresql.org/download/postgresql-42.2.0.jar

rm -f $JAR_PATH
curl $JAR_URI > $JAR_PATH

java -jar $JAR_PATH --version
