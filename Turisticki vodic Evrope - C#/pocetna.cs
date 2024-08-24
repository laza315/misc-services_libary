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
    public partial class pocetna : Form
    {
        public pocetna()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm =  new vrsteTurizma();
            newForm.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("U nedoumici ste oko planiranja Vašeg puta?" +
                "Mi Vam nudimo jednostavan način kako da u par kratkih koraka odaberete idealnu destinaciju za Vas i vase bližnje." +
                "Kroz nekoliko formalnih pitanja lične prirode, dobićete turističke predloge kao i optimalnu sumu novca koju je potrebno izdvojiti za Vaš put. Bilo da se radi o letovanju, zimovanju, soskom turizmu ili poseti Evropi generalno, sigurni smo da ćete uživati." +
                "Srećno!", " Saznaj vise", MessageBoxButtons.OK, MessageBoxIcon.None) == DialogResult.OK);
        }
        
          
        
    }
}
