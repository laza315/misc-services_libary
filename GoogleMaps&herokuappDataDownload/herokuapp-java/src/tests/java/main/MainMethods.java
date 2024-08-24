package src.tests.java.main;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class MainMethods extends Setup1 {
    public static Long index = null;
    public static String email;
    public static String trenutno;

    public void verifyThatElementIsVisible(By locator) {
        WebDriverWait wait = new WebDriverWait(getDriver(), 10);
        wait.until(ExpectedConditions.presenceOfElementLocated(locator));
    }
    public void mouseHover(By locator){
        WebElement element = driver.findElement(By.xpath(""));
        Actions action = new Actions(driver);
        action.moveToElement(element).perform();

    }

    public void verifyTableElementPresents(By locator){
        WebElement cell = driver.findElement(By.xpath(""));
    }



    public void verifyThatElementIsNotVisible(By locator) {
        WebDriverWait wait = new WebDriverWait(getDriver(), 5);
        wait.until(ExpectedConditions.invisibilityOfElementLocated(locator));
    }

    public void verifyThatSomethinhIsVisibleAfterRefresh(By locator) throws Exception {
        boolean elementVisible = checkIfElementIsVisible(locator);
        int counter = 0;
        while (!elementVisible && counter <= 3) {
            getDriver().navigate().refresh();
            Thread.sleep(700);
            counter++;
            elementVisible = checkIfElementIsVisible(locator);
        }
        if (elementVisible) {
            System.out.println("The element is visible and correct");
        } else {
            throw new SeleneseException("#### Element is not visible after refresh");

        }
    }

    public void switchToIFrame(By element) {
        WebElement iFrame = getDriver().findElement(element);
        getDriver().switchTo().frame(iFrame);
    }
    public void dragAndDrop(By element){
        WebElement draggable = driver.findElement(By.xpath("locator"));
        WebElement dropable = driver.findElement(By.xpath("locator"));
        new Actions(driver)
                .dragAndDrop(draggable, dropable)
                .perform();
    }


    public void click(By locator) {
        try {
            WebDriverWait wait = new WebDriverWait(getDriver(), 5);
            wait.until(ExpectedConditions.elementToBeClickable(locator)).click();
        } catch (Exception e) {
            throw new SeleneseException("pucaj");
        }

    }

    public void clicWithAction(By locator) throws SeleneseException {
        try {
            Thread.sleep(300);
            WebElement el = getDriver().findElement(locator);
            Actions act = new Actions(getDriver());
            act.moveToElement(el).click().build().perform();
            Thread.sleep(300);
        } catch (Exception e) {
            throw new SeleneseException("Button is not clicked");
        }
    }

    public void type(By locator, String text) {
        WebDriverWait wait = new WebDriverWait(getDriver(), 10);
        wait.until(ExpectedConditions.presenceOfElementLocated(locator)).sendKeys(text);
    }

    public String incrementNumberInFile() {

        File file = new File("A:/firstProject/folder/indexOfEmail.txt");

        if (!file.exists()) {
            index = 1L;
        } else {
            try (BufferedReader bf = Files.newBufferedReader(file.toPath())) {
                index = Long.parseLong(bf.readLine());
            } catch (Exception e) {
                throw new SeleneseException(("Error while reading an index from the file"));
            }
        }
        try (FileWriter fileWriter = new FileWriter(file)) {
            index++;
            fileWriter.write(index.toString());
        } catch (Exception e) {
            throw new SeleneseException(("Error while writing a new index in the file"));
        }
        return index.toString();
    }

    public Boolean checkIfElementIsVisible(By locator) {
        boolean isVisible = true;
        try {
            getDriver().findElement(locator);
        } catch (Exception e) {
            isVisible = false;
        }
        return isVisible;
    }


    public String createEmail() {
        incrementNumberInFile();
        String emailPrefix = "prefix";
        emailPrefix += index;
        email = "petarStudent+" + emailPrefix + "@protonmail.com";
        trenutno = email;
        return email;
    }


    public void clear(By locator) {
        WebDriverWait wait = new WebDriverWait(getDriver(), 5);
        wait.until(ExpectedConditions.presenceOfElementLocated(locator)).clear();
    }

    public void refreshPage() {
        getDriver().navigate().refresh();
    }

    public void waitForPageToBeLoaded() {
        WebDriverWait wait = new WebDriverWait(getDriver(), 5);
        wait.until(webDriver -> ((JavascriptExecutor) getDriver()).executeScript("return document.readyState").equals("complete"));
    }

    public void switchToTab(int numberOfTab) {
        ArrayList<String> tabs2 = new ArrayList<>(getDriver().getWindowHandles());
        getDriver().switchTo().window(tabs2.get(numberOfTab));
    }

    public void closeTabAndSwitchToMain(int closeTab, int switchTab) {
        Set<String> handlesSet = getDriver().getWindowHandles();
        List<String> handlesList = new ArrayList<>(handlesSet);
        getDriver().switchTo().window(handlesList.get(closeTab));
        getDriver().close();
        getDriver().switchTo().window(handlesList.get(switchTab));
    }

    public static String getLastModifiedFileName(String directoryFilePath) {
        File directory = new File(directoryFilePath);
        File[] files = directory.listFiles(File::isFile);
        long lastModifiedTime = Long.MIN_VALUE;
        File chosenFile = null;

        if (files != null) {
            for (File file : files) {
                if (file.lastModified() > lastModifiedTime) {
                    chosenFile = file;
                    lastModifiedTime = file.lastModified();
                }
            }

        }
        return directoryFilePath;
    }

        }