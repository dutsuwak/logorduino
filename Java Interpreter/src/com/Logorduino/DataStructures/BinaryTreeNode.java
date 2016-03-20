package com.Logorduino.DataStructures;

public class BinaryTreeNode<E>{
    
    protected String _nombre; //identificador unico para cada compuerta, creado por la GUI
    protected E _data;
    protected BinaryTreeNode<E> _leftChild;
    protected BinaryTreeNode<E> _rightChild;
    
    public BinaryTreeNode(String pID,E pDato){
        this._nombre = pID;
        this._data= pDato;
        this._leftChild=null;
        this._rightChild=null;
    }
    
    public void actualizarData(E pData){
    	this._data=pData;
    }
    
    public E getData(){
    	return this._data;
    }
    
    public String getIdentificador(){//identificador unico asignado en la GUI
        return this._nombre;
    }
 
}
