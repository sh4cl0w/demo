/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package publicPackage;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/**
 *
 * @author 84347
 */
public class Users {
    ArrayList<User>users =new ArrayList<>();

    public Users() {
    }
    public void add(User u){
        this.users.add(u);
        
    }

    public ArrayList<User> getUsers() {
        return users;
    }
    public boolean contains(String username){
        for(User x:users){
            if(x.getUsername().equalsIgnoreCase(username)){
                return true;
            }
        }
        return false;
    }
    public boolean isUser(String username,String password){
        for(User x:users){
            if(x.getUsername().equals(username) && x.getPassword().equals(password)){
                return true;
            }
        }
        return false;
    }
    public void clear(){
        users.clear();
    }
    public void savetoFile(String filePath) throws IOException{
        File f =new File(filePath);
        FileWriter fw= new FileWriter(f);
        BufferedWriter bw=new BufferedWriter(fw);
        
        for(User x:users)
        {
            bw.write(x.toStringFile());
            bw.newLine();
        }
        bw.close();
        fw.close();
    }
    public void loadfromFile(String filePath) throws FileNotFoundException, IOException{
        users.clear();
        File f=new File(filePath);
        FileReader fr=new FileReader(f);
        BufferedReader br=new BufferedReader(fr);
        
        String str ="";
        while((str=br.readLine())!=null){
            
            String obj[] = str.split("\\$");
            String username=obj[0];
            String password=obj[1];
            String address=obj[2];
            boolean isMale=Boolean.parseBoolean(obj[3]);
            String job=obj[4];
            users.add(new User(username,password,address,isMale,job));
        }
        br.close();
        fr.close();
    }
    
}
