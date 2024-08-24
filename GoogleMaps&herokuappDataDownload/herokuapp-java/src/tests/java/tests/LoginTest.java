package src.tests.java.tests;


import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class LoginTest extends MainMethods {

    LoginPage loginPage = new LoginPage();
    SuccessLog successLog = new SuccessLog();

@BeforeMethod
    public void SetUp(){
        createDriver();
        openApplication("https://the-internet.herokuapp.com/login");
    }
    @Test
    public void LoginTest() {
        createReport("Login test");
        loginPage.verifyText()
                .enterUsername()
                .enterPassword()
                .button().clickingOnLogOutButton().verifyThatLogOutTittleIsVisible();

    }
    @Test
    public void SuccessTest() {
        createReport("Success test");
        successLog.verifyThatLoginTittleIsVisible();



    }
@AfterMethod
        public static void tearDown(){

        }

}
