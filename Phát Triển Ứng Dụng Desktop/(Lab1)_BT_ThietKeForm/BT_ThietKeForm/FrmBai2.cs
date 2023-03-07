using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BT_ThietKeForm
{
    public partial class FrmBai2 : Form
    {
        public FrmBai2()
        {
            InitializeComponent();
        }

        private void btnChonHang_Click(object sender, EventArgs e)
        {
            var item = listBox1.SelectedItem;
            listBox2.Items.Add(item);
        }

        private void btnBoHang_Click(object sender, EventArgs e)
        {
            listBox2.Items.Remove(listBox2.SelectedItem);
        }

        private void btnTinhTien_Click(object sender, EventArgs e)
        {
            int soTien = 0;
            //Duyet ds cac mat hang trong listbox2
            // cong don so tien
            foreach(string hang in listBox2.Items)
                switch(hang)
                {
                    case "Chuot":
                        soTien += 10000;
                        break;
                    case "Ban Phim":
                        soTien += 15000;
                        break;
                    case "May in":
                        soTien += 200000;
                        break;
                    case "USB KingMax":
                        soTien += 20000;
                        break;
                }
            // dien giong ten hang da go o listbox1
            lblSoTien.Text = soTien + "dong";

        }
    }
}
