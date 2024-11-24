using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;//za input/output: rad sa folderima/podfolderima, odnosno datotekama

public class RukovanjeFolderima
{
    public Dictionary<string,List<string>> SadrzajFoldera { get; private set; }

    public RukovanjeFolderima()
    {
        SadrzajFoldera = new Dictionary<string, List<string>>();
    }

    //Publikovanje 
    private void PublikujSadrzajFoldera(string putanja)
    {
        // Dodavanje foldera i fajlova u Dictionary SadrzajFoldera
        var folderinfo=new DirectoryInfo(putanja);
        if((folderinfo.Attributes & FileAttributes.Hidden) !=FileAttributes.Hidden && (folderinfo.Attributes & FileAttributes.Hidden) != FileAttributes.System)
        {
            var fajlovi = Directory.GetFiles(putanja);
            SadrzajFoldera[putanja] = new List<string>(fajlovi);
            var podFolderi = Directory.GetDirectories(putanja); 
            foreach(var podFolder in podFolderi)
            {
                PublikujSadrzajFoldera(podFolder);
            }
        }
    }
    //Ucitavanje foldera
    public void UcitajFoldere(string putanja)
    {
        if (!Directory.Exists(putanja))
            throw new DirectoryNotFoundException("Izabrani direktorijum / drive ne postoji!!!");
        SadrzajFoldera.Clear();
        //Publikovanje:
        PublikujSadrzajFoldera(putanja);
    }
    //Funkcija za peuzimanje fajlova
    public List<string>PreuzmiFajlove(string putanja)
    {
        if (SadrzajFoldera.ContainsKey(putanja))
            return SadrzajFoldera[putanja];
        return new List<string>();
    }
    //Funkcija za pruzimenja PodFoldera
    public List<string> PreuzmiPodfoldere(string putanja)
    {
        var podfolderi = new List<string>();    
        foreach(var folder in SadrzajFoldera.Keys)
        {
            if(folder.StartsWith(putanja) && folder !=putanja)
                podfolderi.Add(folder); 
        }
        return podfolderi;
    }
}
