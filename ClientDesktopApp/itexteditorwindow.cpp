#include "itexteditorwindow.h"
#include "ui_itexteditorwindow.h"

ITextEditorWindow::ITextEditorWindow(QWidget *parent) :QMainWindow(parent),ui(new Ui::ITextEditorWindow){
    ui->setupUi(this);
    this->setWindowTitle("Logorduino text code editor");
    this->mySocket = new QTcpSocket();
    this->ui->progressBar->setVisible(false);
    this->ui->label_info->setVisible(false);
    this->ui->label_info->setText("");
}

ITextEditorWindow::~ITextEditorWindow(){delete ui;}

void ITextEditorWindow::on_actionExit_triggered(){
    this->mySocket->close();
    this->close();
}

bool ITextEditorWindow::passConfigAndInit(QString pIp, int pPort){
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

void ITextEditorWindow::setTitlename(QString pName){
    this->setWindowTitle("Logorduino text code editor"+pName);
}

void ITextEditorWindow::on_actionCheck_triggered(){
    if(this->sendCode(ui->plainTextEdit->toPlainText(),false)){
        //revisar si el codigo es correcto;
    }else{
        this->ui->label_info->setVisible(true);
        this->ui->label_info->setText("Error, try again");
    }
}

void ITextEditorWindow::on_actionRun_triggered(){
    if(this->sendCode(ui->plainTextEdit->toPlainText(),true)){
        //revisar si el codigo es correcto
        this->ui->plainTextEdit->clear();

        ui->progressBar->setVisible(true);
        for(int i=0;i<100;i++){
            ui->progressBar->setValue(i);
            QThread::msleep(10);
        }
        ui->progressBar->setVisible(false);
    }else{
        this->ui->label_info->setVisible(true);
        this->ui->label_info->setText("Error, try again");
    }
}

bool ITextEditorWindow::sendCode(QString pCode, bool act){
    if(mySocket->write(pCode.toLatin1().data(),pCode.size())){
        return true;
    }else{
        return false;
    }

}


void ITextEditorWindow::on_actionNew_triggered(){
    this->mFilename="";
    ui->plainTextEdit->setPlainText("");
}

void ITextEditorWindow::on_actionOpen_triggered(){
    QString file = QFileDialog::getOpenFileName(this,"Open a file");

    if(!file.isEmpty()){
        QFile sFile(file);
        if(sFile.open(QFile::ReadOnly|QFile::Text)){
            mFilename = file;
            QTextStream in(&sFile);
            QString text = in.readAll();
            sFile.close();
            ui->plainTextEdit->setPlainText(text);
            ui->label_info->setText("");
        }
    }else{
        ui->label_info->setText("Error al abrir el archivo");
    }
}

void ITextEditorWindow::on_actionSave_triggered(){
    QFile sFile(mFilename);
    if(mFilename==""){
        this->on_actionSave_as_triggered();
    }
    else if(sFile.open(QFile::WriteOnly|QFile::Text)){
        QTextStream out(&sFile);
        out<<ui->plainTextEdit->toPlainText();
        sFile.flush();
        sFile.close();
    }else{
        ui->label_info->setText("Error al guardar");
    }
}

void ITextEditorWindow::on_actionSave_as_triggered(){
    QString file = QFileDialog::getSaveFileName(this,"Save as");

    if(!file.isEmpty()){
       mFilename = file;
        on_actionSave_triggered();
    }else{
        ui->label_info->setText("Error al guardar");
    }
}

void ITextEditorWindow::on_actionCopy_triggered(){
    ui->plainTextEdit->copy();
}

void ITextEditorWindow::on_actionPaste_triggered(){
    ui->plainTextEdit->paste();
}

void ITextEditorWindow::on_actionCut_triggered(){
    ui->plainTextEdit->cut();
}


void ITextEditorWindow::on_actionUndo_triggered(){
    ui->plainTextEdit->undo();
}

void ITextEditorWindow::on_actionRedo_triggered(){
    ui->plainTextEdit->redo();
}


void ITextEditorWindow::on_actionInformation_triggered(){
    this->on_actionSave_triggered();
    this->ui->plainTextEdit->setPlainText("Aplicacion creada por: Lenin Torres \n Fabian Solan \n David Monestel \n Abraham Arias");
}
