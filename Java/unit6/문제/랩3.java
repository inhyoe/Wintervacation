class Tv{
    private String model;
    void setModel(String model){
        this.model = model;
    }
    String getModel(){
        return model;
    }
}

public class 랩3 {
    public static void main(String[] args) {
        Tv t = new Tv();
        t.setModel("STV-101");
        String b = t.getModel();
        System.out.println(b);
    }
}
