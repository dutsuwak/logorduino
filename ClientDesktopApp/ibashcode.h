#ifndef IBASHCODE_H
#define IBASHCODE_H

#include <QMainWindow>
#include <QTcpSocket>
#include <QtDebug>

namespace Ui {class IBashCode;}

class IBashCode : public QMainWindow{

    Q_OBJECT

public:
    explicit IBashCode(QWidget *parent = 0);
    ~IBashCode();
    bool passConfigAndInit(QString pIp, int pPort);

public slots:
    void on_Bsend_clicked();
    void on_Bexit_clicked();

private slots:
    void on_lineEditCode_returnPressed();

private:
    Ui::IBashCode* ui;
    QTcpSocket* mySocket;
};

#endif // IBASHCODE_H
