/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.util.Date;

/**
 *
 * @author 84347
 */
public class Sinhvien {
    private String maSV;
    private String tenSV;
    private Date ngaySinh;
    private boolean GioiTinh;
    private String Diachi;
    

    public Sinhvien(String maSV, String tenSV) {
        this.maSV = maSV;
        this.tenSV = tenSV;
    }

    public Sinhvien(String maSV, String tenSV, Date ngaySinh, boolean GioiTinh, String Diachi) {
        this.maSV = maSV;
        this.tenSV = tenSV;
        this.ngaySinh = ngaySinh;
        this.GioiTinh = GioiTinh;
        this.Diachi = Diachi;
        
    }

    public Sinhvien() {
    }

    

    public String getMaSV() {
        return maSV;
    }

    public String getTenSV() {
        return tenSV;
    }

    public Date getNgaySinh() {
        return ngaySinh;
    }

    public boolean isGioiTinh() {
        return GioiTinh;
    }

    public String getDiachi() {
        return Diachi;
    }

   

    public void setMaSV(String maSV) {
        this.maSV = maSV;
    }

    public void setTenSV(String tenSV) {
        this.tenSV = tenSV;
    }

    public void setNgaySinh(Date ngaySinh) {
        this.ngaySinh = ngaySinh;
    }

    public void setGioiTinh(boolean GioiTinh) {
        this.GioiTinh = GioiTinh;
    }

    public void setDiachi(String Diachi) {
        this.Diachi = Diachi;
    }

   
    
    
    
    
}
