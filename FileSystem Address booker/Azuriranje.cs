using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Predavanje_2
{
    public partial class Azuriranje : Form
    {
        static string dat = @"C:\Users\User\Desktop\services-hub\FileSystem Address booker\Datoteke\kontakti.txt";
        static string akcija;
        public Azuriranje(string StaDaRadi, string id, string sime, string sprezime, string smesto, string sadresa, string stelefon)
            // StaDaRadi: 'D' - dodavanje, 'I' - izmena
        {
            InitializeComponent();
            Status.Text =  string.Empty;
            // zovemo imena labela i dodeljujemo im parametre
            akcija = StaDaRadi;
            idbroj.Text = id;
            ime.Text = sime;
            prezime.Text = sprezime;
            mesto.Text = smesto;
            adresa.Text = sadresa;
            telefon.Text = stelefon;
            PrikazPodataka();
        }

        private void PrikazPodataka()
        {
            if (File.Exists(@dat))
            {
                if (akcija == "D")
                {
                    int max = 0;
                    string[] nizK = File.ReadAllLines(@dat);
                    if (nizK.Length > 0)//proveravamo da li se formirao niz, broj elemenata (Length) >0
                    {
                        for (int i = 0; i < nizK.Length; i++)
                        {
                            string[] red = nizK[i].Split(';');
                            // kreiraj automatski id broj od prvog elementa iz reda
                            int max1 = int.Parse(red[0]);
                            if (max1 > max)
                                max = max1;
                        }

                    }
                    int NoviIdBroj = max + 1;
                    idbroj.Text = NoviIdBroj.ToString();
                }
            }
            else
                idbroj.Text = "1";
        }

        private void Azuriranje_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }

        private void IsprazniStatus(object sender, EventArgs e)
        {
            Status.Text = "     ";
        }

        private void Otkazi_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Ponisti dodavanje kontakta ";
        }

        private void Sacuvaj_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Sacuvaj dodavanje kontakta ";

        }

        private void Telefon_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Unesi Telefon ";
        }

        private void Adresa_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Unesi adresu ";

        }

        private void Mesto_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Unesi Mesto ";

        }

        private void Prezime_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Unesi Prezime ";

        }

        private void Ime_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " Unesi Ime ";

        }

        private void IDBroj_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = " IDbroj se automatski generise ";

        }

        private void Dodavanje()
            //upisujemo u klasu
        {
            Kontakt k = new Kontakt();
            k.IdBroj = Int32.Parse(idbroj.Text);
            int newId = k.IdBroj + 1;
            k.Ime = ime.Text;
            k.Prezime = prezime.Text;
            k.Mesto = mesto.Text;
            k.Adresa = adresa.Text;
            k.Telefon = telefon.Text;
            string Linija = k.Ispis();
            // protok podataka za upis u datoteku
            StreamWriter sw = new StreamWriter(dat, true);
            sw.WriteLine(Linija);
            sw.Close();
            idbroj.Text = newId.ToString();
            ime.Text = "";
            prezime.Text = "";
            mesto.Text = "";
            adresa.Text = "";
            telefon.Text = "";
        }

        private void Izmene()
        {
            Kontakt k = new Kontakt();
            k.IdBroj = Int32.Parse(idbroj.Text);
            k.Ime = ime.Text;
            k.Prezime = prezime.Text;
            k.Mesto = mesto.Text;
            k.Adresa = adresa.Text;
            k.Telefon = telefon.Text;
            string linija = k.Ispis();
            if (File.Exists(@dat))//proverava se da li postoji txt datoteka sa kontaktima
            {
                // upamticemo izmene i smestiti ih u promenljivu nizk
                string[] nizK = File.ReadAllLines(@dat);
                // potom obrisati fajl
                File.Delete(@dat);
                if (nizK.Length > 0)//proveravamo da li se formirao niz, broj elemenata (Length) >0
                {
                    for (int i = 0; i < nizK.Length; i++)
                    {
                        string[] red = nizK[i].Split(';');//red[0]=IdBroj, red[1]=Ime, ....
                        int ucIdbroj = Int32.Parse(red[0]);
                        if (ucIdbroj == k.IdBroj)
                            // uporediti da li se vuce isti ID kontakta,
                            // ako se ispunjava napisi stare podatke iz objekta k 
                        {
                            nizK[i] = linija;
                        }
                        //protok podataka za upis u datoteku
                        StreamWriter sw = new StreamWriter(@dat, true);
                        sw.WriteLine(nizK[i]);
                        sw.Close();
                    }
                }
            }
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (akcija == "D")
                Dodavanje();
            else
                Izmene();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button3_Close(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
