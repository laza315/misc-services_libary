package src.tests.java.pages;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.*;
import src.tests.java.main.MainMethods;
import javax.xml.xpath.XPath;


public class SuccessLog extends MainMethods {

    private final By logintittle = By.xpath("//div[@class = 'flash success']");
    private final By logoutbutton = By.xpath("//i[@class = 'icon-2x icon-signout']");
    private final By logoutittle = By.xpath("//div[@id ='flash']");
    private final By username = By.xpath("//input[@id='username']");
    private final By password = By.xpath("//input[@id='password']");
    private final By button = By.xpath("//button");



    public SuccessLog verifyThatLoginTittleIsVisible(){
        verifyThatElementIsVisible(logintittle);
        return this;
    }

    public SuccessLog clickingOnLogOutButton(){
        click(logoutbutton);
        return this;
    }

    public LoginPage verifyThatLogOutTittleIsVisible(){
        verifyThatElementIsVisible(logoutittle);
        return new LoginPage();
    }




}
