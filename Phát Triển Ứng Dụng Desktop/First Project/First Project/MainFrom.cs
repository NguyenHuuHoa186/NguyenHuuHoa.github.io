using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace First_Project
{
    public partial class MainFrom : Form
    {
        public MainFrom()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        
        private void MainFrom_Load(object sender, EventArgs e)
        {

        }

        // Click doi vao nut se tu dong tao ban su kien 
        // Khi ta click chuot vao nut chuong trinh se lam gi
        private void bntOK_Click_1(object sender, EventArgs e)
        {
            var tenDaNhap = txtTen.Text;
            MessageBox.Show($"Xin chao ban {tenDaNhap}.Rat vui duoc gap ban");
        }

        //Tren nhap gi duoi sao chep lai
        private void bntSaoChep_Click(object sender, EventArgs e)
        {
            txtSaoChep.Text = txtTen.Text;
        }
        //Sao chep lai k can nut sao chep
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            txtSaoChep.Text = txtTen.Text;  
        }
    }
}
