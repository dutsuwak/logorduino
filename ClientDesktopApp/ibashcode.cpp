#include "ibashcode.h"
#include "ui_ibashcode.h"

IBashCode::IBashCode(QWidget *parent) :QMainWindow(parent),ui(new Ui::IBashCode){

    ui->setupUi(this);
    this->setWindowTitle("Logorduino command promt");
    this->mySocket = new QTcpSocket();

}


IBashCode::~IBashCode(){delete ui;}

bool IBashCode::passConfigAndInit(QString pIp, int pPort){
    try{
        QString p = QString::number(pPort);
        //qDebug() << "Ip: " << pIp << ".";
        //qDebug() << "Port: " << p << ".";
        mySocket->connectToHost(pIp,pPort);
    }catch (QString e){
        return false;
    }
    return true;
}
void IBashCode::on_Bsend_clicked(){

    QString command = ui->lineEditCode->text();
    ui->lineEditCode->setText("");
    ui->textBrowser->append("<<<"+command);
    if(!command.isEmpty()){
        mySocket->write(command.toLatin1().data(), command.size());
    }
}

void IBashCode::on_Bexit_clicked(){
    this->mySocket->close();
}

void IBashCode::on_lineEditCode_returnPressed(){
    this->on_Bsend_clicked();
}
