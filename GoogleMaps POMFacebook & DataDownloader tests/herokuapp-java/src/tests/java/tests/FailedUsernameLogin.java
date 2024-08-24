package src.tests.java.tests;

import org.openqa.selenium.*;
import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class FailedUsernameLogin extends MainMethods {

    LoginForWrongUsername loginForWrongUsername = new LoginForWrongUsername();

    @BeforeMethod
    public void SetUp(){
        createDriver();
        openApplication("https://the-internet.herokuapp.com/login");
    }
    @Test

    public void LoginTest() {
        createReport("Login test");
        loginForWrongUsername.verifyText()
                .enterWrongUsername()
                .enterPassword()
                .buttonClick()
                .message();
    }
    @AfterMethod
    public static void tearDown(){

    }
}
