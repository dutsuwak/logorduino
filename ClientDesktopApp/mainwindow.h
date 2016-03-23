#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
//#include <QTcpSocket>
#include <QHostAddress>
#include <QList>
#include <QString>
#include <QTextStream>
#include <QtGui>
#include <QtCore>
#include "ibashcode.h"
#include "itexteditorwindow.h"

namespace Ui {class MainWindow;}

class MainWindow : public QMainWindow{
    Q_OBJECT

private:
    Ui::MainWindow *ui;
    //ClientSocket* socketClient;
    //QTcpSocket* socket;
    //bool tcpsession;
    QString IP;
    int PORT;
    IBashCode* windowBash;
    ITextEditorWindow* windowTextEditor;

private slots:
    void on_B_connect_clicked();
    void secondWindow();


public slots:

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();


};

#endif // MAINWINDOW_H
