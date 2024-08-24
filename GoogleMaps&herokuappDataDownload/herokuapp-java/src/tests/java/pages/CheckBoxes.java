package src.tests.java.pages;

import org.openqa.selenium.*;
import com.relevantcodes.extentreports.LogStatus;
import src.com.selenium.*;
import src.tests.java.main.*;


    public class CheckBoxes extends MainMethods {
        private final By checkbox1 = By.xpath("//input[@type='checkbox'][1]");
        private final By checkbox2 = By.xpath("//input[@type='checkbox'][2]");
        private final By checkbox1IsClicked = By.xpath("//input[@type='checkbox' and @checked='']");

        public CheckBoxes clickOnChechbox1() {
            click(checkbox1);
            test.log(LogStatus.INFO, "Button [checkbox 1] is clicked");
            return this;
        }

        public CheckBoxes clickOnChechbox2() {
            click(checkbox2);
            test.log(LogStatus.INFO, "Button [checkbox 2] is clicked");
            return this;
        }

        public CheckBoxes verifyThathChecbox1IsChecked() {
            verifyThatElementIsVisible(checkbox1IsClicked);
            test.log(LogStatus.INFO, "Button [checkbox 1] is checked");
            return this;
        }

        public CheckBoxes verifyThatCheckbox2IsUnChecked() {
            verifyThatElementIsVisible(checkbox2);
            test.log(LogStatus.INFO, "Button [checkbox 2] is unchecked");
            return this;
        }


    }

