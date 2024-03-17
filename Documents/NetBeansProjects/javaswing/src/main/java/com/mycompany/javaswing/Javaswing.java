/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.javaswing;

import java.io.IOException;
import publicPackage.User;
import java.util.ArrayList;
import publicPackage.Users;

/**
 *
 * @author 84347
 */
public class Javaswing {

    public static Users users = new Users();
    public static formDangKy fDangKy = new formDangKy();
    public static formDangNhap fDangNhap = new formDangNhap();
    public static String filePath ="data.txt";

    public static void main(String[] args) throws IOException {
        users.loadfromFile(filePath);
        fDangNhap.setVisible(true);
        fDangKy.setVisible(false);

    }

}
