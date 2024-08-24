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
    public partial class planinskiVenci : Form
    {
        public planinskiVenci()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new vrsteTurizma();
            newForm.Show();
        }

        private void podaci()
        {
            if (radioButton3.Checked)
            {
                Odgovori.planine = "alpi";
                this.Hide();
                var newForm = new skijanje();
                newForm.Show();
            }else if (radioButton4.Checked)
           {
                Odgovori.planine = "domace";
                this.Hide();
                var newForm = new skijanje();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Odaberite jedan od ponudjenih odgovara!");
                this.Hide();
                var newForm = new planinskiVenci();
                newForm.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new pocetna();
            newForm.Show();
        }

        private void Forma11_Load(object sender, EventArgs e)
        {

        }
    }
}
