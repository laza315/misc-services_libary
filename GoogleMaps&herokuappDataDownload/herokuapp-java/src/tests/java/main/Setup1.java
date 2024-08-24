package src.tests.java.main;

import com.relevantcodes.extentreports.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.testng.*;
import org.testng.annotations.*;

public class Setup1 {
    public static WebDriver driver;

    public static ExtentReports report;
    public static ExtentTest test;

    public WebDriver getDriver() {
        return driver;
    }

    public WebDriver createDriver() {

        try {
            if (getDriver() != null) {
                return getDriver();
            }
            String DRIVER_NAME_CHROME = "webdriver.chrome.driver";
            System.setProperty(DRIVER_NAME_CHROME, Paths.DRIVER_PATH);
            ChromeOptions options = new ChromeOptions();
            options.addArguments("disable-infobars");
            options.addArguments("--disable-extensions");
            options.addArguments("start-maximized");
            options.addArguments("--disable-notifications");

            return driver = new ChromeDriver(options);
        } catch (SeleneseException e) {
            throw new SeleneseException("The driver is not created");
        }
    }

    public void quitDriver() {
        driver.quit();
        driver = null;
    }

    public void openApplication(String URL){
        getDriver().get(URL);
    }

    public void createReport(String testName) {

        report = new ExtentReports(Paths.FOLDER_REPORT_PATH, false);
        report.addSystemInfo("OS", "Ubuntu 20.04.2 LTS");
        report.addSystemInfo("Browser", "Chrome 89");
        report.addSystemInfo("Tester name", "Petar98");
        report.addSystemInfo("URL", "");
        report.addSystemInfo("Date", "3.28.2022.");
        test = report.startTest(testName);
    }

    @AfterMethod
    public void tearDown(ITestResult testResult) throws Exception {
        if (testResult.getStatus() == ITestResult.FAILURE) {
            quitDriver();
            openApplication("http://the-internet.herokuapp.com/");

            test.log(LogStatus.FAIL, "The following test case FAILED: " + testResult.getName());
            test.log(LogStatus.FAIL, "The following method FAILED: " + testResult.getThrowable());
        } else if (testResult.getStatus() == ITestResult.SUCCESS) {
            test.log(LogStatus.PASS, "The following test case PASSED:" + testResult.getName());
        } else if (testResult.getStatus() == ITestResult.SKIP) {
            test.log(LogStatus.PASS, "The following test case SKIPPED: " + testResult.getName());
        }

        report.endTest(test);
        report.flush();
    }

}
