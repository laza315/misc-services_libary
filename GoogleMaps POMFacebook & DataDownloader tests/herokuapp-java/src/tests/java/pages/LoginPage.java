package src.tests.java.pages;

import com.relevantcodes.extentreports.*;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.*;
import src.tests.java.main.MainMethods;

public class LoginPage extends MainMethods {

    private final By header = By.xpath("//div[@class ='example']");
    private final By username = By.xpath("//input[@id='username']");
    private final By password = By.xpath("//input[@id='password']");
    private final By button = By.xpath("//button");


    public LoginPage verifyText(){
        verifyThatElementIsVisible(header);
        //test.log(LogStatus.INFO, "[Header] is visible");
        return this;
    }

    public LoginPage enterUsername() {
        type(username, "tomsmith");
        return this;
    }

    public LoginPage enterPassword() {
        type(password, "SuperSecretPassword!");
        return this;
    }

    public SuccessLog button() {
        click(button);
        return new SuccessLog();

    }



}

