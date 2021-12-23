package Java.unit12;

import java.io.IOException;
import java.io.PrintWriter;

public class 예외와_메소드 {
    public void writelist() throws IOException{
        예외와_메소드 out = new 예외와_메소드(new FileWriter("outfile.txt"));
    }
}
