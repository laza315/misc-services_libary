using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Predavanje_2
{
    public partial class Pocetna : Form
    {
        public Pocetna()
        {
            InitializeComponent();
            Status.Text = "";
        }

        private void Isprazni_Status(object sender, EventArgs e)
        {
            Status.Text = "";
        }

        private void button1_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Prekid rada sa APLIKACIJOM!";
        }

        private void button2_MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Pokrece formu za rad sa folderima i datotekama!";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Pocetna_KeyDown(object sender, KeyEventArgs e)
        {
            if(e.KeyCode==Keys.Escape)
                Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            FolderiDatoteke frm = new FolderiDatoteke();
            this.Hide();
            frm.ShowDialog();
            this.Show();
        }

        private void Pocetna_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Adresar frm = new Adresar();
            this.Hide();
            frm.ShowDialog();
            this.Show();
        }

        private void button_3MouseMove(object sender, MouseEventArgs e)
        {
            Status.Text = "     Pokrece formu za rad sa rad sa kontaktima!";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Crtanje frm = new Crtanje();
            this.Hide();
            frm.ShowDialog();
            this.Show();
        }
    }
}
