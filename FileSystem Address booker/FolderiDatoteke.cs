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
    public partial class FolderiDatoteke : Form
    {
        private RukovanjeFolderima rukovanjeFolderima;
        static string IzabraniHD = "";
        static string IzabranaPutanjaFoldera = "";
        public FolderiDatoteke()
        {
            InitializeComponent();
            Status.Text = String.Empty;
            rukovanjeFolderima = new RukovanjeFolderima();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void FolderiDatoteke_KeyDown(object sender, KeyEventArgs e)
        {
            if(e.KeyCode==Keys.Escape)
                this.Close();
        }

        private void IsprazniStatus(object sender, EventArgs e)
        {
            Status.Text = string.Empty;
        }

        private void button1_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Povratak na pocetni ekran!";
        }

        private void Diskovi_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Izabrati LOGICKI disk!";
        }

        private void button2_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Za ucitavanje foldera/podfoldera izabranog diska!";
        }

        private void izbfolder_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Uneti naziv foldera koji se kreira!";
        }

        private void button3_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Kreiranje foldera iz gornjeg text box-a!";
        }

        private void Stablo_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Sadrzaj izabranog diska: lista foldera i podfoldera!";
        }

        private void ListaFajlova_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "  Lista fajlova izabranog foldera!";
        }

        private void FolderiDatoteke_Load(object sender, EventArgs e)
        {
            try
            {
                DriveInfo[] DiskoviNiz = DriveInfo.GetDrives();
                foreach (DriveInfo disk in DiskoviNiz)
                {
                    if (disk.IsReady)
                    {
                        Diskovi.Items.Add(disk.Name);
                    }
                }
            }
            catch (Exception)
            {
                throw;
            }
            //Indeksiranje za nizove pocinje od 0
            //Diskovi.SelectedIndex = 0;
            for (int i = 0; i < Diskovi.Items.Count; i++)
            {
                string disk = Diskovi.Items[i].ToString().Trim();//"D:\  "->"D:\"
                if (disk.Contains("C") || disk.Contains("c"))
                {
                    Diskovi.SelectedIndex = i;
                    break;
                }
            }
        }

        private void Diskovi_SelectedIndexChanged(object sender, EventArgs e)
        {
            IzabraniHD = Diskovi.SelectedItem.ToString().Trim();
            textBox1.Text = IzabraniHD;
        }
        private void DodajPodfoldere(TreeNode cvor)
        {
            string putanjafoldera = cvor.Tag.ToString().Trim();
            var podfolderi = rukovanjeFolderima.PreuzmiPodfoldere(putanjafoldera);//niz podfoldera
            foreach(var subF in podfolderi)
            {
                TreeNode subNode = new TreeNode(Path.GetFileName(subF))
                { 
                    Tag=subF        
                };
                cvor.Nodes.Add(subNode);
                DodajPodfoldere(subNode);
            }
        }
        private void PopuniStablo(string putanja)
        {
            Stablo.Nodes.Clear();
            TreeNode koren = new TreeNode(putanja)
            {
                Tag = putanja
            };
            Stablo.Nodes.Add(koren);
            //Podfolderima
            DodajPodfoldere(koren);
            Stablo.ExpandAll();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            rukovanjeFolderima.UcitajFoldere(IzabraniHD);
            PopuniStablo(IzabraniHD);
        }

        private void PopuniListuFajlova(string putanja)
        {
            ListaFajlova.Items.Clear();
            var fajlovi = rukovanjeFolderima.PreuzmiFajlove(putanja);
            foreach(var fajl in fajlovi)
            {
                string ime_fajla = Path.GetFileName(fajl);
                ListaFajlova.Items.Add(ime_fajla);
            }
            ListaFajlova.Refresh();
        }
        private void Stablo_AfterSelect(object sender, TreeViewEventArgs e)
        {
            IzabranaPutanjaFoldera = e.Node.Tag.ToString().Trim();
            PopuniListuFajlova(IzabranaPutanjaFoldera);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string NoviPF = izbfolder.Text.Trim();
            if(string.IsNullOrWhiteSpace(NoviPF))
            {
                MessageBox.Show("UNETI NAZIV PODFOLDERA", "Greska UNOSA", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                string putanja = IzabranaPutanjaFoldera + "\\" + NoviPF;
                if(Directory.Exists(putanja))
                {
                    MessageBox.Show("PODFOLDER POSTOJI", "Greska UNOSA", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
                else
                {
                    Directory.CreateDirectory(putanja);
                    MessageBox.Show($"PODFOLDER '{NoviPF}' uspesno kreiran na :\n{putanja}", "USPESNO KREIRANIO", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    button2.PerformClick();
                }
            }
        }

        private void ListaFajlova_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
