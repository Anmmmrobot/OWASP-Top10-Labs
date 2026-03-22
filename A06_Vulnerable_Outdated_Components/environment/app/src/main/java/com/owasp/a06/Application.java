package com.owasp.a06;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@SpringBootApplication
@RestController
public class Application {

    // Log4j2 Logger
    private static final Logger logger =
            LogManager.getLogger(Application.class);

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    /*用户输入被直接写入日志，Log4j2 会解析 ${} lookup，从而触发 JNDI 远程加载 → RCE*/
    @GetMapping("/login")
    public String login(@RequestParam String username) {

        // 关键漏洞点：必须使用参数化日志
        // Log4j 会在格式化阶段解析 ${jndi:...}
        logger.info("User login: {}", username);

        return "Hello " + username;
    }
}
