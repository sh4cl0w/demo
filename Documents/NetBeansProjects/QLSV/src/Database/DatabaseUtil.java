/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Database;

import java.sql.Connection;
import java.sql.DriverManager;

import java.sql.SQLException;


/**
 *
 * @author 84347
 */

public class DatabaseUtil {

    /**
     *
     */
    public static final String connectionUrl ="jdbc:sqlserver://localhost:1433;"
            + "databaseName=DB_Student;user=sa;password=sa;encrypt=false";
    public static Connection getDBConnect(){
        Connection con =null;
        try {
            
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            con= DriverManager.getConnection(connectionUrl);
            return con;
      
        } catch (ClassNotFoundException ex) {
            System.out.println("ERORR:"+ex.toString());
        }catch(SQLException ex){
            System.out.println("ERORR"+ex.toString());
        }
        return null;
    }

    
}
