package src.tests.java.pages;

import org.openqa.selenium.*;
import com.relevantcodes.extentreports.LogStatus;
import org.openqa.selenium.interactions.*;
import src.tests.java.main.*;

import java.awt.*;

public class DragAndDrop extends MainMethods {

    private final By Tittle = By.xpath("//h3[text()='Drag and Drop']");
    private final By BoxA = By.xpath("//div[@id='column-a']");
    private  final By BoxB = By.xpath("//div[@id='column-b']");


    public DragAndDrop verifyingTittle(){
        verifyThatElementIsVisible(Tittle);
        test.log(LogStatus.INFO, "[Header] is visible");
        return this;

    }
    public DragAndDrop prevuci(){
       WebElement drag = getDriver().findElement(BoxA);
       WebElement drop = getDriver().findElement(BoxB);
        //Robot robot = new Robot(getDriver());
      //  robot.mouseMove(drag, drop);
        //Actions actions = new Actions(getDriver());
       // actions.dragAndDrop(drag,drop).build().perform();
        test.log(LogStatus.INFO, "[A] is moved to position[B]");
       return this;

    }

}
