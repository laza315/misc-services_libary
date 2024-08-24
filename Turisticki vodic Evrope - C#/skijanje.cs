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
    public partial class skijanje : Form
    {
        public skijanje()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new planinskiVenci();
            newForm.Show();
        }

        private void podaci()
        {
            if (radioButton1.Checked)
            {
                Odgovori.skijanje = "da";
                this.Hide();
                var newForm = new provod2();
                newForm.Show();
            }else if (radioButton2.Checked)
            {
                Odgovori.skijanje = "ne";
                this.Hide();
                var newForm = new provod2();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new skijanje();
                newForm.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
        }
    }
}
