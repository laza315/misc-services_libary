using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Matrix
{
    public partial class Matrix : Form
    {
        static int red = 0;
        static int kol = 0;
        static int[,] mM;
        static int n;
        static int m;
        private ListView Matrica;
        public Matrix()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();   
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string nn = txtn.Text.Trim();
            string mm = txtm.Text.Trim();
            if (string.IsNullOrWhiteSpace(nn) || string.IsNullOrWhiteSpace(mm))
            {
                MessageBox.Show("Enter n, m between 4 & 7", "Parse Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                n = Int32.Parse(nn);
                m = Int32.Parse(mm);
                if(n<4 || n>7 || m<4 || m>7)
                {
                    MessageBox.Show("n & m bust be between 4 & 7", "Parse Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    mM = new int[n, m];
                    Matrica = new ListView
                    {
                        View = View.Details,
                        FullRowSelect = true,
                        GridLines = true,
                        Location = new Point(21,168),
                        //m column, width per column 70
                        Size= new Size((m+1)*70+10,184)
                    };
                    //adding ListView object in form
                    this.Controls.Add( Matrica );
                    for (int i = 0; i <= m; i++)
                    {
                        ColumnHeader kolona = new ColumnHeader
                        {
                            Text = i < m ? $"K {i + 1}" : "SR.V",//title
                            Width = 70
                        };
                        Matrica.Columns.Add( kolona );
                    }
                    label4.Visible= true;
                    broj.Visible= true;
                    button3.Visible = true;
                    label6.Visible = true;
                    MatricaM.Visible= true;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string sBroj=broj.Text.Trim();
            if (string.IsNullOrWhiteSpace(sBroj))
                MessageBox.Show("Please enter some number!!!", "Parse Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            else
            { 
                int iBroj=Int32.Parse(sBroj);
                MatricaM.Text += sBroj + "\t";
                mM[red, kol] = iBroj;
                broj.Text = string.Empty;
                kol++;
                if(kol>=m)
                {
                    //show current row in Matrix object - ListView
                    string[] redic=new string[m+1];
                    int zbir = 0;
                    for(int j = 0;j<m;j++) // this will aggregate avrage values per row, and increase it until the end
                    {
                        redic[j] = mM[red, j].ToString();
                        zbir += mM[red, j];
                    }
                    float aRs = (float)zbir / m;
                    redic[m]=aRs.ToString();
                    ListViewItem lw = new ListViewItem(redic);
                    Matrica.Items.Add(lw);
                    red++;
                    kol = 0;
                }
                if(kol>m)
                {
                    MatricaM.Text += "\r\n";
                }
                if(red>=n)
                {
                    string[] nizs=new string[n];
                    label4.Visible = false;
                    broj.Visible = false;
                    button3.Visible = false;
                    for(int j=0;j<m;j++)
                    {
                        int zbir = 0;
                        for(int k=0;k<n;k++) // summing avrage per column.
                                             // This will go in depth in 1 row until the botom is reached. 
                                             // row remains the same. Step forward is only on column
                        {
                            zbir=zbir+mM[k,j]; 
                        }
                        float aRs=zbir / n;
                        nizs[j]=aRs.ToString();
                    }
                    ListViewItem lw = new ListViewItem(nizs);
                    Matrica.Items.Add(lw);
                }
            }
        }
    }
}
