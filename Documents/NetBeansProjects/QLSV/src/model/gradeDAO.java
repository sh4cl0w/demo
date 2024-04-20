/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import Database.DatabaseUtil;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author 84347
 */
public class gradeDAO {

    

    public int add(Grade g) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        
        try {
            String sSQL = "insert into Grade(MaSV,Toan,Ly,Hoa) values(?,?,?,?)";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(1, g.getSv().getMaSV());
            ps.setDouble(2, g.getToan());
            ps.setDouble(3, g.getLy());
            ps.setDouble(4, g.getHoa());

            if (ps.executeUpdate() > 0) {
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

    
        
    public List<Grade> getAllGrade(){
    List<Grade> ls = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            String sSQL="SELECT dbo.Grade.MaSV,dbo.Sinhvien.TenSV, dbo.Grade.Toan, dbo.Grade.Ly"
                    + ", dbo.Grade.Hoa FROM dbo.Grade INNER JOIN dbo.Sinhvien ON"
                    + " dbo.Grade.MaSV = dbo.Sinhvien.MaSV ";
            conn = DatabaseUtil.getDBConnect();
           ps=conn.prepareStatement(sSQL);
           rs=ps.executeQuery();
            
            while(rs.next()){
                Grade g=new Grade();
                g.setSv(new Sinhvien(rs.getString(1),rs.getString(2)));
                g.setToan(rs.getDouble(3));
                g.setLy(rs.getDouble(4));
                g.setHoa(rs.getDouble(5));
                ls.add(g);
                
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

    public Grade getOneGradebyMaSV(String masv) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Grade g = new Grade();
        try {
            String sSQL = "SELECT dbo.Grade.MaSV,dbo.Sinhvien.TenSV, dbo.Grade.Toan, dbo.Grade.Ly,"
                    + " dbo.Grade.Hoa FROM dbo.Grade INNER JOIN "
                    + "dbo.Sinhvien ON dbo.Grade.MaSV = dbo.Sinhvien.MaSV where Grade.MaSV=?";
            conn = DatabaseUtil.getDBConnect();
            ps=conn.prepareStatement(sSQL);
            ps.setString(1, masv);
            rs = ps.executeQuery();

            while (rs.next()) {
                g.setSv(new Sinhvien(rs.getString(1),rs.getString(2)));
                g.setToan(rs.getDouble(3));
                g.setLy(rs.getDouble(4));
                g.setHoa(rs.getDouble(5));
                return g;
                
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

    public int updateGrade(Grade g) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        
        try {
            String sSQL = "update Grade set Toan =?,Ly=?,Hoa=? where MaSV=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(4, g.getSv().getMaSV());
            ps.setDouble(1, g.getToan());
            ps.setDouble(2, g.getLy());
            ps.setDouble(3, g.getHoa());

            if (ps.executeUpdate() > 0) {
                System.out.println("sua thanh cong");
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

    public int delGrade(String maSV) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        User u = new User();
        try {
            String sSQL = "delete Grade where MaSV=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            
            ps.setString(1, maSV);

            if (ps.executeUpdate() > 0) {
                System.out.println("xoa thanh cong");
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
}
