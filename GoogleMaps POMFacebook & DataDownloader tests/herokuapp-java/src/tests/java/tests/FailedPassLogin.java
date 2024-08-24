package src.tests.java.tests;

import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class FailedPassLogin extends MainMethods {

    LoginForWrongPass loginForWrongPass = new LoginForWrongPass();

    @BeforeMethod
    public void SetUp(){
        createDriver();
        openApplication("https://the-internet.herokuapp.com/login");
    }
    @Test
    public void LoginTest() {
        createReport("Login test");
        loginForWrongPass.verifyText()
                 .enterUsername()
                 .enterWrongPassword()
                .buttonClick()
                .message();


    }
    @AfterMethod
    public static void tearDown(){

    }
}
