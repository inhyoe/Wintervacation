public class 랩4 {
    private String title,director,actors;
    void settitle(String title){
        this.title = title;
    }// 접근자

    String gettitle(){
        return title;
    } // 생성자

    void setdirector(String director){
        this.director = director;
    }
    String getdirector(){
        return director;
    }
    void actors(String actors){
        this.actors = actors;
    }
    String getactors(){
        return actors;
    }
    public static void main(String[] args) {
        랩4 s = new 랩4();
        s.settitle("김노매");
        s.gettitle();
    }
}
