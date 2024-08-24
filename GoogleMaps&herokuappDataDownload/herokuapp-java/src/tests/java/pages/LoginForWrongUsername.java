package src.tests.java.pages;

import org.openqa.selenium.*;
import src.tests.java.main.*;

public class LoginForWrongUsername extends MainMethods {
    private final By header = By.xpath("//div[@class ='example']");
    private final By username = By.xpath("//input[@id='username']");
    private final By password = By.xpath("//input[@id='password']");
    private final By button = By.xpath("//button");
    private final By errorMessage = By.xpath("//div[@class ='flash error']");


    public LoginForWrongUsername verifyText(){
        verifyThatElementIsVisible(header);
        //test.log(LogStatus.INFO, "[Headeris visible"] );
        return this;
    }

    public LoginForWrongUsername enterWrongUsername() {
        type(username, "tom");
        return this;
    }

    public LoginForWrongUsername enterPassword() {
        type(password, "SuperSecretPassword!");
        return this;
    }
    public LoginForWrongUsername buttonClick(){
        click(button);
        return this;
    }
    public LoginForWrongUsername message(){
        verifyThatElementIsVisible(errorMessage);
        return this;
    }



}
