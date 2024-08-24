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
    public partial class provod1 : Form
    {
        public provod1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new stanovnistvo();
            newForm.Show();
        }

        private void podaci()
        {
            if (radioButton1.Checked)
            {
                Odgovori.provod = "da";
                this.Hide();
                var newForm = new kuhinja();
                newForm.Show();
            }
            else if (radioButton2.Checked)
            {
                Odgovori.provod = "ne";
                this.Hide();
                var newForm = new kuhinja();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new provod1();
                newForm.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
        }
    }
}
