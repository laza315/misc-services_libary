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
    public partial class kultura2 : Form
    {
        public kultura2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new stanovnistvo2();
            newForm.Show();
        }

        private void podaci()
        {
            if (radioButton1.Checked)
            {
                Odgovori.kultura = "da";
                this.Hide();
                var newForm = new ponuda2();
                newForm.Show();
            }
            else if (radioButton2.Checked)
            {
                Odgovori.kultura = "ne";
                this.Hide();
                var newForm = new ponuda2();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new kultura2();
                newForm.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new kuhinja2();
            newForm.Show();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            podaci();
        }
    }
}
