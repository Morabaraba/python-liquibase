#!/usr/bin/env sh

set -e

JAR_PATH=liquibase/jar/mysql-connector-java-5.1.45.jar
JAR_URI=https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.45/mysql-connector-java-5.1.45.jar

rm -f $JAR_PATH
curl $JAR_URI > $JAR_PATH

java -jar $JAR_PATH --version
