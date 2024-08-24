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
    public partial class letovalista : Form
    {
        public letovalista()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new vrsteTurizma();
            newForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
            {
                Odgovori.more = "jadransko";
                this.Hide();
                var newForm = new stanovnistvo();
                newForm.Show();
            }
            else if (radioButton2.Checked)
            {
                Odgovori.more = "egejsko";
                this.Hide();
                var newForm = new stanovnistvo();
                newForm.Show();
            }
            else if (radioButton3.Checked)
            {
                Odgovori.more = "jonsko";
                this.Hide();
                var newForm = new stanovnistvo();
                newForm.Show();
            }
            else
            {
                MessageBox.Show("Izaberite jedan od ponudjenih odgovora!");
                this.Hide();
                var newForm = new letovalista();
                newForm.Show();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
