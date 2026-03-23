package com.owasp.a05;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class App {

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }

    // 未授权后台
    @GetMapping("/admin")
    public String admin(@RequestParam(defaultValue = "guest") String user) {
        return "Admin Panel Access : " + user;
    }

    // 故意泄露服务器环境
    @GetMapping("/debug")
    public Object debug() {
        return System.getenv();
    }
}
