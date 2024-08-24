package src.tests.java.tests;

import org.testng.annotations.*;
import src.tests.java.main.*;

public class TableElementsDemo extends MainMethods {

    TableElementsDemo tableElements = new TableElementsDemo();

    @BeforeMethod
    public void SetUp() {
        createDriver();
        openApplication("https://the-internet.herokuapp.com/challenging_dom");
    }
        @Test
        public void TableElements() {




        }

        @AfterMethod
        public static void tearDown() {


    }
    }


