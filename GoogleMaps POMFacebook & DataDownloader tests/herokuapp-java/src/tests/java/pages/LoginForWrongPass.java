package src.tests.java.pages;

import org.openqa.selenium.*;
import src.tests.java.main.*;

public class LoginForWrongPass extends MainMethods {

    private final By header = By.xpath("//div[@class ='example']");
    private final By username = By.xpath("//input[@id='username']");
    private final By password = By.xpath("//input[@id='password']");
    private final By button = By.xpath("//button");
    private final By errorMessage = By.xpath("//div[@class ='flash error']");


    public LoginForWrongPass verifyText(){
        verifyThatElementIsVisible(header);
        //test.log(LogStatus.INFO, "[Header] is visible");
        return this;
    }

    public LoginForWrongPass enterUsername() {
        type(username, "tomsmith");
        return this;
    }

    public LoginForWrongPass enterWrongPassword() {
        type(password, "SuperSecretPass");
        return this;
    }
    public LoginForWrongPass buttonClick(){
        click(button);
        return this;
    }
    public LoginForWrongPass message(){
        verifyThatElementIsVisible(errorMessage);
        return this;
    }



}
