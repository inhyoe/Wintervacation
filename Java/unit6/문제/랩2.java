public class 랩2 {
    
    static void givemeastring(Object y){
        y = "This is a string";
    }
    public static void main(String[] args) {
        Object x = null;
        givemeastring(x);
        System.out.println(x);
    }
}
