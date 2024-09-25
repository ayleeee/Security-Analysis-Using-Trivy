# 1. Build stage
FROM gradle:7.6.1-jdk17 AS build

WORKDIR /app

COPY build.gradle settings.gradle ./

COPY src ./src

RUN gradle build --no-daemon

# 2. Run stage
FROM openjdk:17-jdk-slim

WORKDIR /app

COPY --from=build /app/build/libs/wooso-0.0.1-SNAPSHOT.jar ./wooso.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "wooso.jar"]

