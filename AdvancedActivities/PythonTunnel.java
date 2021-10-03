import java.io.*;
public class PythonTunnel{
   public static void main(String... args){
      try{
         Process p = Runtime.getRuntime().exec("python grabhost.py");
         BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
         String line = "";
         while ((line = reader.readLine()) != null) {
            System.out.println(line + "\n");
         }
      }catch(Exception ignore){}
   }
}