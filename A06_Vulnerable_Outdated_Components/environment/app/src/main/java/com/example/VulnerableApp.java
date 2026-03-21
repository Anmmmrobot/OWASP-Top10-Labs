package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@SpringBootApplication
@RestController
public class VulnerableApp {

    private static final Logger logger =
            LogManager.getLogger(VulnerableApp.class);

    public static void main(String[] args) {
        SpringApplication.run(VulnerableApp.class, args);
    }

    @GetMapping("/")
    public String home(
            @RequestHeader(value="User-Agent", defaultValue="unknown") String ua
    ) {

        // 漏洞触发点
        logger.info("User Agent: {}", ua);

        return "Log4Shell demo running";
    }
}
