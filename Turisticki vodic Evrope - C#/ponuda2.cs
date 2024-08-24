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
    public partial class ponuda2 : Form
    {
        public ponuda2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new Form18();
            newForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new Form20();
            newForm.Show();
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new kultura2();
            newForm.Show();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new Rezultat();
            newForm.Show();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
