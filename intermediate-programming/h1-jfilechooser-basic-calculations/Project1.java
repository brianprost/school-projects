/*
 * Weight.java
 * Brian Prost
 * 06 October 2020
 * Project 1
 */

package homeworkBar;

import java.io.*;
import java.util.Scanner;
import javax.swing.JFileChooser;

public class Project1 {

    // main method
    public static void main(String[] args) {
        // declarations
        Weight[] weightArray = new Weight[25];
        Scanner sc;
        int response;

        // JFileChooser initialization
        JFileChooser jfc = new JFileChooser(".");
        jfc.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
        response = jfc.showOpenDialog(null);
        String dl = ",";

        // loop to read all values in file
        if (response == JFileChooser.APPROVE_OPTION) {
            File file = jfc.getSelectedFile();
            int count = 0;

            try {
                sc = new Scanner(file);
                sc.useDelimiter(dl);

                while (sc.hasNextLine()) {
                    String[] breakLine = sc.nextLine().split(dl);
                    int lb = Integer.parseInt(breakLine[0]);
                    double ounce = Double.parseDouble(breakLine[1]);
                    weightArray[count] = new Weight(lb, ounce);
                    // System.out.println(weightArray[count]);
                    count++;
                }
                sc.close();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        // calls
        System.out.println("Thanks for all that info. Here's what I have to say about it:");

        // minimum
        System.out.println("Your minimum weight: ");
        int minimumWeight = findMinimum(weightArray);
        weightArray[minimumWeight].normalize();
        System.out.println(weightArray[minimumWeight]);

        // maximum
        System.out.println("Your maximum weight: ");
        int maximumWeight = findMaximum(weightArray);
        System.out.println(weightArray[maximumWeight]);

        // average
        System.out.println("Your average weight: ");
        double average = findAverage(weightArray);
        Weight avgOfArray = new Weight(0, average);
        avgOfArray.normalize();
        System.out.println(avgOfArray);
    }

    // methods:

    private static int findMinimum(Weight[] weightArray) {
        double min = weightArray[0].toOunces();
        int minIndex = 0;
        for (int i = 0; i < weightArray.length; i++) {
            if (weightArray[i].toOunces() < min) {
                min = weightArray[i].toOunces();
                minIndex = i;
            }
        }
        return minIndex;
    }

    private static int findMaximum(Weight[] weightArray) {
        double max = weightArray[0].toOunces();
        int maxIndex = 0;
        for (int i = 0; i < weightArray.length; i++) {
            if (weightArray[i].toOunces() > max) {
                max = weightArray[i].toOunces();
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    private static double findAverage(Weight[] weightArray) {

        double sum = 0;

        for (Weight weight : weightArray) {
            sum += weight.toOunces();
        }

        return sum / weightArray.length;
    }

}
