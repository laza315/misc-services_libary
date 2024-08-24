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
    public partial class Form20 : Form
    {
        public Form20()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new ponuda();
            newForm.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new ponuda2();
            newForm.Show();
        }
    }
}
