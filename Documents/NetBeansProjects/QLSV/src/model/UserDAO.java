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
public class UserDAO {

    List<User> ls = new ArrayList<>();

    public UserDAO() {
    }

    public User getuserbyID(String username) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        User u = new User();
        try {
            String sSQL = "select * from Users where username=?";
            conn = DatabaseUtil.getDBConnect();
            ps = conn.prepareStatement(sSQL);
            ps.setString(1, username);
            rs = ps.executeQuery();
            while (rs.next()) {
                u.setUsername(rs.getString(1));
                u.setPassword(rs.getString(2));
                u.setRole(rs.getBoolean(3));
                return u;
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

    
public boolean checkLogin(String username,String pass){
    User u =getuserbyID(username);
    if(u!=null){
            if(u.getPassword().equals(pass)){
                return true;
            }
    }
    return false;
}
                
}

