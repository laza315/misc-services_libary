package src.tests.java.pages;

import org.openqa.selenium.*;
import org.testng.annotations.*;
import src.tests.java.main.*;
import com.relevantcodes.extentreports.LogStatus;

import java.io.*;


public class FileDownload extends MainMethods {

    private final By Tittle = By.xpath("//h3[text()='File Downloader']");
    private final By someFileTxt = By.xpath("//a[@href='download/some-file.txt']");

    public FileDownload verifyTittle() {
        verifyThatElementIsVisible(Tittle);
        test.log(LogStatus.INFO, "Tittle is visible");
        return this;
    }

    public FileDownload clickOnFileDwnl() {
        click(someFileTxt);
        test.log(LogStatus.INFO, "[SomeFileText] is clicked");
        return this;
    }
/*
    public FileDownload isFileDownloaded() {
        File dir = new File("C:\Users\User\Downloads", "some-file.txt");
        File[] totalFiles = dir.listFiles();
        for (File file : totalFiles) {
            if (file.getName().equals("someFileTxt")) {
                System.out.println("File is downloaded");
                file.delete();
                return this;
            }

        }
    }   */
}