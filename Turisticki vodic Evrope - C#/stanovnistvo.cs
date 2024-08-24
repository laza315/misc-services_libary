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
    public partial class stanovnistvo : Form
    {
        public stanovnistvo()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new letovalista();
            newForm.Show();
        }

        private void podaci()
        {
            if (radioButton1.Checked)
            {
                Odgovori.populacija = "da";
                this.Hide();
                var newForm = new provod1();
                newForm.Show();
            }else if (radioButton2.Checked)
            {
                Odgovori.populacija = "ne";
                this.Hide();
                var newForm = new provod1();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new stanovnistvo();
                newForm.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
        }
    }
}
