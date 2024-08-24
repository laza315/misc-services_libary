using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Turisticki_vodic_Evrope
{
    public partial class Rezultat : Form
    {

        SqlConnection sc = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=C:\\Users\\Jovan\\turizam.mdf;Integrated Security=True;Connect Timeout=30");

        public Rezultat()
        {
            InitializeComponent();
        }

        public void podaci()
        {

            if (Odgovori.turizam == "leto" && Odgovori.more == "jadransko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '1'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jadransko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '9'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jadransko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '4'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jadransko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '8'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "egejsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '10'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "egejsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '11'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "egejsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '12'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "egejsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '13'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jonsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '2'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jonsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '16'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jonsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '15'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "leto" && Odgovori.more == "jonsko" && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && Odgovori.kuhinja == "da" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '14'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "alpi" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne")  && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "da" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '19'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "alpi" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "da" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '18'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "alpi" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '17'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "alpi" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '20'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "domace" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '24'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "domace" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "ne" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '23'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "domace" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "da" && Odgovori.kultura == "ne")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '21'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }

            else if (Odgovori.turizam == "zima" && Odgovori.planine == "domace" && (Odgovori.skijanje == "da" || Odgovori.skijanje == "ne") && (Odgovori.provod == "da" || Odgovori.provod == "ne") && (Odgovori.populacija == "ne" || Odgovori.populacija == "da") && Odgovori.kuhinja == "da" && Odgovori.kultura == "da")
            {
                SqlCommand cmd = new SqlCommand("select mesto, drzava from destinacije where id = '22'", sc);
                SqlDataAdapter sd = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                sd.Fill(dt);
                dataGridView1.DataSource = dt;
            }
        }

        private void Rezultat_Load(object sender, EventArgs e)
        {
            podaci();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            var newForm = new pocetna();
            newForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
