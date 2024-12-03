using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Predavanje_2
{
    public partial class Crtanje : Form
    {
        //Globalne promenljive
        bool Crtaj = false;
        PointF Prva = new PointF(0F, 0F);
        PointF Druga = new PointF(0F, 0F);
        PointF PrvaK = new PointF(0F, 0F);
        Pen olovka = new Pen(Color.Black, 1F);
        Brush cetkica = new SolidBrush(Color.Black);
        // niz tacaka

        float[] nizx = new float[1000];
        float[] nizy = new float[1000];

        int brojTacaka = 0;
        string objekat = "";
        public Crtanje()
        {
            InitializeComponent();
            DebljinaLinije.Text = "1.0";
        }

        private void IzborBojeLinije(object sender, EventArgs e)
        {
            PictureBox p = (PictureBox)sender;
            olovka.Color = p.BackColor;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void CrtanjeKeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }

        private void IzborBojeIspune(object sender, EventArgs e)
        {
            PictureBox p = (PictureBox)sender;
            cetkica = new SolidBrush(p.BackColor);
        }

        private void Click_on_plus(object sender, EventArgs e)
        {
            float broj = float.Parse(DebljinaLinije.Text);
            broj = broj + 0.5F;
            if (broj > 5F)
                broj = 5F;
            DebljinaLinije.Text = broj.ToString("0.00"); //u 2 decimale
            olovka.Width = broj;
        }

        private void Click_on_minus(object sender, EventArgs e)
        {
            float broj = float.Parse(DebljinaLinije.Text);
            broj = broj - 0.5F;
            if (broj < 0.5F)
                broj = 0.5F;
            DebljinaLinije.Text = broj.ToString("0.00");//konverzija broja u string sa 2 decimale
            olovka.Width = broj;
        }

        private void IzabraniObjekat(object sender, EventArgs e)
        {
            Button b = (Button)sender;
            string tekst = b.Text.ToString().Trim(); // ovo ce da cita vrednost stringa iz dugmica
            if (tekst == "Linija")
                objekat = "L";
            if (tekst == "Pravougaonik")
                objekat = "P";
            if(tekst == "Elipsa")
                objekat = "E";
            if(tekst == "Krug")
                objekat = "K";
            if (tekst == "Kriva")
                objekat = "Kr";
            if (tekst == "Poligon")
                objekat = "Po";

        }

        private void Ocisti_click(object sender, EventArgs e)
        {
            Graphics g = RadnaPovrsina.CreateGraphics();
            g.Clear(Color.White);

        }

        private void RadnaPovrsina_MouseDown(object sender, MouseEventArgs e)
        {
            Crtaj = true;
            Prva = e.Location; // X i Y koordinatu
            PrvaK =  e.Location; // X i Y koord
            nizx[brojTacaka] = Prva.X;
            nizy[brojTacaka] = Prva.Y;
            brojTacaka++;
            tekuceX.Text = Prva.X.ToString("0.00");
            tekuceY.Text = Prva.Y.ToString("0.00");


        }

        private void RadnaPovrsina_MouseMove(object sender, MouseEventArgs e)
        {
            PointF DrugaK = e.Location; // X i Y koordinatu
            tekuceX.Text = DrugaK.X.ToString("0.00"); // vraca X koordinatu iz Location metode od PointF
            tekuceY.Text = DrugaK.Y.ToString("0.00"); // vraca Y
            if(Crtaj)
            {
                // Graphics g =  RadnaPovrsina.CreateGraphics();
            }
        }

        private void RadnaPovrsina_MouseUo(object sender, MouseEventArgs e)
        {
            Crtaj = false;
            PrvaK.X = -1F;
            PrvaK.Y = -1F;
            Druga = e.Location;
            if (objekat=="L")
            {
                Graphics g = RadnaPovrsina.CreateGraphics();
                g.DrawLine(olovka, Prva, Druga);
            }
            if (objekat=="P") 
            {
                Graphics g = RadnaPovrsina.CreateGraphics();
                g.DrawRectangle(olovka, Prva.X, Prva.Y, e.X - Prva.X, e.Y - Prva.Y);
                g.FillRectangle(cetkica,Prva.X + olovka.Width, Prva.Y + olovka.Width, e.X - Prva.X - olovka.Width, e.Y - Prva.Y - olovka.Width);
                g.Dispose();

            }
            if (objekat == "E")
            {
                Graphics g = RadnaPovrsina.CreateGraphics();
                g.DrawEllipse(olovka, Prva.X, Prva.Y, e.X - Prva.X, e.Y - Prva.Y);
                g.FillEllipse(cetkica, Prva.X + olovka.Width, Prva.Y + olovka.Width, e.X - Prva.X - olovka.Width, e.Y - Prva.Y - olovka.Width);
                g.Dispose();
            }
            if (objekat == "K")
            {
                Graphics g = RadnaPovrsina.CreateGraphics();
                //prvo se definise centar, zatim se definise pravvougaonik kao za elipsu a==b
                g.DrawEllipse(olovka, Prva.X, Prva.Y, 2 * (Druga.X - Prva.X), 2 * (Druga.X - Prva.X));
                g.FillEllipse(cetkica, Prva.X + olovka.Width, Prva.Y + olovka.Width, 2 * (e.X - Prva.X), 2 * (e.X - Prva.X));
                g.Dispose();
            }
        }
    }

}
