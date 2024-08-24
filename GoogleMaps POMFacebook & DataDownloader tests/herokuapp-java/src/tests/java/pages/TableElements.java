package src.tests.java.pages;

import org.openqa.selenium.*;
import org.openqa.selenium.interactions.*;
import src.tests.java.main.*;

public class TableElements extends MainMethods {

    private final By red6 = By.xpath("//*[@id='content']/div/div/div/div[2]/table/tbody/tr[7]");

    public TableElements proveraElementa() {
        verifyTableElementPresents(red6);
        return this;
    }
}
