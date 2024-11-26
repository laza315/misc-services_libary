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
using System.Diagnostics.Eventing.Reader;

namespace Predavanje_2
{
    public partial class Adresar : Form
    {
        static string dat = @"C:\Users\User\Desktop\services-hub\FileSystem Address booker\Datoteke\kontakti.txt";
        public Adresar()
        {
            InitializeComponent();
            Status.Text = string.Empty;
            PopuniListu();
        }
        private void PopuniListu()
        {
            Podaci.Items.Clear();
            string prazno = "----;--------;--------;--------;--------;--------";
            if (File.Exists(@dat)) // Proearava da li postoji txt datoteka sa kontaktima 
            {
                //Metoda RealAllLines

                string[] nizk = File.ReadAllLines(@dat);
                if (nizk.Length > 0) //proveravamo da li se formirao niz, broj elemenata (Length) >0
                {
                    for (int i = 0; i < nizk.Length; i++)
                    {
                        string[] red = nizk[i].Split(';');
                        ListViewItem lw = new ListViewItem(red);
                        Podaci.Items.Add(lw);
                    }
                }
            }
            else
            {
                string[] red = prazno.Split(';');
                ListViewItem lw = new ListViewItem(red);
                Podaci.Items.Add(lw);
            }
            Podaci.Refresh();
        }

        private void Podaci_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Prikaz unetih podataka o kontaktima!!!";
        }

        private void IsprazniStatus(object sender, EventArgs e)
        {
            Status.Text = string.Empty;
        }

        private void Podaci_SelecteIndexChanged(object sender, EventArgs e)
        {

        }

        private void button2_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Pokrecete formu za unos NOVOG kontakta!";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Azuriranje frm = new Azuriranje("D", "", "", "", "", "", "");
            this.Enabled = false;
            frm.ShowDialog();
            this.Enabled = true;

        }

        private void button3_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Pokrecete formu za izmenu postojeceg kontakta!";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (Podaci.SelectedItems.Count == 0) // Zato sto je multiselect == False, mora biti selektovan barem 1 i nijedan vise
            {
                MessageBox.Show("Niste izabrali kontakt iz adresara", "Gresk Izbora", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            else
            {
                string sid = Podaci.SelectedItems[0].SubItems[0].Text.ToString();
                string sime = Podaci.SelectedItems[0].SubItems[1].Text.ToString();
                string sprezime = Podaci.SelectedItems[0].SubItems[2].Text.ToString();
                string smesto = Podaci.SelectedItems[0].SubItems[3].Text.ToString();
                string sadresa = Podaci.SelectedItems[0].SubItems[4].Text.ToString();
                string stelefon = Podaci.SelectedItems[0].SubItems[5].Text.ToString();
                Azuriranje frm = new Azuriranje("I", sid, sime, sprezime, smesto, sadresa, stelefon);
                this.Enabled = false;
                frm.ShowDialog();
                this.Enabled = true;
                PopuniListu();

            }

        }

        private void Adresar_KeyDown(object sender, KeyEventArgs e)

        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (Podaci.SelectedItems.Count == 0)
            {
                MessageBox.Show("Niste izabrali kontakt (koji se uklanja) iz adresara", "Greska izbora", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            else
            {
                DialogResult Odg = MessageBox.Show("Brisanje izabranog kontakta", "Brisanje", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
                if (Odg == DialogResult.Yes)
                {
                    int idToDelete = Int32.Parse(Podaci.SelectedItems[0].SubItems[0].Text.ToString());
                    if (File.Exists(@dat))
                    {
                        string[] nizK = File.ReadAllLines(@dat);
                        File.Delete(@dat);
                        if (nizK.Length > 0)//proveravamo da li se formirao niz, broj elemenata (Length) >0
                        {
                            for (int i = 0; i < nizK.Length; i++)
                            {
                                string[] red = nizK[i].Split(';');//red[0]=IdBroj, red[1]=Ime, ....
                                int ucIdbroj = Int32.Parse(red[0]);
                                if (ucIdbroj != idToDelete)
                                {
                                    //protok podataka za upis u datoteku
                                    StreamWriter sw = new StreamWriter(@dat, true);
                                    sw.WriteLine(nizK[i]);
                                    sw.Close();
                                }
                                else
                                {
                                    // Ako ID brojevi odgovaraju, prikazujemo poruku
                                    MessageBox.Show($"Brišem red sa ID: {idToDelete}");
                                }
                            }
                        }
                    }
                    PopuniListu();
                }

            }
        }
    }
}

