/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author 84347
 */
public class Grade {

    private int id;
    private Sinhvien sv;
    private double Toan, Ly, Hoa;

    public Grade() {
    }

    public Grade(int id, Sinhvien sv, double Toan, double Ly, double Hoa) {
        this.id = id;
        this.sv = sv;
        this.Toan = Toan;
        this.Ly = Ly;
        this.Hoa = Hoa;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Sinhvien getSv() {
        return sv;
    }

    public void setSv(Sinhvien sv) {
        this.sv = sv;
    }

    public double getToan() {
        return Toan;
    }

    public void setToan(double Toan) {
        this.Toan = Toan;
    }

    public double getLy() {
        return Ly;
    }

    public void setLy(double Ly) {
        this.Ly = Ly;
    }

    public double getHoa() {
        return Hoa;
    }

    public void setHoa(double Hoa) {
        this.Hoa = Hoa;
    }

    public double getTBC() {
        return (getToan() + getLy() + getHoa()) / 3;
    }

    public String getXeploai() {
        String xl = "";
        double tbc=getTBC();
        if(tbc>8){
            xl="Giỏi";
        }
        else if(tbc>7){
            xl="Khá";
        }
        else if(tbc>=5){
            xl="Trung Bình";
        }
        else{
            xl="Yếu";
        }
        return xl;
    }
}
