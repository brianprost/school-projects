/*
 * StatesDataEntry.java
 * Brian Prost
 * Homework 4
 * 05 July 2020
 */

public class UMUC_2D {
    public static void main(String[] args) {
        int row, col;
        int[][] scores; // array declaration
        scores = new int[2][3]; // creation of 2 x 3 array

        // fills a 2 x 3 array with random numbers
        for (row = 0; row < scores.length; row++) {
            for (col = 0; col < scores[row].length; col++) {
                scores[row][col] = (int) (Math.random() * 50);
            }
        }

        // prints the contents of the array
        for (row = 0; row < scores.length; row++) {
            for (col = 0; col < scores[row].length; col++) {
                System.out.print("row[" + row + "]" + "col[" + col
                        + "]=" + scores[row][col] + "  ");
            }
            System.out.println(); // moves to next line
        }
    }
}
