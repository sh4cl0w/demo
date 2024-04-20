/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;
import Database.DatabaseUtil;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author 84347
 */
public class SinhvienDAO {
SimpleDateFormat  date_format = new SimpleDateFormat("yyyy/MM/dd");
    public static List<Sinhvien> ls = new ArrayList<>();

    

   public int add(Sinhvien sv){
       Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        User u = new User();
        try {
            String sSQL = "insert into Sinhvien(MaSV,TenSV,NgaySinh,GioiTinh,DiaChi) values(?,?,?,?,?)";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(1, sv.getMaSV());
            ps.setString(2, sv.getTenSV());
            ps.setString(3, date_format.format(sv.getNgaySinh()));
            ps.setBoolean(4, sv.isGioiTinh());
            ps.setString(5, sv.getDiachi());
            
            
            if(ps.executeUpdate()>0){
                System.out.println("add thanh cong");
                return 1;
            }

        } catch (Exception e) {
            System.out.println("ERORR:" + e.toString());
        } finally {
            try {
                conn.close(); 
                rs.close();
                ps.close();
            } catch (Exception e) {
            }
            
        }
return -1;
       
       
   }

    public List<Sinhvien> getAllSinhvien() {
       List<Sinhvien> ls=new ArrayList<>();
       
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
       
        try {
            String sSQL = "Select * from Sinhvien";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            rs=ps.executeQuery();
     
            while(rs.next()){
                Sinhvien sv =new Sinhvien();
                sv.setMaSV(rs.getString(1));
                sv.setTenSV(rs.getString(2));
                sv.setNgaySinh(rs.getDate(3));
                sv.setGioiTinh(rs.getBoolean(4));
                sv.setDiachi(rs.getString(5));
                
                ls.add(sv);
            }

        } catch (Exception e) {
            System.out.println("ERORR:" + e.toString());
        } finally {
            try {
                conn.close(); 
                rs.close();
                ps.close();
            } catch (Exception e) {
            }
            
        }
return ls;
    }

    public int delSinhVienbyID(String sv){
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        User u = new User();
        try {
            String sSQL = "delete Sinhvien where MaSv=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            
           
            ps.setString(1, sv);
            
            
            if(ps.executeUpdate()>0){
                System.out.println("Xoa thanh cong");
                return 1;
            }

        } catch (Exception e) {
            System.out.println("ERORR:" + e.toString());
        } finally {
            try {
                conn.close(); 
                rs.close();
                ps.close();
            } catch (Exception e) {
            }
            
        }
return -1;

    }

    public Sinhvien getSinhVienByID(String MaSV) {
       Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Sinhvien sv = new Sinhvien();
        try {
            String sSQL = "select * from Sinhvien where MaSv=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(1, MaSV);
            rs = ps.executeQuery();
            while (rs.next()) {
                
                sv.setMaSV(rs.getString(1));
                sv.setTenSV(rs.getString(2));
                sv.setNgaySinh(rs.getDate(3));
                sv.setGioiTinh(rs.getBoolean(4));
                sv.setDiachi(rs.getString(5));
                return sv;
            }

        } catch (Exception e) {
            System.out.println("ERORR:" + e.toString());
        } finally {
            try {
                conn.close(); 
                rs.close();
                ps.close();
            } catch (Exception e) {
            }
            
        }
return null;

    }

    public int updateSinhVienbyID(Sinhvien sv) {
         Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        User u = new User();
        try {
            String sSQL = "update Sinhvien set TenSV=?,NgaySinh =?,GioiTinh=?,DiaChi=? where MaSV=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(1, sv.getTenSV());
            ps.setString(2, date_format.format(sv.getNgaySinh()));
            ps.setBoolean(3, sv.isGioiTinh());
            ps.setString(4, sv.getDiachi());
           
            ps.setString(5, sv.getMaSV());
            
            
            if(ps.executeUpdate()>0){
                System.out.println("Sua thanh cong");
                return 1;
            }

        } catch (Exception e) {
            System.out.println("ERORR:" + e.toString());
        } finally {
            try {
                conn.close(); 
                rs.close();
                ps.close();
            } catch (Exception e) {
            }
            
        }
return -1;}

}
