package src.tests.java.tests;

import org.openqa.selenium.*;
import org.openqa.selenium.interactions.*;
import org.testng.annotations.*;
import src.com.selenium.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class DragAndDropDemo extends MainMethods {

       DragAndDrop dragAndDrop = new DragAndDrop();

    @BeforeMethod
    public void SetUp() {
        createDriver();
        openApplication("https://the-internet.herokuapp.com/drag_and_drop");
    }
        @Test
        public void DADDemoTest() {
            createReport("CheckBox test");
            dragAndDrop.verifyingTittle().prevuci();

        }


        @AfterMethod
        public static void tearDown(){


        }
    }

