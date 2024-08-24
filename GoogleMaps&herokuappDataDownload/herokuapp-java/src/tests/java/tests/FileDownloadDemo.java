/* package src.tests.java.tests;

import org.openqa.selenium.*;
import org.testng.annotations.*;
import src.tests.java.main.*;
import src.tests.java.pages.*;

public class FileDownloadDemo extends MainMethods {

    FileDownload fileDownload = new FileDownload();

    @BeforeMethod
    public void SetUp() {
        createDriver();
        openApplication("https://the-internet.herokuapp.com/download");
    }
    @Test
    public  void FileDwnl(){
        createReport("File Download test");
        fileDownload.verifyTittle().clickOnFileDwnl().isFileDownloaded();


    }




    @AfterMethod
    public static void tearDown(){


    }

}
*/