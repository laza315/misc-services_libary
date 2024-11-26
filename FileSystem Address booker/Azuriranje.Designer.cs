namespace Predavanje_2
{
    partial class Azuriranje
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.button1 = new System.Windows.Forms.Button();
            this.panel2 = new System.Windows.Forms.Panel();
            this.Status = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.ime = new System.Windows.Forms.TextBox();
            this.prezime = new System.Windows.Forms.TextBox();
            this.mesto = new System.Windows.Forms.TextBox();
            this.adresa = new System.Windows.Forms.TextBox();
            this.telefon = new System.Windows.Forms.TextBox();
            this.idbroj = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.button1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(580, 37);
            this.panel1.TabIndex = 5;
            // 
            // button1
            // 
            this.button1.Dock = System.Windows.Forms.DockStyle.Right;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button1.ForeColor = System.Drawing.Color.Red;
            this.button1.Location = new System.Drawing.Point(551, 0);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(29, 37);
            this.button1.TabIndex = 0;
            this.button1.Text = "X";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.Status);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel2.Location = new System.Drawing.Point(0, 418);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(580, 32);
            this.panel2.TabIndex = 6;
            // 
            // Status
            // 
            this.Status.AutoSize = true;
            this.Status.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Status.ForeColor = System.Drawing.Color.Navy;
            this.Status.Location = new System.Drawing.Point(3, 4);
            this.Status.Name = "Status";
            this.Status.Size = new System.Drawing.Size(52, 18);
            this.Status.TabIndex = 0;
            this.Status.Text = "label1";
            this.Status.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Navy;
            this.label1.Location = new System.Drawing.Point(13, 59);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 18);
            this.label1.TabIndex = 7;
            this.label1.Text = "ID broj";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.Navy;
            this.label2.Location = new System.Drawing.Point(13, 119);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(35, 18);
            this.label2.TabIndex = 8;
            this.label2.Text = "Ime";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.ForeColor = System.Drawing.Color.Navy;
            this.label3.Location = new System.Drawing.Point(12, 163);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(70, 18);
            this.label3.TabIndex = 9;
            this.label3.Text = "Prezime";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.ForeColor = System.Drawing.Color.Navy;
            this.label4.Location = new System.Drawing.Point(13, 205);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(55, 18);
            this.label4.TabIndex = 10;
            this.label4.Text = "Mesto";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.ForeColor = System.Drawing.Color.Navy;
            this.label5.Location = new System.Drawing.Point(13, 251);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(60, 18);
            this.label5.TabIndex = 11;
            this.label5.Text = "Adresa";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.ForeColor = System.Drawing.Color.Navy;
            this.label6.Location = new System.Drawing.Point(12, 297);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(64, 18);
            this.label6.TabIndex = 12;
            this.label6.Text = "Telefon";
            // 
            // ime
            // 
            this.ime.Location = new System.Drawing.Point(140, 118);
            this.ime.Name = "ime";
            this.ime.Size = new System.Drawing.Size(213, 20);
            this.ime.TabIndex = 13;
            this.ime.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.ime.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Ime_MouseMove);
            // 
            // prezime
            // 
            this.prezime.Location = new System.Drawing.Point(140, 164);
            this.prezime.Name = "prezime";
            this.prezime.Size = new System.Drawing.Size(294, 20);
            this.prezime.TabIndex = 14;
            this.prezime.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.prezime.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Prezime_MouseMove);
            // 
            // mesto
            // 
            this.mesto.Location = new System.Drawing.Point(140, 206);
            this.mesto.Name = "mesto";
            this.mesto.Size = new System.Drawing.Size(401, 20);
            this.mesto.TabIndex = 15;
            this.mesto.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.mesto.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Mesto_MouseMove);
            // 
            // adresa
            // 
            this.adresa.Location = new System.Drawing.Point(140, 242);
            this.adresa.Multiline = true;
            this.adresa.Name = "adresa";
            this.adresa.Size = new System.Drawing.Size(401, 38);
            this.adresa.TabIndex = 16;
            this.adresa.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.adresa.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Adresa_MouseMove);
            // 
            // telefon
            // 
            this.telefon.Location = new System.Drawing.Point(140, 295);
            this.telefon.Name = "telefon";
            this.telefon.Size = new System.Drawing.Size(401, 20);
            this.telefon.TabIndex = 17;
            this.telefon.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.telefon.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Telefon_MouseMove);
            // 
            // idbroj
            // 
            this.idbroj.Location = new System.Drawing.Point(437, 59);
            this.idbroj.Name = "idbroj";
            this.idbroj.Size = new System.Drawing.Size(104, 20);
            this.idbroj.TabIndex = 18;
            this.idbroj.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.idbroj.MouseMove += new System.Windows.Forms.MouseEventHandler(this.IDBroj_MouseMove);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.ForeColor = System.Drawing.Color.Navy;
            this.button2.Location = new System.Drawing.Point(139, 354);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(207, 41);
            this.button2.TabIndex = 19;
            this.button2.Text = "SACUVAJ";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            this.button2.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.button2.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Sacuvaj_MouseMove);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button3.ForeColor = System.Drawing.Color.Red;
            this.button3.Location = new System.Drawing.Point(352, 354);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(188, 40);
            this.button3.TabIndex = 20;
            this.button3.Text = "OTKAZI!";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Close);
            this.button3.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.button3.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Otkazi_MouseMove);
            // 
            // Azuriranje
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(580, 450);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.idbroj);
            this.Controls.Add(this.telefon);
            this.Controls.Add(this.adresa);
            this.Controls.Add(this.mesto);
            this.Controls.Add(this.prezime);
            this.Controls.Add(this.ime);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Name = "Azuriranje";
            this.Text = "Azuriranje Podataka o kontaktima              ESC - Povratak na predhodni ekran";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Azuriranje_KeyDown);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label Status;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox ime;
        private System.Windows.Forms.TextBox prezime;
        private System.Windows.Forms.TextBox mesto;
        private System.Windows.Forms.TextBox adresa;
        private System.Windows.Forms.TextBox telefon;
        private System.Windows.Forms.TextBox idbroj;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
    }
}