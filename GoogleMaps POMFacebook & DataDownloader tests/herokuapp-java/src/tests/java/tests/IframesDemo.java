package src.tests.java.tests;

import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class IframesDemo extends MainMethods {

    Iframe iframe = new Iframe();

    @BeforeMethod
    public void SetUp() {
        createDriver();
        openApplication("https://the-internet.herokuapp.com/iframe");
    }
    @Test
    public void IframesDemo(){
        createReport("Proba Iframes");
        iframe.verifyTittle().clickOnFile().clickOnNewDoc().typeOnIFrame().clickOnFormat().lookingForHeader3();

    }
    @AfterMethod
    public static void tearDown(){

    }
}
