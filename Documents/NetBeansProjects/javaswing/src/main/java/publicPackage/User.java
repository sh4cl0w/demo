/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package publicPackage;

/**
 *
 * @author 84347
 */
public class User {

    private String username;
    private String password;
    private String address;
    private boolean isMale;
    private String job;

    public User() {
    }

    public User(String username, String password, String address, boolean isMale, String job) {
        this.username = username;
        this.password = password;
        this.address = address;
        this.isMale = isMale;
        this.job = job;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getAddress() {
        return address;
    }

    public boolean isIsMale() {
        return isMale;
    }

    public String getJob() {
        return job;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setIsMale(boolean isMale) {
        this.isMale = isMale;
    }

    public void setJob(String job) {
        this.job = job;
    }

    @Override
    public String toString() {
        return "User{" + "username=" + username + ", password=" + password + ", address=" + address + ", isMale=" + isMale + ", job=" + job + '}';
    }

    public void showinfo() {
        System.out.println(this.toString());
    }

    public String toStringFile() {
        return username +"$"+password+"$"+address+"$"+isMale+"$"+job+"$";
    }

}
