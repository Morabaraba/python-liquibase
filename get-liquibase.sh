#!/usr/bin/env sh

set -e

JAR_PATH=liquibase/jar/liquibase.jar
JAR_URI=http://central.maven.org/maven2/org/liquibase/liquibase-core/3.5.3/liquibase-core-3.5.3.jar

rm -f $JAR_PATH
curl $JAR_URI > $JAR_PATH

java -jar $JAR_PATH --version
