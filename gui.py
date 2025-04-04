import main
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPixmap
from Ui_untitled import Ui_Riemann

class MyWindow(QWidget, Ui_Riemann):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)

    def button_click(self):
        self.p1 = float(self.p1_edt.text())
        self.p2 = float(self.p2_edt.text())
        self.u1 = float(self.u1_edt.text())
        self.u2 = float(self.u2_edt.text())
        self.rho1 = float(self.rho1_edt.text())
        self.rho2 = float(self.rho2_edt.text())
        self.t = float(self.t_edt.text())
        main.main(self.t, self.u1, self.u2, self.rho1, self.rho2, self.p1, self.p2)
        self.tittle_lab.setText(str('p1='+str(self.p1)+',p2='+str(self.p2)+',u1='+str(self.u1)+',u2='+str(self.u2)+',rho1='+str(self.rho1)+',rho2='+str(self.rho2)+'\nt='+str(self.t)))
        pixmap = QPixmap("Riemann.png")
        self.pic_lab.setPixmap(pixmap)
        self.pic_lab.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

