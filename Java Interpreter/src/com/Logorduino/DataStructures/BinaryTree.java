package com.Logorduino.DataStructures;

public class BinaryTree<E>{
    
    protected BinaryTreeNode<E> _primerElemento;
    protected int _nElementos; 
    
    public BinaryTree(){
        this._nElementos = 0;
        this._primerElemento = null;
    }
    
    public BinaryTreeNode<E> getRoot(){
        return this._primerElemento;
    }
    
}
