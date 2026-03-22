FROM maven:3.9.9-eclipse-temurin-8 AS builder

WORKDIR /build

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests

FROM eclipse-temurin:8-jdk

WORKDIR /app

# 拷贝构建好的 jar
COPY --from=builder /build/target/a06-vulnerable-0.0.1-SNAPSHOT.jar app.jar

# 暴露端口
EXPOSE 8080

# 关键：重新开启 JNDI 远程加载，用于复现 Log4Shell
CMD ["java","-Dcom.sun.jndi.ldap.object.trustURLCodebase=true","-Dcom.sun.jndi.rmi.object.trustURLCodebase=true","-jar","app.jar"]
