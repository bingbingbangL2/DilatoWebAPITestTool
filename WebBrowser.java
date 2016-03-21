package com.dilato.model.web.dilatoWebDriver;

public enum WebBrowser {

	FIREFOX ("firefox"), 
	CHROME ("chrome"), 
	IE ("ie");
	
	private final String value;
	
	public String getValue() {
		return value;
	}

	private WebBrowser(String value){
		this.value =value;
		
	}

}
