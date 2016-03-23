#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent),ui(new Ui::MainWindow){
    ui->setupUi(this);
    ui->label_init_errors->setVisible(false);
    this->setWindowTitle("Logorduino");
}

MainWindow::~MainWindow(){delete ui;}

void MainWindow::on_B_connect_clicked(){
    ui->label_init_errors->setVisible(false);
    IP = ui->lineEdit_IP->text();
    bool ok;
    QString PORT = ui->lineEdit_Port->text();
    int port = PORT.toInt(&ok);
    QHostAddress myIP;
    if(IP.isEmpty() || PORT.isEmpty()){                //error input vacio
        ui->label_init_errors->setText("Fill all the spaces");
        ui->label_init_errors->setVisible(true);
    }
    else if(myIP.setAddress(IP) && ok){
        this->secondWindow();
    }else if(!ok){
        ui->label_init_errors->setText("Bad port");     //incorrecto puerto
        ui->label_init_errors->setVisible(true);
    }else{                                              //incorrecta ip
        ui->label_init_errors->setText("Bad ip");
        ui->label_init_errors->setVisible(true);
    }
}
    //TCPCliente->write(ui->lineEdit->text().toLatin1().data(),ui->lineEdit->text().size()); enviar por socket
    //ui->lineEdit->clear();


void MainWindow::secondWindow(){
    if(ui->rB_Bash->isChecked()){                       //vamos por terminal
        this->windowBash= new IBashCode(this);
        bool resp = windowBash->passConfigAndInit(IP,PORT);
        if(resp){
            windowBash->show();
        }else{
            ui->label_init_errors->setText("Error en la conexcion");
        }
    }else if (ui->rB_texteditor->isChecked()){          //vamos por text editor
        this->windowTextEditor = new ITextEditorWindow(this);
        windowTextEditor->show();
    }
}



