namespace First_Project
{
    partial class MainFrom
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
            this.label1 = new System.Windows.Forms.Label();
            this.txtTen = new System.Windows.Forms.TextBox();
            this.bntOK = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.bntSaoChep = new System.Windows.Forms.Button();
            this.txtSaoChep = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(132, 72);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(99, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Nhap Ten Cua Ban";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // txtTen
            // 
            this.txtTen.Location = new System.Drawing.Point(247, 72);
            this.txtTen.Name = "txtTen";
            this.txtTen.Size = new System.Drawing.Size(100, 20);
            this.txtTen.TabIndex = 1;
            this.txtTen.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // bntOK
            // 
            this.bntOK.Cursor = System.Windows.Forms.Cursors.Default;
            this.bntOK.Location = new System.Drawing.Point(247, 98);
            this.bntOK.Name = "bntOK";
            this.bntOK.Size = new System.Drawing.Size(75, 23);
            this.bntOK.TabIndex = 2;
            this.bntOK.Text = "Xu Ly";
            this.bntOK.UseVisualStyleBackColor = true;
            this.bntOK.Click += new System.EventHandler(this.bntOK_Click_1);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(132, 140);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(72, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Ban Da Nhap";
            // 
            // bntSaoChep
            // 
            this.bntSaoChep.Cursor = System.Windows.Forms.Cursors.Default;
            this.bntSaoChep.Location = new System.Drawing.Point(348, 98);
            this.bntSaoChep.Name = "bntSaoChep";
            this.bntSaoChep.Size = new System.Drawing.Size(75, 23);
            this.bntSaoChep.TabIndex = 2;
            this.bntSaoChep.Text = "Sao Chep";
            this.bntSaoChep.UseVisualStyleBackColor = true;
            this.bntSaoChep.Click += new System.EventHandler(this.bntSaoChep_Click);
            // 
            // txtSaoChep
            // 
            this.txtSaoChep.Location = new System.Drawing.Point(247, 137);
            this.txtSaoChep.Name = "txtSaoChep";
            this.txtSaoChep.Size = new System.Drawing.Size(100, 20);
            this.txtSaoChep.TabIndex = 1;
            this.txtSaoChep.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // MainFrom
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.bntSaoChep);
            this.Controls.Add(this.bntOK);
            this.Controls.Add(this.txtSaoChep);
            this.Controls.Add(this.txtTen);
            this.Controls.Add(this.label1);
            this.Name = "MainFrom";
            this.Text = "Chuong Trinh Dau Tien";
            this.Load += new System.EventHandler(this.MainFrom_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtTen;
        private System.Windows.Forms.Button bntOK;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button bntSaoChep;
        private System.Windows.Forms.TextBox txtSaoChep;
    }
}

