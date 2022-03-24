/*
Brian Prost
UMGC
This is a Test Class for guitar.
This creates the guitar and calls to print it.
Date: 16 June 2020
 */

public class TestGuitar {
    public static void main(String[] args) {
        // toggle comment to try different guitars
        Guitar myGuitar = new Guitar(6, 40.0, "Gibson", "black");
        // Guitar myGuitar = new Guitar(6,42.0,"Fender","cyan");
        // Guitar myGuitar = new Guitar(4,46.5,"Fender","orange");

        int numStrings = myGuitar.getStrings();
        double guitarLength = myGuitar.getLength();
        String guitarManufacturer = myGuitar.getManufacturer();
        String guitarColor = myGuitar.getColor();

        System.out.println(myGuitar.toString());
        System.out.println(myGuitar.playGuitar());
    }
}
