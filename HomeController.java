package com.Mario.HelloHuman;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController 
public class HomeController {
	@RequestMapping("/")
	public String name(@RequestParam(value = "name", required = false) String searchQuery) {
		if(searchQuery==null) {
		return  "Hello Human" +" Welcome To SpringBoot!";
		}else {
			return "Welcome" + "" + searchQuery + " to SpringBoot!";
		}
	} 
}
