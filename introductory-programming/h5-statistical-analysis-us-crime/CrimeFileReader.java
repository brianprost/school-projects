/*
CrimeFileReader.java
Brian Prost
13 July 2020
This class reads the CSV crime file
 */

// library imports
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class CrimeFileReader {

    // variables for parsing the CSV
    String splitBy = ",";

    // this will be called by TestUSCrime
    public void Open(String crimeFile) {
        // instantiate scanner outside of try statement.
        Scanner crimeDataFile = null;

        try {
            // define File class
            File myFile = new File(crimeFile);
            // new*3. but for real, this scans the file using BufferedReader
            crimeDataFile = new Scanner(new BufferedReader(new FileReader(myFile)));
            // since this is a comma seperated file, we have to define the boundaries of
            // data points by commas
            crimeDataFile.useDelimiter(splitBy);
            // call below method
            Read(crimeDataFile);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.exit(0);
        } finally {
            if (crimeDataFile != null)
                crimeDataFile.close();
        }
    }

    // called by Open
    private void Read(Scanner fileIn) {
        // variable delcarations
        String crimeStatsLine;
        String[] crimeStatsFields;
        int count = 0;

        try {
            // while loop to read all of the data points has long as there is another line.
            // originally I had declared another String variable as "" but then I found out
            // about .hasNextLine in Scanner
            while (fileIn.hasNextLine()) {
                crimeStatsLine = fileIn.nextLine();
                crimeStatsFields = crimeStatsLine.split(splitBy);

                if (count > 0) {
                    USCrime.buildList(crimeStatsFields); // add to array list in USCrime
                }
                count++;
            }
        } catch (Exception e) {
            System.out.println("There was an error accessing the file.");
            System.exit(0);
        }
    }
}
