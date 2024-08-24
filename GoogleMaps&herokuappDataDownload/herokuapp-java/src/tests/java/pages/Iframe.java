package src.tests.java.pages;

import org.openqa.selenium.*;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.*;
import src.tests.java.main.*;
import com.relevantcodes.extentreports.LogStatus;

public class Iframe extends MainMethods {

    private final By Tittle = By.xpath("//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']");
    private final By FileName = By.xpath("//span[text()='File']");
    private final By NewDocName = By.xpath("//div[text()='New document']");
    private final By emptyBox = By.xpath("//iframe[@id='mce_0_ifr']");
    private final By inputFieldForText = By.xpath("//body[@id='tinymce']");
    private final By FormatButton = By.xpath("//div[@class='tox-menubar']//button[@class='tox-mbtn tox-mbtn--select']//span[@class= 'tox-mbtn__select-label'][text()='Format']");
    //prekriven je lokator drugim elemntom i ne moze da se klikne
    private final By formatsMouseOver = By.xpath("//div[@text()='Formats']");
    private final By headingsMouseOver = By.xpath("//div[@text()='Headings']");
    private final By header3 = By.xpath("//div[@class='tox-collection__item-label']//h3");

    public Iframe verifyTittle() {
        verifyThatElementIsVisible(Tittle);
        test.log(LogStatus.INFO, "Tittle is visible");
        return this;

    }

    public Iframe clickOnFile() {
        click(FileName);
        test.log(LogStatus.INFO, "[File] is clicked");
        return this;
    }

    public Iframe clickOnNewDoc() {
        click(NewDocName);
        test.log(LogStatus.INFO, "[New Document] is clicked");
        return this;
    }

    public Iframe typeOnIFrame() {
        switchToIFrame(emptyBox);
        type(inputFieldForText, "Iframe Test");
        test.log(LogStatus.INFO, "Text is input in field");
        return this;
    }

    public Iframe clickOnFormat() {
        click(FormatButton);
        test.log(LogStatus.INFO, "Format is clicked");
        return this;
    }

    public Iframe lookingForHeader3() {
        mouseHover(formatsMouseOver);
        mouseHover(headingsMouseOver);
        mouseHover(header3);
        click(header3);
        return this;
    }

}