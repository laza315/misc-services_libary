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
    public partial class vrsteTurizma : Form
    {
        public vrsteTurizma()
        {
            InitializeComponent();
        }

        private void podaci()
        {
            if (radioButton1.Checked == true) {

                Odgovori.turizam = "leto";
                var newForm = new letovalista();
                newForm.Show();
            }
           else if (radioButton2.Checked == true)
            {

                Odgovori.turizam = "zima";
                var newForm = new planinskiVenci();
                newForm.Show();
            }


            else if (radioButton1.Checked == false && radioButton2.Checked == false )
            {
                MessageBox.Show("Izaberite jedno od ponudjenih odgovora!");
                var newForm = new vrsteTurizma();
                newForm.Show();

            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
            var newForm = new pocetna();
            newForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            podaci();
            this.Close();
           
        }
      






    }
}
