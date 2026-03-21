FROM openjdk:8-jdk

WORKDIR /app

# 安装 Maven
RUN apt-get update && apt-get install -y maven

# 拷贝项目
COPY . .

# 编译
RUN mvn clean package -DskipTests

EXPOSE 8080

CMD ["java", "-jar", "target/vulnerable-app-1.0.jar"]
