/*
Brian Prost
UMGC
This is a class for guitar. It assigns a
number of strings, length of the guitar,
the manufacturer, and the color.
Date: 16 June 2020
 */

import java.util.Random;

public class Guitar {
    private int numStrings;
    private double guitarLength;
    private String guitarManufacturer;
    private String guitarColor;

    // default constructor
    public Guitar() {
        this.numStrings = 6;
        this.guitarLength = 28.2;
        this.guitarManufacturer = "Gibson";
        this.guitarColor = "red";
    }

    public Guitar(int gtrStrings, double gtrLength, String gtrManufacturer, String gtrColor) {
        this.numStrings = gtrStrings;
        this.guitarLength = gtrLength;
        this.guitarManufacturer = gtrManufacturer;
        this.guitarColor = gtrColor;
    }

    // getter methods
    public int getStrings() {
        return this.numStrings;
    }

    public double getLength() {
        return this.guitarLength;
    }

    public String getManufacturer() {
        return this.guitarManufacturer;
    }

    public String getColor() {
        return this.guitarColor;
    }

    // playGuitar function
    public String playGuitar() {
        String song = "Here's a song for you. It goes like this: 1, and a 2, and a 1,2,3,4!\n\n[";

        String musicalNotes = "ABCDEFG";
        Random rnd = new Random();

        for (int i = 0; i < 16; i++) {
            // generate random number no greater than 3
            char musicNote = musicalNotes.charAt(rnd.nextInt(musicalNotes.length()));
            double musicNoteLength = (rnd.nextDouble() * 3);
            song = song + musicNote + "(" + String.format("%.1f", musicNoteLength) + ")";
        }
        song = song + "]\n\n\tWow, that was beautiful! .·´¯`(>▂<)´¯`·.";
        return song;
    }

    // print
    public String toString() {
        if (this.numStrings < 5) {
            String printBass = ("This " + guitarColor + " colored " + numStrings + " stringed bass is " + guitarLength
                    + " inches long and is made by " + guitarManufacturer + ".");
            return printBass;
        } else {
            String printGtr = ("This " + guitarColor + " colored " + numStrings + " stringed guitar is " + guitarLength
                    + " inches long and is made by " + guitarManufacturer + ".");
            return printGtr;
        }
    }
}