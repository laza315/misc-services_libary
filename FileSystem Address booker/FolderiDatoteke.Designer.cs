namespace Predavanje_2
{
    partial class FolderiDatoteke
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
            this.panel2 = new System.Windows.Forms.Panel();
            this.Status = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.Diskovi = new System.Windows.Forms.ComboBox();
            this.button2 = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.izbfolder = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.button3 = new System.Windows.Forms.Button();
            this.Stablo = new System.Windows.Forms.TreeView();
            this.ListaFajlova = new System.Windows.Forms.ListBox();
            this.panel2.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.Status);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel2.Location = new System.Drawing.Point(0, 694);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(914, 32);
            this.panel2.TabIndex = 3;
            // 
            // Status
            // 
            this.Status.AutoSize = true;
            this.Status.Location = new System.Drawing.Point(3, 4);
            this.Status.Name = "Status";
            this.Status.Size = new System.Drawing.Size(60, 24);
            this.Status.TabIndex = 0;
            this.Status.Text = "label1";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.button1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(914, 37);
            this.panel1.TabIndex = 2;
            // 
            // button1
            // 
            this.button1.Dock = System.Windows.Forms.DockStyle.Right;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button1.ForeColor = System.Drawing.Color.Red;
            this.button1.Location = new System.Drawing.Point(885, 0);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(29, 37);
            this.button1.TabIndex = 0;
            this.button1.Text = "X";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            this.button1.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.button1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.button1_MouseMove);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 70);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(106, 24);
            this.label1.TabIndex = 4;
            this.label1.Text = "Izabrati disk";
            // 
            // Diskovi
            // 
            this.Diskovi.FormattingEnabled = true;
            this.Diskovi.Location = new System.Drawing.Point(127, 70);
            this.Diskovi.Name = "Diskovi";
            this.Diskovi.Size = new System.Drawing.Size(121, 32);
            this.Diskovi.TabIndex = 5;
            this.Diskovi.SelectedIndexChanged += new System.EventHandler(this.Diskovi_SelectedIndexChanged);
            this.Diskovi.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.Diskovi.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Diskovi_MouseMove);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(265, 70);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(182, 32);
            this.button2.TabIndex = 6;
            this.button2.Text = "Ucitati foldere";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            this.button2.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.button2.MouseMove += new System.Windows.Forms.MouseEventHandler(this.button2_MouseMove);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(466, 74);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(120, 24);
            this.label2.TabIndex = 7;
            this.label2.Text = "Izabrati folder";
            // 
            // izbfolder
            // 
            this.izbfolder.Location = new System.Drawing.Point(628, 73);
            this.izbfolder.Name = "izbfolder";
            this.izbfolder.Size = new System.Drawing.Size(250, 29);
            this.izbfolder.TabIndex = 8;
            this.izbfolder.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.izbfolder.MouseMove += new System.Windows.Forms.MouseEventHandler(this.izbfolder_MouseMove);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(131, 117);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 29);
            this.textBox1.TabIndex = 9;
            this.textBox1.Visible = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(15, 169);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(141, 24);
            this.label3.TabIndex = 10;
            this.label3.Text = "Lista FOLDERA";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(466, 169);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(137, 24);
            this.label4.TabIndex = 11;
            this.label4.Text = "Lista FAJLOVA";
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(628, 117);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(250, 32);
            this.button3.TabIndex = 12;
            this.button3.Text = "Kreiraj podfolder";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            this.button3.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.button3.MouseMove += new System.Windows.Forms.MouseEventHandler(this.button3_MouseMove);
            // 
            // Stablo
            // 
            this.Stablo.Location = new System.Drawing.Point(19, 209);
            this.Stablo.Name = "Stablo";
            this.Stablo.Size = new System.Drawing.Size(427, 460);
            this.Stablo.TabIndex = 13;
            this.Stablo.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.Stablo_AfterSelect);
            this.Stablo.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.Stablo.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Stablo_MouseMove);
            // 
            // ListaFajlova
            // 
            this.ListaFajlova.FormattingEnabled = true;
            this.ListaFajlova.ItemHeight = 24;
            this.ListaFajlova.Location = new System.Drawing.Point(470, 209);
            this.ListaFajlova.Name = "ListaFajlova";
            this.ListaFajlova.Size = new System.Drawing.Size(415, 460);
            this.ListaFajlova.TabIndex = 14;
            this.ListaFajlova.SelectedIndexChanged += new System.EventHandler(this.ListaFajlova_SelectedIndexChanged);
            this.ListaFajlova.MouseLeave += new System.EventHandler(this.IsprazniStatus);
            this.ListaFajlova.MouseMove += new System.Windows.Forms.MouseEventHandler(this.ListaFajlova_MouseMove);
            // 
            // FolderiDatoteke
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(914, 726);
            this.ControlBox = false;
            this.Controls.Add(this.ListaFajlova);
            this.Controls.Add(this.Stablo);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.izbfolder);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.Diskovi);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.ForeColor = System.Drawing.Color.Navy;
            this.KeyPreview = true;
            this.Name = "FolderiDatoteke";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Predavanje 3: Primer rada sa folderima i datotekama                              " +
    "       Esc - povratak na prethodni ekran";
            this.Load += new System.EventHandler(this.FolderiDatoteke_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FolderiDatoteke_KeyDown);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label Status;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox Diskovi;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox izbfolder;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TreeView Stablo;
        private System.Windows.Forms.ListBox ListaFajlova;
    }
}