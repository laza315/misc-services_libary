
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Turisticki_vodic_Evrope
{
    
    

    public partial class provod2 : Form
    {
        
        public provod2()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Forma2_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new vrsteTurizma();
            newForm.Show();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new pocetna();
            newForm.Show();
        }

        private void label1_Click_1(object sender, EventArgs e)
        {

        }

        private void podaci()
        {
            if (radioButton1.Checked)
            {
                Odgovori.provod = "da";
                this.Hide();
                var newForm = new stanovnistvo2();
                newForm.Show();
            }
            else if (radioButton2.Checked)
            {
                Odgovori.provod = "ne";
                this.Hide();
                var newForm = new stanovnistvo2();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new provod2();
                newForm.Show();
            }
        }
            private void button1_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new skijanje();
            newForm.Show();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            podaci();
        }
    }
}
