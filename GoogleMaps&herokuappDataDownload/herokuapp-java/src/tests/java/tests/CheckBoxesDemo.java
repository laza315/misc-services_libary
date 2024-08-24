package src.tests.java.tests;


import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class CheckBoxesDemo extends MainMethods {

    CheckBoxes checkBoxes = new CheckBoxes();

    @BeforeMethod
    public void SetUp() {
        createDriver();
        openApplication("https://the-internet.herokuapp.com/checkboxes");
    }

    @Test
    public void CheckBoxPageVerificationAndAction() {
        createReport("CheckBox test");
        checkBoxes.clickOnChechbox1().verifyThathChecbox1IsChecked().clickOnChechbox2().verifyThatCheckbox2IsUnChecked().clickOnChechbox1();

    }
    @AfterMethod
    public static void tearDown(){


    }
}






