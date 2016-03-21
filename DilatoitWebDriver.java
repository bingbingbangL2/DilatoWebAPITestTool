package com.dilato.model.web.dilatoWebDriver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.RemoteWebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.internal.Dynamic;

import com.dilato.model.web.dilatoWebDriver.WebBrowser;

public class DilatoitWebDriver {
	public RemoteWebDriver webDriver;
	
	public DilatoitWebDriver(WebBrowser browser){
		switch(browser)
		{
		case CHROME:
			this.webDriver = new ChromeDriver();
			break;
		case IE:
			this.webDriver = new InternetExplorerDriver();
			break;
		case FIREFOX:
			this.webDriver = new FirefoxDriver();
			break;
		default:
			break;
 		}
	}

	public RemoteWebDriver getDilatoitWebDriver(){
		return this.webDriver;
	}
	
	public RemoteWebElement getElementBySelector(RemoteWebDriver webDriver, String cssSelector){
		RemoteWebElement element = (RemoteWebElement) webDriver.findElementByCssSelector(cssSelector);
		return element;
	}

	public void navigate(String url) throws InterruptedException{
		webDriver.get(url);
	}

	public RemoteWebElement getElementByXPath(RemoteWebDriver dilatoitWebDriver,
			String XPth) {
		RemoteWebElement element = (RemoteWebElement) webDriver.findElementByXPath(XPth);
		return element;
	}
	
	public RemoteWebElement getElementById(RemoteWebDriver dilatoitWebDriver,
			String id) {
		RemoteWebElement element = (RemoteWebElement) webDriver.findElementById(id);
		return element;
	}
	
	/*
	 * Wait for element appear
	 */
	public void waitForAppear(RemoteWebDriver dilatoitWebDriver, CssCodeType cssCodeType, final String cssCode, long timeout){
		WebDriverWait wait = new WebDriverWait(dilatoitWebDriver, timeout);
		By locator = null;
		Class<?> byClass;
		try {
			byClass = Class.forName("org.openqa.selenium.By");
			Method[] methods = byClass.getMethods();
			for(Method method : methods){
				if(method.getName().toUpperCase().equals(cssCodeType.toString())){
					locator = (By) method.invoke(byClass, cssCode);
					break;
				}
			}
			wait.until(ExpectedConditions.presenceOfElementLocated(locator));
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			e.printStackTrace();
		} catch (IllegalArgumentException e) {
			e.printStackTrace();
		} catch (InvocationTargetException e) {
			e.printStackTrace();
		} catch(NoSuchElementException noSuchElementEx){
			noSuchElementEx.printStackTrace();
		} catch(TimeoutException timeoutEx){
			timeoutEx.printStackTrace();
		}
	}
	
	public void maxWindow(){
		this.webDriver.manage().window().maximize();
	}
	
	/*
	 * Switch to frame by index
	 */
	public void switchToFrame(int index){
		this.webDriver.switchTo().frame(index);
	}
	
	/*
	 * Switch to default content
	 * 
	 */
	public void switchToDefaultContent(){
		this.webDriver.switchTo().defaultContent();
	}
	
	public void waitPageLoadComplete(){
//		this.webDriver.manage().
	}
	
	public void forward(){
		this.webDriver.navigate().forward();
	}
	
	public void back(){
		this.webDriver.navigate().back();
	}
	
	public void getPageSource(){
		this.webDriver.getPageSource();
	}
	
	public Object excuteJavaScript(String script, Object... args){
		
		script = "return " + script;
		
		return this.webDriver.executeScript(script, args);
	}
	
	public void closeLastWindow(){
		this.webDriver.close();
	}
	
	public void quitWebDriver(){
		this.webDriver.quit();
	}
}
